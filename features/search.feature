Feature: Search functionality

  @positive
  Scenario: Search for valid product
    Given I go to home page
    When I enter valid product into search box
    And I click search box button
    Then The valid product should be displayed

  @negative
  Scenario: Search for invalid product
    Given I go to home page
    When I enter invalid product into search box
    And I click search box button
    Then Warning message is displayed

  @negative
  Scenario: Searching without entering product name
    Given I go to home page
    When I click search box button
    Then Warning message is displayed
