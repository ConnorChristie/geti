# Copyright (C) 2022-2025 Intel Corporation
# LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE

"""This module implements the MongoDB mappers for active suggestion entities"""

from active_learning.entities import ActiveSuggestion

from iai_core.repos.mappers.mongodb_mapper_interface import IMapperSimple

__all__ = ["ActiveSuggestionToMongo"]

from iai_core.repos.mappers.mongodb_mappers.id_mapper import IDToMongo
from iai_core.repos.mappers.mongodb_mappers.media_mapper import MediaIdentifierToMongo


class ActiveSuggestionToMongo(IMapperSimple[ActiveSuggestion, dict]):
    """MongoDB mapper for `ActiveSuggestion` entities"""

    @staticmethod
    def forward(instance: ActiveSuggestion) -> dict:
        return {
            "_id": IDToMongo.forward(instance.id_),
            "media_identifier": MediaIdentifierToMongo.forward(instance.media_identifier),
            "score": instance.score,
            "models": [IDToMongo.forward(model_id) for model_id in instance.models],
            "user": instance.user,
            "reason": instance.reason,
        }

    @staticmethod
    def backward(instance: dict) -> ActiveSuggestion:
        media_identifier = MediaIdentifierToMongo.backward(instance["media_identifier"])
        models = [IDToMongo.backward(model_id) for model_id in instance["models"]]
        return ActiveSuggestion(
            id_=IDToMongo.backward(instance["_id"]),
            media_identifier=media_identifier,
            score=instance["score"],
            models=models,
            user=instance["user"],
            reason=instance["reason"],
            ephemeral=False,
        )
