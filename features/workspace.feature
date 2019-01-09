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
