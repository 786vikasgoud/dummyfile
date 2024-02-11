import time

import pytest

from pobamazon.conftest.diversetup import driver_setup
from pobamazon.error_content.Errors import Content
from selenium.webdriver.common.by import By
from pobamazon.pages.logout import logoutPage


@pytest.mark.parametrize("username, password, expected", [
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", Content.sucess_signout),
    ("SHIVAIAHGARIVIKASGOUD@GMAIL.COM", "Vikas786@", Content.tit)
])
def test_validating_logout_details(driver_setup, username, password, expected):
    driver = driver_setup
    driver.get("https://www.amazon.in/")
    logout = logoutPage(driver)
    logout.account_singnin(username, password)
    logout.accout_logout()
    title = driver.title
    assert title == expected




@pytest.mark.parametrize("username, password, expected", [
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", Content.sucess_signout),
    ("SHIVAIAHGARIVIKASGOUD@GMAIL.COM", "Vikas786@", Content.tit)
])
def test_validating_relogin_details(driver_setup, username, password, expected):
    driver = driver_setup
    driver.get("https://www.amazon.in/")
    logout = logoutPage(driver)
    logout.account_singnin(username, password)
    driver = driver_setup
    driver.get("https://www.amazon.in/")
    title = driver.title
    assert title == expected


@pytest.mark.parametrize("expected", [Content.sucess_signout, Content.tit])
def test_validating_logout_details(driver_setup, expected):
    driver = driver_setup
    driver.get("https://www.amazon.in/")
    time.sleep(3)
    title = driver.title
    assert title == expected
