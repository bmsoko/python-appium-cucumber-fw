from behave import given, when, then
import json
import time


@when('user enters invalid {data} as phone number')
def step_when_user_enters_invalid_pn(context, data):
    context.app.phone_number_page.input_phone_number(data)


@when('user enters a valid phone number')
def step_when_user_enters_valid_ph(context):
    f = open('/Users/brunosoko/Documents/dev/python-appium-cucumber-fw/data/data.json')
    data = json.load(f)
    context.app.phone_number_page.input_phone_number(data['valid_user']['phone_number'])
    context.app.phone_number_page.tap_continue()
    time.sleep(50)

# @then('user verifies that error message {error_message} is shown')
# def user_error_should_be_shown(context, error_message: str):
#     error = context.app.main_page.get_snack_bar_text()
#     assert error_message in error, f'Expected {error_message} to be in {error}'
