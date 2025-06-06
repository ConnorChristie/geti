# Copyright (C) 2022-2025 Intel Corporation
# LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE
import logging

from geti_telemetry_tools import unified_tracing
from geti_types import ID
from iai_core.entities.evaluation_result import EvaluationPurpose
from iai_core.repos import EvaluationResultRepo, ProjectRepo

logger = logging.getLogger(__name__)


class UpdateProjectPerformanceUseCase:
    @staticmethod
    @unified_tracing
    def update_project_performance(
        project_id: ID,
        task_node_id: ID,
        inference_model_id: ID,
    ) -> None:
        """
        Update task performance and project score in project performance.

        :param project_id: ID of the project that the task and model belong to
        :param task_node_id: ID of the task that has newly activated model
        :param inference_model_id: ID of the newly activated inference model
        """
        project_repo: ProjectRepo = ProjectRepo()
        project = project_repo.get_by_id(project_id)

        evaluation_result_repo: EvaluationResultRepo = EvaluationResultRepo(project.identifier)
        model_performance = evaluation_result_repo.get_performance_by_model_ids(
            equivalent_model_ids=[inference_model_id], purpose=EvaluationPurpose.TEST
        )

        logger.info(
            "Updating project performance, because a new model got activated. "
            "Current project performance: %s, "
            "Project ID: %s, "
            "TaskNode ID: %s, "
            "New model performance: %s. ",
            project.performance,
            project_id,
            task_node_id,
            model_performance,
        )
        project.performance.update_task_performance(task_node_id=task_node_id, model_performance=model_performance)
        project_repo.update_project_performance(project_id=project.id_, project_performance=project.performance)

        logger.info(
            "Updated project performance: %s.",
            project.performance,
        )
