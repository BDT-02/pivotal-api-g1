from behave import given, when, then

from src.pivotal_api_services.workspaces import WorkspaceServices
from src.utils.json_schema_validator import validate_json_schema

workspace_services = WorkspaceServices()
other_workspaces = {"Non-Existent": "1", "Non-Authorized": "12E45"}


@given("I have the workspaces list")
def step_impl(context):
    context.workspace_list = workspace_services.get_workspaces()


@given("I created the workspace {name}")
def create_workspace_step(context, name):
    data = {"name": name}
    context.response_status, context.workspace_response = workspace_services.create_workspace(data)


@then("verify the {action_type} status is {status_code}")
def verify_action_status(context, action_type, status_code):
    assert context.response_status == int(status_code), \
        "Workspace %s status is %s" % (action_type, status_code)


@then("verify the workspace schema")
def verify_workspace_schema(context):
    workspace = workspace_services.get_workspace(id=str(context.workspace_response["id"])).json()
    schema = workspace_services.get_workspace_schema()
    is_schema_valid, schema_failure_reason = validate_json_schema(schema, workspace)
    assert is_schema_valid, "Workspace Schema failed due to: {}".format(schema_failure_reason)


@then("verify the workspace {name} exists")
def verify_workspace_exists(context, name):
    assert name in context.workspace_list, "Workspace {} is not in the list".format(name)


@given("I selected {name} from the list")
def step_impl(context, name):
    context.workspace_id = other_workspaces[name] if name in other_workspaces \
        else context.workspace_list[name]


@when("I requested its details")
def step_impl(context):
    response = workspace_services.get_workspace(context.workspace_id)
    context.workspace_response = response.json()
    context.response_status = response.status_code
    context.response_reason = response.reason


@when("I requested delete it")
def step_impl(context):
    context.response_status, context.response_reason = \
        workspace_services.delete_workspace(context.workspace_id)


@then('the response reason is "{reason}"')
def step_impl(context, reason):
    assert context.response_reason == reason, "Workspace response reason is '%s'" % reason


@given("I delete all the workspaces")
def delete_workspaces(context):
    workspace_services.delete_all_workspaces()


@then("verify the list is empty")
def step_impl(context):
    assert not workspace_services.get_workspaces(), "There is still workspaces"
