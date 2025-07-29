Feature: New Users can register an account when all password requirements are met

    Scenario: All password requirements are met
        Given I am on the login page
        When I click on the register button
        And I enter my email
        And I enter a valid password
        Then all password requirements should be green
        When I press the register button
        Then I should be registered successfully

    
     Scenario: No password requirements are met
        Given I am on the login page
        When I click on the register button
        And I enter my email
        And I enter a invalid password
        Then all password requirements should be red
        When I press the register button
        Then I should see an error message indicating password requirements are not met
