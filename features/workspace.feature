Feature: Work with workspaces

  Background:
    Given I have the workspaces list

  Scenario Outline: Create new workspace <name>
    Given I created the workspace <name>
    Then verify the creation status is 200
    And verify the workspace schema
    And verify the workspace <name> exists
    Examples: Workspaces
      | name         |
      | Workspace_01 |
      | Workspace_02 |
      | Workspace_03 |

  Scenario: Details of existent workspace
    Given I selected Workspace_01 from the list
    When I requested its details
    Then verify the get status is 200
    And verify the workspace schema

  Scenario: Details of non-existent workspace
    Given I selected Non-Existent from the list
    When I requested its details
    Then verify the get status is 404
    And the response reason is "Not Found"

  Scenario: Details of non-authorized workspace
    Given I selected Non-Authorized from the list
    When I requested its details
    Then verify the get status is 403
    And the response reason is "Forbidden"

  Scenario: Delete a existent workspace
    Given I selected Workspace_03 from the list
    When I requested delete it
    Then verify the deletion status is 204
    And the response reason is "No Content"

  Scenario: Delete a non-existent workspace
    Given I selected Non-Existent from the list
    When I requested delete it
    Then verify the deletion status is 404
    And the response reason is "Not Found"

  Scenario: Delete all workspaces
    Given I delete all the workspaces
    Then verify the list is empty


# Feature: Work with projects into workspaces
  # Scenario: Add list of projects to a workspace
  # Scenario: Same project can be on multiple workspaces
  # Scenario: remove a project from a workspace
  # Scenario: remove all projects from a workspace

#  https://www.pivotaltracker.com/services/v5/my/workspaces/123456
#  code 403 Forbidden
#  {
#    "code": "unauthorized_operation",
#    "kind": "error",
#    "error": "Authorization failure.",
#    "general_problem": "You aren't authorized to access the requested resource.",
#    "possible_fix": "Your project permissions are determined on the Project Membership page. If you are receiving this error you may be trying to access the wrong project, or the project API access is disabled, or someone listed as the project's Owner needs to change your membership type."
#}

#  https://www.pivotaltracker.com/services/v5/my/workspaces/12345644
#  code 404 Not Found
#    {
#    "code": "unfound_resource",
#    "kind": "error",
#    "error": "The object you tried to access could not be found.  It may have been removed by another user, you may be using the ID of another object type, or you may be trying to access a sub-resource at the wrong point in a tree."
#}