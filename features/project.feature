Feature: showing off behave

  Scenario: Create new project
    Given I create a project
        | name | First Project|
    Then I verify project creation status is 200
    And I verify project schema