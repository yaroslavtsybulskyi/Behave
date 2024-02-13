Feature: Register functionality

  @positive
  Scenario: Register with credentials
    Given I navigate to the register page
    When I enter valid users data into the text field
    And I click on continue button
    Then I should see notification that account was created
    And I press Continue button
    And I am logged in to the account

  @negative
  Scenario: Register with invalid credentials
    Given I navigate to the register page
    When I enter valid users data into the text field and already used email
    And I click on continue button
    Then I should see notification that email is already used
