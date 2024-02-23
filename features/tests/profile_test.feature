Feature: Account
  As an end user that had already created my account
  I would like to access my account profile
  So that I can update it.

  # Next scenario is to be run with "appium:noReset": "true" in environment.py test
  # First you'll need to login with phone number and place the screen at Rides
  Scenario: Edit My Profile
    Given user is at rides page
    When user access account page
    And user opens profile
    And user attempts to update name with text: update
    Then user sees Profile Updated successfully message
    When user opens profile
    Then user sees that first and last name are updated
