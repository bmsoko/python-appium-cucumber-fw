from behave import given, when, then


@given('user taps on get started button')
def user_taps_get_started_button(context):
    context.app.main_page.tap_getstared()


@when('user enters invalid {data}')
def step_when_user_enters_invalid_pn(context, data):
    context.app.phone_number_page.input_phone_number(data)


@then('user verifies that error message {error_message} is shown')
def user_error_should_be_shown(context, error_message: str):
    error = context.app.main_page.get_snack_bar_text()
    assert error_message in error, f'Expected {error_message} to be in {error}'