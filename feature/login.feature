Feature: Login to orangeHRM
  Scenario: Login to orangeHRM by using valid parameters
    Given Launch Chrome browser
    When open homepage
    And Enter "admin" and "admin123"
    And Click on login button
    Then User must successfully login to the dashboard page

#scenario outline is used when passing multiple parameters
  Scenario Outline: Login to orangeHRM by using valid parameters
    Given Launch Chrome browser
    When open homepage
    And Enter "<username>" and "<password>"
    And Click on login button
    Then User must successfully login to the dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |
