from behave import given, when, then
import json
import time


@given('user is at rides page')
def step_given_user_is_at_ride_page(context):
    time.sleep(30)
    title = context.app.rides_page.get_page_title()
    assert "Rides" in title, f'Expected "Rides" to be in {title}, but found {title}'


@when('user access account page')
def step_when_taps_menu(context):
    context.app.rides_page.tap_main_menu()

