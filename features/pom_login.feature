Feature: Login functionality with POM

  @positive
  Scenario Outline: Login with valid credentials using POM
    Given Navigate to login page
    When I enter "<email>" and "<password>" into the field
    And I click on login button
    Then I should be logged in
    Examples:
      | email | password |
      | homerj@thesimpsons.com | Bart |


    @negative
    Scenario Outline: Login with invalid credentials using POM
    Given Navigate to login page
    When I enter invalid "<email>" and valid "<password>" into the field
    And I click on login button
    Then I should get warning message
    Examples:
      | email | password |
      | horj@thesimpsons.com   | Bart |
      | horwj@thesimpsons.com  | Bart |
      | hor2wj@thesimpsons.com | Bart |