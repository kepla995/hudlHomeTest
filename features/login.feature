Feature: Login User via various methods

    Scenario: Non-registered User cannot login
        Given I am on the login page
        When I enter my email
        And I enter my password
        And I press the login button
        Then I should not be able to login
        And I should see incorrect username or password error message 
    
    Scenario: Email User can login
        Given I am on the login page
        When I enter my email
        And I enter my password
        And I press the login button
        Then I should be logged in successfully

     Scenario: Google User can login
        Given I am on the login page
        When I select the Google login option
        And I enter my Google credentials
        And I press the login button
        Then I should be logged in successfully

    Scenario: Facebook User can login
        Given I am on the login page
        When I select the Facebook login option
        And I enter my Facebook credentials
        And I press the login button
        Then I should be logged in successfully

    Scenario: Apple User can login
        Given I am on the login page
        When I select the Apple login option
        And I enter my Apple credentials
        And I press the login button
        Then I should be logged in successfully

