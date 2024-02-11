import time

import pytest
from pobamazon.error_content.Errors import Content
from pobamazon.pages.loginpage import LoginPage
from pobamazon.conftest.diversetup import driver_setup


def myExcuation(driver, login_page, username):
    driver.get("https://www.amazon.in/")
    login_page.sign_button_click()
    login_page.enter_username_and_continue(username)






@pytest.mark.parametrize("username, password, expected", [
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", Content.tit),
    ("SHIVAIAHGARIVIKASGOUD@GMAIL.COM", "Vikas786@", Content.tit),
    ("SHIVAIAHgariVIKASgoud@GMAIL.COM", "Vikas786@", Content.tit),
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", Content.email_errorText)])
# @pytest.mark.xfail
def test_login_details(driver_setup, username, password, expected):
    driver = driver_setup
    login_page = LoginPage(driver)
    myExcuation(driver, login_page, username)
    login_page.enter_password_and_sign_in(password)
    title = driver.title
    assert title == expected


@pytest.mark.parametrize("username,expected", [
    ("shivaiahgarivikasgoud.com", Content.email_errorText),
    ("shivai.org.in", Content.email_errorText),
    ("@.com", Content.email_errorText),
    ("shiv94498469jbkbffwhf.com", Content.email_errorText),
    ("shivaiahgarivikasgoud.com", Content.noInput_errorText)])
# @pytest.mark.xfail
def test_email_invalid_login_details(driver_setup, username, expected):
    driver = driver_setup
    login_page = LoginPage(driver)
    myExcuation(driver, login_page, username)
    error_message = login_page.get_error_message()
    assert error_message == expected


@pytest.mark.parametrize("username,expected", [
    ("8348", Content.mobile_errorText),
    ("8348897565", Content.mobile_errorText),
    ("834784554764839", Content.mobile_errorText),
    ("8348897565", Content.email_errorText)
])
# @pytest.mark.xfail
def test_invalid_mobile_number_login_details(driver_setup, username, expected):
    driver = driver_setup
    login_page = LoginPage(driver)
    myExcuation(driver, login_page, username)
    error_message = login_page.get_error_message()
    assert error_message == expected


@pytest.mark.parametrize("username,expected", [
    ("", Content.noInput_errorText),
    ("     ",Content.noInput_errorText),
    ("     ",Content.email_errorText)])
# @pytest.mark.xfail
def test_empty_feild_login_details(driver_setup, username, expected):
    driver = driver_setup
    login_page = LoginPage(driver)
    myExcuation(driver, login_page, username)
    error_message = login_page.get_no_input_message()
    assert error_message == expected


@pytest.mark.parametrize("username, password,function_name,expected", [
    ("shivaiahgarivikasgoud@gmail.com", "jhdjhdjh", "get_incorrect_password_message", Content.nopassword_errorText),
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786", "get_incorrect_password_message", Content.nopassword_errorText),
    ("shivaiahgarivikasgoud@gmail.com", "", "get_empty_password_feild_message", Content.enter_password_error_text),
    ("shivaiahgarivikasgoud@gmail.com", "Vikas786", "get_incorrect_password_message", Content.email_errorText)])
# @pytest.mark.xfail
def test_validating_invalid_password(driver_setup, username, password, function_name, expected):
    driver = driver_setup
    login_page = LoginPage(driver)
    myExcuation(driver, login_page, username)
    login_page.enter_password_and_sign_in(password)
    myFunction = getattr(login_page, function_name)
    error_message = myFunction()
    assert error_message == expected


