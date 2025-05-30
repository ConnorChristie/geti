// Copyright (C) 2022-2025 Intel Corporation
// LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE

package usecase

import (
	"context"
	"fmt"
	"io"

	sdkentities "geti.com/iai_core/entities"
	"geti.com/iai_core/logger"
	"geti.com/iai_core/storage"

	"media/app/service"
)

const defaultThumbSize = 256

type NotFoundError struct {
	Message string
}

func (e *NotFoundError) Error() string {
	return e.Message
}

type IGetOrCreateThumbnail interface {
	Execute(ctx context.Context, imageID *sdkentities.FullImageID) (io.ReadCloser, *sdkentities.ObjectMetadata, error)
}

type GetOrCreateThumbnail struct {
	imageRepo storage.ImageRepository
	cropper   service.Cropper
}

func NewGetOrCreateImageThumbnail(imageRepo storage.ImageRepository, cropper service.Cropper) *GetOrCreateThumbnail {
	return &GetOrCreateThumbnail{
		imageRepo: imageRepo,
		cropper:   cropper,
	}
}

// Execute generates a thumbnail for the image with the specified ID and saves it to the storage.
// The method is agnostic to S3 being enabled or disabled.
func (uc *GetOrCreateThumbnail) Execute(ctx context.Context, imageID *sdkentities.FullImageID) (io.ReadCloser, *sdkentities.ObjectMetadata, error) {
	thumbnail, metadata, err := uc.imageRepo.LoadThumbnailByID(ctx, imageID)
	if err != nil {
		logger.TracingLog(ctx).Infof(
			"Thumbnail for Image with ID %s does not yet exist. Attempting to generate one.", imageID)
		reader, _, err := uc.imageRepo.LoadImageByID(ctx, imageID)
		if err != nil {
			return nil, nil, &NotFoundError{"Image not found"}
		}
		croppedImage, err := uc.cropper.CropImage(reader, defaultThumbSize, defaultThumbSize)
		if err != nil {
			return nil, nil, err
		}
		if err = uc.imageRepo.SaveThumbnail(ctx, imageID, croppedImage); err != nil {
			return nil, nil, fmt.Errorf("cannot save thumbnail: %s", err)
		}
		logger.TracingLog(ctx).Infof("Successfully generated thumbnail for Image with ID %s", imageID)
		thumbnail, metadata, err = uc.imageRepo.LoadThumbnailByID(ctx, imageID)
		if err != nil {
			return nil, nil, &NotFoundError{"Thumbnail not found"}
		}
	}
	return thumbnail, metadata, nil
}
