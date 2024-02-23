from behave import given, when, then
import json
import time


@when('user opens profile')
def step_when_user_enters_invalid_pn(context):
    context.app.account_page.tap_profile()

