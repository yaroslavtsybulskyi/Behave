import time

from behave import given, when, then, step
from selenium.webdriver.common.by import By


@step(u'I press "{menu_name}" button')
def step_impl(context, menu_name):
    desktop = context.driver.find_element(By.XPATH, f'//a[text()="{menu_name}"]')
    desktop.click()
    time.sleep(2)


@when(u'I select PC')
def step_impl(context):
    pc_button = context.driver.find_element(By.XPATH, "//a[text()='PC (0)']")
    pc_button.click()
    time.sleep(2)


@then(u'I should see message')
def step_impl(context):
    expected_text = "There are no products to list in this category."
    assert context.driver.find_element(By.XPATH, '//div[@id="content"]/p').text == expected_text


@then(u'I return to Desktops button')
def step_impl(context):
    desktop = context.driver.find_element(By.XPATH, "//a[text()='Desktops']")
    desktop.click()
    time.sleep(2)


@then(u'I select Mac')
def step_impl(context):
    pc_button = context.driver.find_element(By.XPATH, "//a[text()='Mac (1)']")
    pc_button.click()
    time.sleep(2)


@step(u'click on menu {menu_name}')
def step_impl(context, menu_name):
    desktop = context.driver.find_element(By.XPATH, f'//a[text()="{menu_name}"]')
    desktop.click()
    time.sleep(2)


@given(u'I navigate to the main page')
def step_impl(context):
    pass


@when(u'I press Desktops button')
def step_impl(context):
    desktop = context.driver.find_element(By.XPATH, "//a[text()='Desktops']")
    desktop.click()

    time.sleep(2)


@when(u'I select Mac')
def step_impl(context):
    pc_button = context.driver.find_element(By.XPATH, "//a[text()='Mac (1)']")
    pc_button.click()
    time.sleep(2)


@then(u'I should see the product')
def step_impl(context):
    mac = context.driver.find_element(By.XPATH, "//a[text()='iMac']")
    assert mac.is_displayed()


@step(u'I select "{submenu}"')
def step_impl(context, submenu):
    submenu = context.driver.find_element(By.LINK_TEXT, f"{submenu}")
    submenu.click()
