Feature: Menu functionality


  Scenario: Finding PC products
    Given I navigate to the main page
    When I press Desktops button
    And I select PC
    Then I should see message
    And I return to Desktops button
    And I select Mac


  Scenario: Finding Mac products
    Given I navigate to the main page
    When I press Desktops button
    And I select Mac
    Then I should see the product


  Scenario Outline: Test Menu
    Given click on menu <menu_name>
      Examples:
      |menu_name|
      | Desktops |
      | Laptops & Notebooks |
      | Components |
      | Tablets |
      | Software |
      | Phones & PDAs |
      | Cameras |
      | MP3 Players |

  @negative
  Scenario Outline: Check product availability
    Given I navigate to the main page
    When I press "<menu_item>" button
    And I select "<submenu>"
    Then I should see message
    Examples:
      | menu_item | submenu |
      | Desktops  | PC (0)  |
      | Components| Scanners (0) |
      | Components| Printers (0) |
      | Laptops & Notebooks | Windows (0)|
