Feature: testing basic features

  Scenario: representing a controller
    Given we have a controller
    When I represent it as a string
    Then it shows a nice string
