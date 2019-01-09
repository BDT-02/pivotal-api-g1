import unittest
from mock import patch

from src.pivotal_api_services.projects import ProjectServices


class TestProject(unittest.TestCase):

    def setUp(self):
        self.project = ProjectServices()

    @patch('src.core.api.request_handler.RequestHandler.post_request')
    def test_create_project(self, mock_project):
        mock_project.return_value.status_code = 200
        mock_project.return_value.json.return_value = self._project_object()

        data = {"name": "foobar"}
        status_code, project_json = self.project.create_project(data)

        self.assertEquals(200, status_code)
        self.assertEquals(self._project_object(), project_json)

    # Following methods returns mocked results
    @staticmethod
    def _project_object():
        response = {
            "id": 2233328,
            "kind": "project",
            "name": "foobar",
            "version": 1,
            "iteration_length": 1,
            "week_start_day": "Monday",
            "point_scale": "0,1,2,3",
            "point_scale_is_custom": False,
            "bugs_and_chores_are_estimatable": False,
            "automatic_planning": True,
            "enable_tasks": True,
            "time_zone": {
                "kind": "time_zone",
                "olson_name": "America/Los_Angeles",
                "offset": "-08:00"
            },
            "velocity_averaged_over": 3,
            "number_of_done_iterations_to_show": 4,
            "has_google_domain": False,
            "enable_incoming_emails": True,
            "initial_velocity": 10,
            "public": False,
            "atom_enabled": False,
            "project_type": "private",
            "start_time": "2019-01-07T08:00:00Z",
            "created_at": "2018-12-19T13:06:41Z",
            "updated_at": "2018-12-19T14:01:22Z",
            "account_id": 987701,
            "current_iteration_number": 1,
            "enable_following": True
        },

        return response
