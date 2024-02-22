Feature: Login Screen
  As an end user
  I want to access the phone number screen
  So that I can input my phone number to login to the app

  Scenario Outline: User can successfully login
    Given user taps on get started button
    When user enters invalid <data>
    Then user verifies that error message Something went wrong, please try again is shown

    Examples:
    | data       |
    | ********** |
    | ########## |
    | ---------- |
