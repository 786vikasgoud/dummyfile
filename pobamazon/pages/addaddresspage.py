import time

from selenium.webdriver.common.by import By


class addAddressPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_button = (By.XPATH, "//a[@id='nav-link-accountList']")
        self.email_input_locator = (By.XPATH, "//input[@id='ap_email']")
        self.continue_button_locator = (By.XPATH, "//input[@id='continue']")
        self.password_input_locator = (By.XPATH, "//input[@type='password']")
        self.sign_in_button_locator = (By.XPATH, "//input[@id='signInSubmit']")
        self.add_address_button_locator = (By.XPATH, "//a[@id='nav-global-location-popover-link']")
        self.add_address_locator = (By.XPATH, "//a[contains(text(),'Add an address or pick-up point')]")
        self.add_addres = (By.XPATH, "//div[@class='a-box first-desktop-address-tile']")
        self.name_locator = (By.XPATH, "//input[@id='address-ui-widgets-enterAddressFullName']")
        self.mobile_number_locator = (By.XPATH, "//input[@id='address-ui-widgets-enterAddressPhoneNumber']")
        self.pincode_locator = (By.XPATH, "//input[@id='address-ui-widgets-enterAddressPostalCode']")
        self.house_number_locator = (By.XPATH, "//input[@id='address-ui-widgets-enterAddressLine1']")
        self.area_street_locator = (By.XPATH, "//input[@id='address-ui-widgets-enterAddressLine2']")
        self.landmark_locator = (By.XPATH, "//input[@id='address-ui-widgets-landmark']")
        self.add_address_button = (By.XPATH,
                                   "//body/div[@id='a-page']/div[1]/div[1]/div[2]/form[1]/span[1]/div[1]/span[3]/span[1]/span[1]/input[1]")
        self.empty_error_Text = (By.XPATH, "//div[contains(text(),'Please enter a name.')]")
        self.invalid_number_errorText = (By.XPATH,
                                         "//body/div[@id='a-page']/div[1]/div[1]/div[2]/form[1]/span[1]/div[1]/div[8]/div[1]/div[6]/div[3]/div[1]/div[1]/div[1]/div[1]")
        self.empty_number_errorText = (
        By.XPATH, "//div[contains(text(),'Please enter a phone number so we can call if ther')]")
        self.invalid_pincode = (By.XPATH,
                                "//body/div[@id='a-page']/div[1]/div[1]/div[2]/form[1]/span[1]/div[1]/div[7]/div[1]/div[15]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]")
        self.invalid_HouseNo = (By.XPATH,
                                "//body/div[@id='a-page']/div[1]/div[1]/div[2]/form[1]/span[1]/div[1]/div[7]/div[1]/div[10]/div[2]/div[1]")
        self.invalid_area = (By.XPATH,
                             "//body/div[@id='a-page']/div[1]/div[1]/div[2]/form[1]/span[1]/div[1]/div[8]/div[1]/div[12]/div[2]/div[1]/div[1]/div[1]/div[1]")

    def sign_button_click(self):
        self.driver.find_element(*self.sign_button).click()

    def enter_username_and_continue(self, username):
        self.driver.find_element(*self.email_input_locator).send_keys(username)
        self.driver.find_element(*self.continue_button_locator).click()

    def enter_password_and_sign_in(self, password):
        self.driver.find_element(*self.password_input_locator).send_keys(password)
        self.driver.find_element(*self.sign_in_button_locator).click()

    def add_address(self):
        self.driver.find_element(*self.add_address_button_locator).click()
        self.driver.implicitly_wait(5)
        time.sleep(5)
        self.driver.find_element(*self.add_address_locator).click()
        self.driver.implicitly_wait(5)
        time.sleep(5)
        self.driver.find_element(*self.add_addres).click()

    def enter_fullname(self, name):
        self.driver.find_element(*self.name_locator).send_keys(name)

    def enter_mobilenumber(self, number):
        self.driver.find_element(*self.mobile_number_locator).send_keys(number)

    def enter_pincode(self, pincode):
        self.driver.find_element(*self.pincode_locator).send_keys(pincode)

    def enter_housenumber(self, HNo):
        self.driver.find_element(*self.house_number_locator).send_keys(HNo)

    def enter_area_street(self, area):
        self.driver.find_element(*self.area_street_locator).send_keys(area)

    def enter_land_mark(self, landmark):
        self.driver.find_element(*self.landmark_locator).send_keys(landmark)

    def click_add_address_button(self):
        self.driver.find_element(*self.add_address_button).click()

    def empty_name_error(self):
        return self.driver.find_element(*self.empty_error_Text).text

    def enter_invalid_number(self):
        return self.driver.find_element(*self.invalid_number_errorText).text

    def empty_number(self):
        return self.driver.find_element(*self.empty_number_errorText).text

    def enter_invalid_pincode(self):
        return self.driver.find_element(*self.invalid_pincode).text

    def empty_house_no(self):
        return self.driver.find_element(*self.invalid_HouseNo).text

    def empty_area_feild(self):
        return self.driver.find_element(*self.invalid_area).text
