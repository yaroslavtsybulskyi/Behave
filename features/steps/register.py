import time

from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By


@given(u'I navigate to the register page')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    # context.driver.get("https://tutorialsninja.com/demo/")

    my_account = context.driver.find_element(By.XPATH, "//span[text()='My Account']")
    my_account.click()

    login_button = context.driver.find_element(By.LINK_TEXT, "Register")
    login_button.click()
    time.sleep(3)


@when(u'I enter valid users data into the text field')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys('Homer')
    context.driver.find_element(By.ID, "input-lastname").send_keys('Simpson')
    context.driver.find_element(By.ID, "input-email").send_keys('homerjxz@thesimpsons.com')
    context.driver.find_element(By.ID, "input-telephone").send_keys('911')
    context.driver.find_element(By.ID, "input-password").send_keys('Bart')
    context.driver.find_element(By.ID, "input-confirm").send_keys('Bart')

    time.sleep(2)


@when(u'I click on continue button')
def step_impl(context):
    checkbox = context.driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/input[1]')
    checkbox.click()
    time.sleep(2)
    btn = context.driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/input[2]')
    btn.click()

    time.sleep(3)


@then(u'I should see notification that account was created')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//h1[contains(text(), "Your Account Has Been Created")]').is_displayed()
    time.sleep(3)


@then(u'I press Continue button')
def step_impl(context):
    btn = context.driver.find_element(By.XPATH, '//*[@id="content"]/div/div/a')
    btn.click()
    time.sleep(2)


@then(u'I am logged in to the account')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="content"]/h2[1]').is_displayed()
    time.sleep(2)


@when(u'I enter valid users data into the text field and already used email')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys('Homer')
    context.driver.find_element(By.ID, "input-lastname").send_keys('Simpson')
    context.driver.find_element(By.ID, "input-email").send_keys('homiey@thesimpsons.com')
    context.driver.find_element(By.ID, "input-telephone").send_keys('911')
    context.driver.find_element(By.ID, "input-password").send_keys('Bart')
    context.driver.find_element(By.ID, "input-confirm").send_keys('Bart')

    time.sleep(4)


@then(u'I should see notification that email is already used')
def step_impl(context):
    message = context.driver.find_element(By.XPATH, '//div[contains(text(), "Warning: E-Mail Address is already '
                                                    'registered!")]')
    message.is_displayed()
    time.sleep(3)
