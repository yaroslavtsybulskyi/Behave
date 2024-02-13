Feature: Login functionality

  @positive
  Scenario: Login with valid credentials
    Given I navigate to login page
    When I enter valid email and valid password into the text
    And I click login button
    Then I should log in

  @negative
  Scenario Outline: Login with invalid email and valid password
    Given I navigate to login page
    When I enter invalid "<email>" and valid "<password>" into the text field
    And I click login button
    Then I should get warning

    Examples:
      | email                | password |
      |hoerj@thesimpsons.com | Bart     |
      |mrge@thesimpsons.com  | Bart     |