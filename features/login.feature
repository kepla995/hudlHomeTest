Feature: Login User via various methods

    Scenario: Non-registered User cannot login
        Given I am on the login page
        When I enter my email
        And I enter my password
        And I press the login button
        Then I should not be able to login
        And I should see incorrect username or password error message



