import time

import pytest
from pobamazon.error_content.Errors import Content
from pobamazon.conftest.diversetup import driver_setup
from pobamazon.pages.addaddresspage import addAddressPage


def myExcuation(driver, add_address, username, password, name, mobile_number, pincode, HNO, area, landmark):
    driver.get("https://www.amazon.in/")
    add_address.sign_button_click()
    add_address.enter_username_and_continue(username)
    add_address.enter_password_and_sign_in(password)
    # time.sleep(55)
    add_address.add_address()
    driver.implicitly_wait(5)
    add_address.enter_fullname(name)
    driver.implicitly_wait(5)
    add_address.enter_mobilenumber(mobile_number)
    driver.implicitly_wait(5)
    add_address.enter_pincode(pincode)
    time.sleep(2)
    add_address.enter_housenumber(HNO)
    add_address.enter_area_street(area)
    driver.implicitly_wait(5)
    time.sleep(2)
    add_address.enter_land_mark(landmark)
    driver.implicitly_wait(5)
    time.sleep(2)
    add_address.click_add_address_button()


@pytest.mark.parametrize("username, password,name,mobile_number,pincode,HNO,area,landmark,expected", [
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "8647876539", "502316", "2-1-107", "kowdipally",
     "near to daily market", Content.update_address_sucess)])
def test_add_valid_address_details(driver_setup, username, password, name, mobile_number, pincode, HNO, area, landmark,
                                   expected):
    driver = driver_setup
    add_address = addAddressPage(driver)
    myExcuation(driver, add_address, username, password, name, mobile_number, pincode, HNO, area, landmark)
    time.sleep(3)
    title = driver.title

    assert title == expected


@pytest.mark.parametrize("username, password,name,mobile_number,pincode,HNO,area,landmark,expected", [
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "995", "502316", "2-1-107", "kowdipally",
     "near daily market", Content.address_number_errorText),
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "83838hsiut", "502316", "2-1-107", "kowdipally",
     "near daily market", Content.address_number_errorText),
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "hnafrhsiut", "502316", "2-1-107", "kowdipally",
     "near daily market", Content.address_number_errorText)])

def test_validating_mobile_number_details(driver_setup, username, password, name, mobile_number, pincode, HNO, area,
                                          landmark, expected):
    driver = driver_setup
    add_address = addAddressPage(driver)
    myExcuation(driver, add_address, username, password, name, mobile_number, pincode, HNO, area, landmark)
    errorText = add_address.enter_invalid_number()
    assert errorText == expected


@pytest.mark.parametrize("username, password,name,mobile_number,pincode,HNO,area,landmark,expected", [
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "", "502316", "2-1-107", "kowdipally",
     "near daily market", Content.address_empty_number_errorText)])

def test_validating_empty_mobile_number_details(driver_setup, username, password, name, mobile_number, pincode, HNO,
                                                area,
                                                landmark, expected):
    driver = driver_setup
    add_address = addAddressPage(driver)
    myExcuation(driver, add_address, username, password, name, mobile_number, pincode, HNO, area, landmark)
    errorText = add_address.empty_number()
    assert errorText == expected


@pytest.mark.parametrize("username, password,name,mobile_number,pincode,HNO,area,landmark,expected", [
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "9951962196", " ", "2-1-107", "kowdipally",
     "near daily market", Content.address_empty_pincode_errorText),
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "9951962196", "50231", "2-1-107", "kowdipally",
     "near daily market", Content.address_empty_pincode_errorText),
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "9951962196", "teyebd", "2-1-107", "kowdipally",
     "near daily market", Content.address_empty_pincode_errorText),
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "9951962196", "775756", "2-1-107", "kowdipally",
     "near daily market", Content.address_empty_pincode_errorText),
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "9951962196", "858586866", "2-1-107", "kowdipally",
     "near daily market", Content.address_empty_pincode_errorText)
])

def test_validating_pincode_details(driver_setup, username, password, name, mobile_number, pincode, HNO, area, landmark,
                                    expected):
    driver = driver_setup
    add_address = addAddressPage(driver)
    myExcuation(driver, add_address, username, password, name, mobile_number, pincode, HNO, area, landmark)
    errorText = add_address.enter_invalid_pincode()
    assert errorText == expected


@pytest.mark.parametrize("username, password,name,mobile_number,pincode,HNO,area,landmark,expected", [
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "9951962196", "502316", " ", "kowdipally",
     "near daily market", Content.address_Hno_errorText)])

def test_validating_house_No_details(driver_setup, username, password, name, mobile_number, pincode, HNO, area,
                                     landmark, expected):
    driver = driver_setup
    add_address = addAddressPage(driver)
    myExcuation(driver, add_address, username, password, name, mobile_number, pincode, HNO, area, landmark)
    errorText = add_address.empty_house_no()
    assert errorText == expected


@pytest.mark.parametrize("username, password,name,mobile_number,pincode,HNO,area,landmark,expected", [
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "9951962196", "502316", "2-1-107", "",
     "near daily market", Content.address_area_errorText),
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "9951962196", "502316", "2-1-107", "nbsdfjvfjvjhd",
     "near daily market", Content.address_area_errorText),
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "Vikas", "9951962196", "502316", "2-1-107", "758696546jvfjvjhd",
     "near daily market", Content.address_area_errorText)])

def test_validating_area_details(driver_setup, username, password, name, mobile_number, pincode, HNO, area,
                                 landmark, expected):
    driver = driver_setup
    add_address = addAddressPage(driver)
    myExcuation(driver, add_address, username, password, name, mobile_number, pincode, HNO, area, landmark)
    errorText = add_address.empty_area_feild()
    assert errorText == expected
