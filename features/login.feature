Feature: Login User via Email & Passord

       Scenario: Non-registered User cannot login
        Given I am on the login page
        When I enter an un-registered email
        And I enter a password
        And I press the login button
        Then I should not be able to login
        And I should see incorrect username or password error message 
    
    Scenario: User cannot login with incorrect password
        Given I am on the login page
        When I enter a valid email
        And I enter a password
        And I press the login button
        Then I should not be able to login
        And I should see incorrect password error message
    
    Scenario: Email User can login
        Given I am on the login page
        When I enter a valid email
        And I enter a valid password
        And I press the login button
        Then I should be logged in successfully
        And I can logout successfully

    Scenario: User can reset password
        Given I am on the login page
        When I enter a valid email
        And I press the forgot password link
        Then I should be redirected to the password reset page

     