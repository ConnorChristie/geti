# Copyright (C) 2022-2025 Intel Corporation
# LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE
from unittest.mock import patch

from bson import ObjectId

from iai_core.repos.base import SessionBasedRepo
from iai_core.repos.base.session_repo import QueryAccessMode

from geti_types import ProjectIdentifier, make_session


class TestProjectBasedSessionRepo:
    def test_preliminary_query_match_filter(self, fxt_ote_id, fxt_project_based_session_repo) -> None:
        session = make_session()
        project_identifier = ProjectIdentifier(
            workspace_id=session.workspace_id,
            project_id=fxt_ote_id(2),
        )
        repo = fxt_project_based_session_repo(session=session, project_identifier=project_identifier)

        with patch.object(
            SessionBasedRepo, "preliminary_query_match_filter", return_value={}
        ) as mock_super_match_filter:
            out_filter = repo.preliminary_query_match_filter(access_mode=QueryAccessMode.READ)

        mock_super_match_filter.assert_called_once_with(access_mode=QueryAccessMode.READ)
        assert out_filter == {
            "workspace_id": ObjectId(str(project_identifier.workspace_id)),
            "project_id": ObjectId(str(project_identifier.project_id)),
        }

    def test_indexes(self, fxt_ote_id, fxt_project_based_session_repo) -> None:
        session = make_session()
        project_identifier = ProjectIdentifier(
            workspace_id=fxt_ote_id(1),
            project_id=fxt_ote_id(2),
        )
        repo = fxt_project_based_session_repo(session=session, project_identifier=project_identifier)

        indexes_names = set(repo._collection.index_information().keys())

        assert indexes_names == {
            "_id_",
            "organization_id_-1_workspace_id_-1_project_id_-1__id_1",
        }
