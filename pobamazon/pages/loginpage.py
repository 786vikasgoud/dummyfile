from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_button = (By.XPATH, "//a[@id='nav-link-accountList']")
        self.email_input_locator = (By.XPATH, "//input[@id='ap_email']")
        self.continue_button_locator = (By.XPATH, "//input[@id='continue']")
        self.password_input_locator = (By.XPATH, "//input[@type='password']")
        self.empty_password_input_locator = (By.XPATH,"//div[contains(text(),'Enter your password')]")
        self.sign_in_button_locator = (By.XPATH, "//input[@id='signInSubmit']")
        self.no_input_message_locator = (By.XPATH, "//div[contains(text(),'Enter your email or mobile phone number')]")
        self.error_message_locator = (By.XPATH, "//span[@class='a-list-item']")
        self.incorrect_password_message_locator = (By.XPATH, "//span[contains(text(),'Your password is incorrect')]")

    def sign_button_click(self):
        self.driver.find_element(*self.sign_button).click()

    def enter_username_and_continue(self, username):
        self.driver.find_element(*self.email_input_locator).send_keys(username)
        self.driver.find_element(*self.continue_button_locator).click()

    def enter_password_and_sign_in(self, password):
        self.driver.find_element(*self.password_input_locator).send_keys(password)
        self.driver.find_element(*self.sign_in_button_locator).click()

    def get_no_input_message(self):
        errorText = self.driver.find_element(*self.no_input_message_locator).text
        return errorText

    def get_error_message(self):
        errorText = self.driver.find_element(*self.error_message_locator).text
        return errorText

    def get_incorrect_password_message(self):
        errorText = self.driver.find_element(*self.incorrect_password_message_locator).text
        return errorText
    def get_empty_password_feild_message(self):
        return self.driver.find_element(*self.empty_password_input_locator).text
