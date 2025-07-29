Feature: New Users can register and create accounts via various methods

    Scenario: Email User can register and login
        Given I am on the login page
        When I click on the register button
        And I enter my email
        And I enter my password
        And I press the register button
        Then I should be registered successfully

    Scenario: Google User can register and login
        Given I am on the login page
        When I click on the register with Google button
        And I authenticate with Google
        Then I should be registered successfully

    Scenario: Facebook User can register and login
        Given I am on the login page
        When I click on the register with Facebook button
        And I authenticate with Facebook
        Then I should be registered successfully

    Scenario: Apple User can register and login
        Given I am on the login page
        When I click on the register with Apple button
        And I authenticate with Apple
        Then I should be registered successfully    