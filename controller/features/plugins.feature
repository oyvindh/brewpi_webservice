Feature: testing plugin hooks
  
  Scenario: Add a new controller device
    Given There's a controller device model plugin available
    When I activate its model
    Then the model can be used

  Scenario: Add support to administrate a controller device
    Given There's a controller device admin plugin available
    When I activate its admin model
    Then the inline is loaded in the controller administration model
