Feature: testing plugin hooks
  
  Scenario: Add a new controller device
    Given I have a controller device plugin
    When I activate it
    Then the device becomes available

  Scenario: Add support to administrate a controller device
    Given I have a controller device plugin
    When I activate it
    Then I can use it in the controller administration panel
