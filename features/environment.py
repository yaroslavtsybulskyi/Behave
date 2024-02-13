from selenium import webdriver
from features.utilities import ConfigReader


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration('basic info', 'browser')
    if browser_name == 'chrome':
        context.driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        context.driver = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration('basic info', 'url'))


def after_scenario(context, driver):
    context.driver.quit()
