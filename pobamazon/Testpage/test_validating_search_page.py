import time

import pytest

from pobamazon.conftest.diversetup import driver_setup
from pobamazon.error_content.Errors import Content
from pobamazon.pages.searchpage import searchPage


@pytest.mark.parametrize("username, password,productName,expected1,expected2,expected3,expected4",
                         [("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "samsung s22 ultra", Content.tit,
                           Content.product_search_title, Content.product_search_title, Content.payment_page_title),
                          ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "samsung s22 ultra", Content.tit,
                           Content.tit, Content.product_search_title, Content.payment_page_title)
                          ])
# @pytest.mark.xfail
def test_validating_search_details_(driver_setup, username, password, productName, expected1, expected2, expected3,
                                    expected4):
    driver = driver_setup
    login = searchPage(driver)
    driver.get("https://www.amazon.in/")
    login.account_singnin(username, password)
    title = driver.title
    assert expected1 == title
    time.sleep(3)
    login.search_product(productName)
    title = driver.title
    assert expected2 == title
    login.search_product_link_click()
    time.sleep(4)
    title = driver.title
    assert expected3 == title
    time.sleep(3)
    login.buy_now_button_click()
    title = driver.title
    assert expected4 == title


@pytest.mark.parametrize("username, password,productName,expected",
                         [
                             ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "", Content.tit),
                             ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "kbfefkjwf",
                              Content.product_unexist_alpha),
                             ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "9951962196",
                              Content.product_unexist_numaric),
                             ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "abcdef9951962196",
                              Content.product_unexist_alpha_numaric),
                             ("shivaiahgarivikasgoud@gmail.com", "Vikas786@", "hdjdjdjd",
                              Content.product_unexist_alpha_numaric)])
# @pytest.mark.xfail
def test_valdating_product_details_(driver_setup, username, password, productName, expected):
    driver = driver_setup
    login = searchPage(driver)
    driver.get("https://www.amazon.in/")
    login.account_singnin(username, password)
    login.search_product(productName)
    time.sleep(3)
    title = driver.title
    print(title)
    assert expected == title
