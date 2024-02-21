from behave import given, when, then
from appium import *


@given(u'User opens the app')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given User opens the app')


@when(u'User enter valid credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enter valid credentials')


@then(u'User verifies that main screen is shown')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User verifies that main screen is shown')


@when(u'User enters invalid credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters invalid credentials')


@then(u'User sees invalid credentials message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User sees invalid credentials message')