from time import sleep
import pytest
from .utils.fixtures import driver, login_driver
from .utils.allure_wrappers import take_screenshot

URL = "http://localhost:1667/"

def test_logout(login_driver):

    login_driver.get(URL)
    take_screenshot(login_driver, "logged_in")
    logout_link = login_driver.find_element_by_xpath('//a[@active-class="active"]')
    logout_link.click()
    sleep(1)
    take_screenshot(login_driver, "after_logout")
    signup_link = login_driver.find_element_by_xpath('//a[@href="#/register"]')
    assert "Sign up" in signup_link.text
    