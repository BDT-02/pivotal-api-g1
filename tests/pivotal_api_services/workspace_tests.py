import unittest
from mock import patch

from src.pivotal_api_services.workspaces import WorkspaceServices


class TestWorkspaces(unittest.TestCase):

    def setUp(self):
        self.workspace = WorkspaceServices()

    @patch('src.core.api.request_handler.RequestHandler.post_request')
    def test_create_workspace(self, mock_workspace):
        mock_workspace.return_value.status_code = 200
        mock_workspace.return_value.json.return_value = self._workspace_object()

        data = {"name": "foobar"}
        status_code, workspace_json = self.workspace.create_workspace(data)

        self.assertEquals(200, status_code)
        self.assertEquals(self._workspace_object(), workspace_json)

    @patch('src.core.api.request_handler.RequestHandler.post_request')
    def test_create_workspace_fails(self, mock_workspace):
        mock_workspace.return_value.status_code = 400
        mock_workspace.return_value.json.return_value = self._workspace_creation_failed()

        data = {"name1": "foobar"}
        status_code, workspace_json = self.workspace.create_workspace(data)

        self.assertEquals(400, status_code)
        self.assertEquals(self._workspace_creation_failed(), workspace_json)

    # Following methods returns mocked results
    @staticmethod
    def _workspace_object():
        response = {
            "kind": "workspace",
            "id": 123,
            "name": "foobar",
            "person_id": 789,
            "project_ids": []
        }

        return response

    @staticmethod
    def _workspace_list():
        workspaces = {
            "workspace_01": 12345,
            "workspace_03": 78965,
        }

        return workspaces

    @staticmethod
    def _workspace_creation_failed():
        response = {
            "code": "invalid_parameter",
            "error": "One or more request parameters was missing or invalid."
        }
        return response


if __name__ == '__main__':
    unittest.main()
