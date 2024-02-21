Feature: Login
  Scenario: User can successfully login
    Given User opens the app
    When User enter valid credentials
    Then User verifies that main screen is shown


  Scenario: User can not login to the app
    Given User opens the app
    When User enters invalid credentials
    Then User sees invalid credentials message