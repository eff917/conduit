"""
Test conduit app signup
"""

import allure
import pytest
from .utils.fixtures import driver
from .utils.allure_wrappers import take_screenshot

URL = "http://localhost:1667/"

def test_invalid_login(driver):
    """
    Sugnup test
    """
    with allure.step(f"test login"):
        try:
            driver.get(URL)
            signup_link = driver.find_element_by_xpath('//a[@href="#/register"]')
            signup_link.click()
            take_screenshot(driver, "signup_page")
            signup_username_field = driver.find_element_by_xpath('//input[@placeholder="Username"]')
            signup_email_field = driver.find_element_by_xpath('//input[@placeholder="Email"]')
            signup_password_field = driver.find_element_by_xpath('//input[@placeholder="Password"]')
            signup_button = driver.find_element_by_xpath('//button[contains(text(), "Sign up")]')

            signup_username_field.send_keys("TestUser32")
            signup_email_field.send_keys("user32@hotmail.com")
            signup_password_field.send_keys("Userpass1")
            take_screenshot(driver, "signup_page_after_fill")
            signup_button.click()
            take_screenshot(driver, "after_signup")
            # <div class="swal-text" style="">Email must be a valid email.</div>

        except Exception as ex:  # pylint: disable=W0703
            print(ex)
    return True
