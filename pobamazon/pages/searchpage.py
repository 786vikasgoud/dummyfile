import time

from selenium.webdriver.common.by import By


class searchPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_button = (By.XPATH, "//a[@id='nav-link-accountList']")
        self.email_input_locator = (By.XPATH, "//input[@id='ap_email']")
        self.continue_button_locator = (By.XPATH, "//input[@id='continue']")
        self.password_input_locator = (By.XPATH, "//input[@type='password']")
        self.sign_in_button_locator = (By.XPATH, "//input[@id='signInSubmit']")
        self.search_locator = (By.XPATH, "//input[@id='twotabsearchtextbox']")
        self.search_button_locator = (By.XPATH, "//input[@id='nav-search-submit-button']")
        self.search_product_link = (
            By.XPATH,
            "//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]/a[1]/span[1]")
        self.buy_now_button = (By.XPATH, "//input[@id='buy-now-button']")

    def account_singnin(self, username, password):
        self.driver.find_element(*self.sign_button).click()
        self.driver.find_element(*self.email_input_locator).send_keys(username)
        self.driver.find_element(*self.continue_button_locator).click()
        self.driver.find_element(*self.password_input_locator).send_keys(password)
        self.driver.find_element(*self.sign_in_button_locator).click()

    def search_product(self, product):
        self.driver.find_element(*self.search_locator).send_keys(product)
        self.driver.find_element(*self.search_button_locator).click()
        time.sleep(4)

    def search_product_link_click(self):
        self.driver.find_element(*self.search_product_link).click()

    def buy_now_button_click(self):
        window_handles = self.driver.window_handles
        new_window_handle = window_handles[1]
        self.driver.switch_to.window(new_window_handle)
        time.sleep(4)
        self.driver.find_element(*self.buy_now_button).click()
