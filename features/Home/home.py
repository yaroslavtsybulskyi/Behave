from selenium.webdriver.common.by import By


class Home:
    def __init__(self, driver):
        self.driver = driver

    my_account_option_xpath = "//span[text()='My Account']"
    email_id = "input-email"
    my_password = "input-password"
    log_in_check = "Edit your account information"
    login_button = "//input[@value='Login']"

    def click_on_login(self):
        self.driver.find_element(By.XPATH, self.my_account_option_xpath).click()

        login_button = self.driver.find_element(By.LINK_TEXT, "Login")
        login_button.click()

    def type_email(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def type_password(self, password):
        self.driver.find_element(By.ID, self.my_password).send_keys(password)

    def click_log_in_button(self):
        btn = self.driver.find_element(By.XPATH, self.login_button)
        btn.click()

    def check_if_log_in_successful(self):
        self.driver.find_element(By.LINK_TEXT, self.log_in_check).is_displayed()

    def check_if_warning_is_shown(self):
        message = self.driver.find_element(By.XPATH, '//div[contains(text(), "Warning: No match for E-Mail Address '
                                                     'and/or Password.")]')
        message.is_displayed()
