# katas

def i_create_a_project(project_data):
    CONTEXT.project_status, CONTEXT.project_response = project_service.create_project(project_data)


def i_verify_project_creation_status_is(status_code):
    assert CONTEXT.project_status is int(status_code), "Project Status code is {}".format(CONTEXT.project_status)


def i_verify_data_of_project_is_accurate(project_data):
    actual_response = project_service.get_project(id=str(CONTEXT.project_response["id"]))
    for key, value in project_data.items():
        assert actual_response[key] == value, "Project data {} != {}".format(actual_response[key], value)


def i_verify_project_schema():
    actual_response = project_service.get_project(id=str(CONTEXT.project_response["id"]))
    schema = project_service.get_project_schema()
    schema_failure_reason, is_schema_valid = validate_json_schema(schema, actual_response)
    BuiltIn().should_be_true(is_schema_valid, "Project Schema failed due to: {}".format(schema_failure_reason))


def i_delete_all_project
    project_service.delete_all_projects()
    
    
    
To install:
jsonschema
simplejson