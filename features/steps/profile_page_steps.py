from behave import given, when, then
import random
import string


@when('user attempts to update name with text: {data_update}')
def step_when_user_enters_invalid_pn(context, data_update):
    last_name = data_update.join(random.choices(string.ascii_lowercase, k=10))
    first_name = data_update.join(random.choices(string.ascii_lowercase, k=10))
    context.last_name_update = last_name
    context.first_name_update = first_name
    print(context.last_name_update)
    context.app.profile_page.input_name_and_last(first_name, last_name)
    context.app.main_page.tap_done()


@then('user sees {message} message')
def step_then_user_sees_message_profile(context, message):
    success_message = context.app.main_page.get_snack_bar_text()
    assert message in success_message, f'Expected {success_message} to be in {message}'


@then('user sees that first and last name are updated')
def step_then_user_sees_message_profile(context):
    last_name_text = context.app.profile_page.get_last_name_text()
    first_name_text = context.app.profile_page.get_first_name_text()
    ln = context.last_name_update
    fn = context.first_name_update
    assert ln in last_name_text, f'Expected {ln} to be in {last_name_text}'
    assert fn in first_name_text, f'Expected {fn} to be in {first_name_text}'