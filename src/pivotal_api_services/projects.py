from src.pivotal_api_services.pivotal_services import PivotalServices
from src.utils.LoggerHandler import LoggerHandler
from src.utils.file_reader import FileReader
from src.utils.string_handler import StringHandler

logger = LoggerHandler.get_instance()
class ProjectServices(PivotalServices):

    def __init__(self):
        super(ProjectServices, self).__init__()
        self.__project = "{}/projects".format(self.request_handler.main_url)
        self.__project_schema_path = "/src/core/api/json_schemas/project_schema.json"
        self.project = {}
        self.projects = {}

    def create_project(self, data):
        response = self.request_handler.post_request(endpoint=self.__project, body=data)
        return response.status_code, response.json()

    def get_projects(self):
        project_list = self.request_handler.get_request(endpoint=self.__project).json()
        for project in project_list:
            if not project['name'] in self.projects:
                self.projects[project['name']] = project['id']
        return self.projects

    def get_project(self, id):
        current_url = self.__project + "/" + id
        project = self.request_handler.get_request(endpoint=current_url).json()
        if not project['name'] in self.projects:
            self.projects[project['name']] = project['id']
        return project

    def get_project_schema(self):
        return StringHandler.convert_string_to_json(FileReader.get_file_content(self.__project_schema_path))

    def delete_all_projects(self):
        self.get_projects()
        for project in self.projects.values():
            url = self.__project + "/" + str(project)
            logger.info("Deleting %s" % url)
            self.request_handler.delete_request(endpoint=url)
