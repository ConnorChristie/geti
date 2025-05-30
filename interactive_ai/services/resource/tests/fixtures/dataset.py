# Copyright (C) 2022-2025 Intel Corporation
# LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE

import pytest

from iai_core.entities.dataset_item import DatasetItem
from iai_core.entities.datasets import Dataset
from iai_core.entities.subset import Subset
from iai_core.repos import DatasetRepo


@pytest.fixture
def fxt_empty_dataset(fxt_dataset_storage, fxt_mongo_id):
    """Empty dataset"""
    yield Dataset(items=[], id=fxt_mongo_id(100))


@pytest.fixture
def fxt_dataset_item(fxt_image_entity_factory, fxt_annotation_scene):
    """
    DatasetItem with a media and annotation
    The subset can be specified by parameter.
    """

    def _build_item(index: int = 1, subset: Subset = Subset.NONE, cropped: bool = False):
        if cropped:
            roi = fxt_annotation_scene.annotations[0]
        else:
            roi = None
        return DatasetItem(
            media=fxt_image_entity_factory(index=index),
            annotation_scene=fxt_annotation_scene,
            roi=roi,
            subset=subset,
            id_=DatasetRepo.generate_id(),
        )

    yield _build_item


@pytest.fixture
def fxt_empty_dataset_item(fxt_image_entity_factory, fxt_annotation_scene_empty):
    """
    DatasetItem with a media and annotation
    The subset can be specified by parameter.
    """

    def _build_item(index: int = 1, subset: Subset = Subset.NONE, cropped: bool = False):
        return DatasetItem(
            media=fxt_image_entity_factory(index=index),
            annotation_scene=fxt_annotation_scene_empty,
            roi=None,
            subset=subset,
            id_=DatasetRepo.generate_id(),
        )

    yield _build_item


@pytest.fixture
def fxt_dataset_item_anomalous(fxt_image_entity_factory, fxt_annotation_scene_anomalous):
    """
    DatasetItem with a media and anomalous annotation.
    The subset can be specified by parameter.
    """

    def _build_item(index: int = 1, subset: Subset = Subset.NONE):
        return DatasetItem(
            media=fxt_image_entity_factory(index=index),
            annotation_scene=fxt_annotation_scene_anomalous,
            subset=subset,
            id_=DatasetRepo.generate_id(),
        )

    yield _build_item


@pytest.fixture
def fxt_dataset_non_empty(fxt_dataset_item, fxt_dataset_storage, fxt_mongo_id):
    """Dataset with 3 items, belonging to train, valid and test subsets, respectively"""

    items = [
        fxt_dataset_item(index=1, subset=Subset.TRAINING),
        fxt_dataset_item(index=2, subset=Subset.VALIDATION),
        fxt_dataset_item(index=3, subset=Subset.TESTING),
    ]
    dataset = Dataset(items=items, id=fxt_mongo_id(1))
    yield dataset


@pytest.fixture
def fxt_dataset_non_empty_2(fxt_dataset_item, fxt_dataset_storage, fxt_mongo_id):
    """Dataset with 3 items, belonging to train, valid and test subsets, respectively"""

    items = [
        fxt_dataset_item(index=4, subset=Subset.TRAINING),
        fxt_dataset_item(index=5, subset=Subset.VALIDATION),
        fxt_dataset_item(index=6, subset=Subset.TESTING),
    ]
    dataset = Dataset(items=items, id=fxt_mongo_id(2))
    yield dataset


@pytest.fixture
def fxt_dataset(fxt_dataset_non_empty):
    yield fxt_dataset_non_empty


@pytest.fixture
def fxt_dataset_training_subset_only(fxt_dataset_item, fxt_dataset_storage, fxt_mongo_id):
    """Dataset with only items in the train subset"""
    items = [
        fxt_dataset_item(index=1, subset=Subset.TRAINING),
        fxt_dataset_item(index=2, subset=Subset.TRAINING),
    ]
    dataset = Dataset(items=items, id=fxt_mongo_id(2))
    yield dataset


@pytest.fixture
def fxt_dataset_invalid_subset(fxt_dataset_item, fxt_dataset_storage, fxt_mongo_id):
    """
    Dataset with 4 items, one belonging to train, valid and test subsets, and one item
    belonging to 'NONE' subset
    """

    items = [
        fxt_dataset_item(index=1, subset=Subset.TRAINING),
        fxt_dataset_item(index=2, subset=Subset.VALIDATION),
        fxt_dataset_item(index=3, subset=Subset.TESTING),
        fxt_dataset_item(index=4, subset=Subset.NONE),
    ]
    dataset = Dataset(items=items, id=fxt_mongo_id(2))
    yield dataset


@pytest.fixture
def fxt_dataset_counts(fxt_dataset_storage, fxt_dataset):
    yield {
        "dataset_storage_id": fxt_dataset_storage.id_,
        "dataset_revision_id": fxt_dataset.id_,
        "n_samples": 1,
        "n_images": 2,
        "n_videos": 1,
        "n_frames": 3,
    }
