Feature: New Users can register an account when all password requirements are met

    Scenario Outline: Password requirements are met
        Given I am on the login page
        When I click on the register button
        And I enter my email
        And I enter a '<passwordType>' password - '<password>'
        Then the correct requirements should be displayed as green
        And the registration should result in a '<result>'
    Examples:
      | PasswordType | Password         | Result |
      | tooShort     | ABc1!            | Fail   |
      | noLetter     | 12345!?$         | Fail   |
      | noSpecial    | Abc12345         | Pass   |
      | noNumber     | Abcdefgh!        | Pass   |
      | noUpper      | abcd1234#        | Pass   |
      | noLower      | ABCDE123?        | Pass   |
      | strong       | ValidPass123!    | Pass   |
