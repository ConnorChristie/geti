# Copyright (C) 2022-2025 Intel Corporation
# LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE

"""
This module contains the FeatureFlagProvider class
"""

import logging
import os
from enum import Enum, auto

from iai_core.utils.type_helpers import str2bool

logger = logging.getLogger(__name__)


class FeatureFlag(Enum):
    FEATURE_FLAG_ANOMALY_REDUCTION = auto()
    FEATURE_FLAG_KEYPOINT_DETECTION = auto()
    FEATURE_FLAG_RETAIN_TRAINING_ARTIFACTS = auto()
    FEATURE_FLAG_STORAGE_SIZE_COMPUTATION = auto()
    FEATURE_FLAG_CREDIT_SYSTEM = auto()
    FEATURE_FLAG_NEW_CONFIGURABLE_PARAMETERS = auto()


class FeatureFlagProvider:
    @staticmethod
    def is_enabled(feature_flag: FeatureFlag) -> bool:
        """
        Returns whether the provided feature flag is enabled

        :param feature_flag: the feature flag to check
        :return: True if enabled, false otherwise
        """
        value = os.environ.get(feature_flag.name)
        if not value:
            logger.warning(
                "Attempting to access undefined flag %s. Returning false.",
                feature_flag.name,
            )
            enabled = False
        else:
            enabled = str2bool(value)
        return enabled
