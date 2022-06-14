"""
Test conduit app login
"""

import allure
import pytest
from .utils.fixtures import driver
from .utils.allure_wrappers import take_screenshot

URL = "http://localhost:1667/"

@pytest.mark.parametrize(
    "email, password, expected_message",
    [
        ("invalidmail", "Userpass1", "Email must be a valid email."),
        ("user32@hotmail.com", "Userpass1", "Invalid user credentials."),
    ]
)
def test_invalid_login(driver, email, password, expected_message):
    """
    Test invalid login
    """
    with allure.step(f"test login"):
        driver.get(URL)
        login_link = driver.find_element_by_xpath('//a[@href="#/login"]')
        login_link.click()
        take_screenshot(driver, "login_page")
        login_email_field = driver.find_element_by_xpath('//input[@placeholder="Email"]')
        login_password_field = driver.find_element_by_xpath('//input[@placeholder="Password"]')
        login_button = driver.find_element_by_xpath('//button[contains(text(), "Sign in")]')
        login_email_field.send_keys(email)
        login_password_field.send_keys(password)
        take_screenshot(driver, "login_page_after_fill")
        login_button.click()
        take_screenshot(driver, "after_login")
        # TODO create assert for error messages
        # <div class="swal-text" style="">Email must be a valid email.</div>
        error_message = driver.find_element_by_xpath('//div[@class="swal-text"]')
        assert error_message.text == expected_message