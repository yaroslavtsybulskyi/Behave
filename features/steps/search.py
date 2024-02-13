import time

from behave import given, when, then
from selenium.webdriver.common.by import By


@given(u'I go to home page')
def step_impl(context):
    pass


@when(u'I enter valid product into search box')
def step_impl(context):
    search_box = context.driver.find_element(By.NAME, 'search')
    search_box.send_keys('HP')
    time.sleep(2)


@when(u'I click search box button')
def step_impl(context):
    search_button = context.driver.find_element(By.XPATH, '//*[@id="search"]/span/button')
    search_button.click()
    time.sleep(2)


@then(u'The valid product should be displayed')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()


@when(u'I enter invalid product into search box')
def step_impl(context):
    search_box = context.driver.find_element(By.NAME, 'search')
    search_box.send_keys('Ball')
    time.sleep(2)


@then(u'Warning message is displayed')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."
    actual_text = context.driver.find_element(By.XPATH, '//*[@id="content"]/p[2]')
    assert expected_text == actual_text.text
