import time

from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By


@given(u'I navigate to login page')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    # context.driver.get("https://tutorialsninja.com/demo/")

    my_account = context.driver.find_element(By.XPATH, "//span[text()='My Account']")
    my_account.click()

    login_button = context.driver.find_element(By.LINK_TEXT, "Login")
    login_button.click()
    time.sleep(3)


@when(u'I enter valid email and valid password into the text')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys('homerj@thesimpsons.com')
    context.driver.find_element(By.ID, "input-password").send_keys('Bart')


@when(u'I click login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@then(u'I should log in')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Edit your account information').is_displayed()
    time.sleep(2)


@when(u'I enter invalid "{email}" and valid "{password}" into the text field')
def step_impl(context, email, password):
    context.driver.find_element(By.ID, "input-email").send_keys(email)
    context.driver.find_element(By.ID, "input-password").send_keys(password)


@then(u'I should get warning')
def step_impl(context):
    message = context.driver.find_element(By.XPATH, '//div[contains(text(), "Warning: No match for E-Mail Address '
                                                    'and/or Password.")]')
    message.is_displayed()
    time.sleep(2)


