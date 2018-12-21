Feature: showing off behave

  Scenario: Create new workspace
    Given I create a workspace
        | name | First Workspace|
    Then I verify workspace creation status is 200
    And I verify workspace schema