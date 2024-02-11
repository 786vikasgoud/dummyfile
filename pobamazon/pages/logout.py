import time

from selenium.webdriver.common.by import By


class logoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_button = (By.XPATH, "//a[@id='nav-link-accountList']")
        self.email_input_locator = (By.XPATH, "//input[@id='ap_email']")
        self.continue_button_locator = (By.XPATH, "//input[@id='continue']")
        self.password_input_locator = (By.XPATH, "//input[@type='password']")
        self.sign_in_button_locator = (By.XPATH, "//input[@id='signInSubmit']")
        self.menu_button = (By.XPATH, "//a[@id='nav-hamburger-menu']")
        self.signout = (By.XPATH,
                        "//body/div[@id='hmenu-container']/div[@id='hmenu-canvas']/div[@id='hmenu-content']/ul[1]/li[32]/a[1]")

    def account_singnin(self, username, password):
        self.driver.find_element(*self.sign_button).click()
        self.driver.find_element(*self.email_input_locator).send_keys(username)
        self.driver.find_element(*self.continue_button_locator).click()
        self.driver.find_element(*self.password_input_locator).send_keys(password)
        self.driver.find_element(*self.sign_in_button_locator).click()
        time.sleep(3)

    def accout_logout(self):
        self.driver.find_element(*self.menu_button).click()
        time.sleep(3)
        self.driver.find_element(*self.signout).click()
        time.sleep(3)
