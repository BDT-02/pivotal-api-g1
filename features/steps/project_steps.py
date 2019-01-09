import time

from behave import Given, then, step

from src.pivotal_api_services.projects import ProjectServices
from src.utils.json_schema_validator import validate_json_schema

project_services = ProjectServices()


@Given(u"I create a project")
def create_project_step(context):
    data = {"name": "New Project1"}
    context.project_status, context.project_response = project_services.create_project(data)


@then(u'I verify project creation status is {status_code}')
def step_impl(context, status_code):
    print(context.project_status)
    assert context.project_status == int(status_code), "Project creation status is %s" % status_code


@step(u'I verify project schema')
def step_impl(context):
    actual_response = project_services.get_project(id=str(context.project_response["id"]))
    schema = project_services.get_project_schema()
    is_schema_valid, schema_failure_reason = validate_json_schema(schema, actual_response)
    assert is_schema_valid, "Project Schema failed due to: {}".format(schema_failure_reason)


@Given("I delete all projects")
def step_impl(context):
    project_services.delete_all_projects()
