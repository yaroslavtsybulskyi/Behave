import time

from behave import given, when, then
from features.Home.home import Home


@given(u'Navigate to login page')
def step_impl(context):
    context.home_page = Home(context.driver)
    context.home_page.click_on_login()
    time.sleep(2)


@when(u'I enter "{email}" and "{password}" into the field')
def step_impl(context, email, password):
    context.home_page.type_email(email)
    context.home_page.type_password(password)
    time.sleep(2)


@when(u'I click on login button')
def step_impl(context):
    context.home_page.click_log_in_button()
    time.sleep(2)


@then(u'I should be logged in')
def step_impl(context):
    context.home_page.check_if_log_in_successful()
    time.sleep(2)


@when(u'I enter invalid "{email}" and valid "{password}" into the field')
def step_impl(context, email, password):
    context.home_page.type_email(email)
    context.home_page.type_password(password)
    time.sleep(2)


@then(u'I should get warning message')
def step_impl(context):
    context.home_page.check_if_warning_is_shown()
    time.sleep(2)

