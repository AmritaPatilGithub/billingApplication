Feature: Orange HRM logo
  Scenario: Logo present on the orangeHRM home page
    Given Launch Chrome browser
    When Open orange HRM homepage
    Then Verify that the logo present on the page
    And Close the browser