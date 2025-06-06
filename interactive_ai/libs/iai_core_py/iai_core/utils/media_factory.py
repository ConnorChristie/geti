# Copyright (C) 2022-2025 Intel Corporation
# LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE

"""
This module implements a singleton-class that fetches media for a given identifier
"""

import io
from typing import BinaryIO

import cv2
import numpy as np

from iai_core.entities.media import ImageExtensions
from iai_core.entities.media_2d import Media2D
from iai_core.entities.video import VideoFrame
from iai_core.repos.storage.binary_repos import ThumbnailBinaryRepo
from iai_core.utils.constants import DEFAULT_THUMBNAIL_SIZE

from geti_types import DatasetStorageIdentifier, ImageIdentifier, MediaIdentifierEntity, Singleton, VideoFrameIdentifier


class Media2DFactory(metaclass=Singleton):
    """
    The Media2DFactory is a singleton-class that fetches media for a given identifier.
    For example, a VideoFrameIdentifier can be traded for a VideoFrame entity.
    """

    @staticmethod
    def get_media_for_identifier(
        media_identifier: MediaIdentifierEntity,
        dataset_storage_identifier: DatasetStorageIdentifier,
    ) -> Media2D:
        """
        Retrieves media from the database based on a media identifier

        :param media_identifier: Identifier of the media to fetch
        :param dataset_storage_identifier: Identifier of the DS containing the media
        :return: Media entity
        """
        from iai_core.repos import ImageRepo, VideoRepo

        if isinstance(media_identifier, VideoFrameIdentifier):
            video_repo = VideoRepo(dataset_storage_identifier)
            return VideoFrame(
                video_repo.get_by_id(media_identifier.media_id),
                media_identifier.frame_index,
            )
        if isinstance(media_identifier, ImageIdentifier):
            image_repo = ImageRepo(dataset_storage_identifier)
            return image_repo.get_by_id(media_identifier.media_id)
        raise ValueError(
            f"Could not retrieve 2D-media for `{media_identifier}`, instance of `{repr(media_identifier)}`"
        )

    @staticmethod
    def crop_to_thumbnail(media_numpy: np.ndarray, target_height: int, target_width: int) -> np.ndarray:
        """
        Crop an image to a thumbnail. The image is first scaled according to the side with the least amount of
        rescaling, and then the other side is cropped. In this way, a maximal portion of the image is visible in the
        thumbnail.

        :param media_numpy: media to crop to thumbnail, represented in numpy RGB
        :param target_height: target height to crop the thumbnail to
        :param target_width: target width to crop the thumbnail to
        """
        initial_height, initial_width = media_numpy.shape[0:2]
        scale_width = target_width / initial_width
        scale_height = target_height / initial_height
        scaling_factor = max(scale_width, scale_height)
        resized_media = cv2.resize(
            media_numpy,
            (int(initial_width * scaling_factor), int(initial_height * scaling_factor)),
            interpolation=cv2.INTER_AREA,
        )
        current_width, current_height = resized_media.shape[1], resized_media.shape[0]
        # cropping
        x1 = (current_width - target_width) / 2
        x2 = x1 + target_width
        y1 = (current_height - target_height) / 2
        y2 = y1 + target_height
        x1 = int(round(max(x1, 0)))
        x2 = int(round(min(x2, current_width)))
        y1 = int(round(max(y1, 0)))
        y2 = int(round(min(y2, current_height)))
        return resized_media[y1:y2, x1:x2]

    @staticmethod
    def create_and_save_media_thumbnail(
        dataset_storage_identifier: DatasetStorageIdentifier,
        media_numpy: np.ndarray,
        thumbnail_binary_filename: str,
    ) -> BinaryIO:
        """
        Creates and saves a thumbnail for the media

        :param dataset_storage_identifier: Identifier of the dataset storage containing the media
        :param media_numpy: Base media to use for thumbnail generation.
        :param thumbnail_binary_filename: Binary filename for the thumbnail used to save it in the binary repo
        :return: The created thumbnail as np array.
        """
        # Create and save thumbnail
        thumbnail = Media2DFactory.crop_to_thumbnail(
            media_numpy=media_numpy,
            target_height=DEFAULT_THUMBNAIL_SIZE,
            target_width=DEFAULT_THUMBNAIL_SIZE,
        )
        im_bgr = cv2.cvtColor(thumbnail, cv2.COLOR_RGB2BGR)
        _, data = cv2.imencode(ImageExtensions.JPG.value, im_bgr)
        im_bytes = data.tobytes()
        ThumbnailBinaryRepo(dataset_storage_identifier).save(
            data_source=im_bytes, dst_file_name=thumbnail_binary_filename
        )
        return io.BytesIO(im_bytes)
