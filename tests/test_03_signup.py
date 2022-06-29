"""
Test conduit app signup
"""

from time import sleep
import allure
import pytest
from .utils.fixtures import driver
from .utils.allure_wrappers import take_screenshot

URL = "http://localhost:1667/"

@pytest.mark.parametrize(
    "username, email, password, expected_message",
    [
        ("invalidmail", "invalidmail", "Userpass1", "Email must be a valid email."),
        ("", "empty@username.com", "Userpass1", "Username field required."),
        ("emptymail", "", "Userpass1", "Email field required."),
        ("emptypw", "user32@example.com", "", "Password field required."),
        ("", "", "", "Username field required.")
    ],
    ids = [
        "Invalid email format",
        "Empty username",
        "Empty email",
        "Empty password",
        "All fields empty"
    ]
)
def test_invalid_signup(driver, username, email, password, expected_message):
    """
    Signup test
    """
    with allure.step("test signup"):
        driver.get(URL)
        signup_link = driver.find_element_by_xpath('//a[@href="#/register"]')
        signup_link.click()
        take_screenshot(driver, "signup_page")
        signup_username_field = driver.find_element_by_xpath('//input[@placeholder="Username"]')
        signup_email_field = driver.find_element_by_xpath('//input[@placeholder="Email"]')
        signup_password_field = driver.find_element_by_xpath('//input[@placeholder="Password"]')
        signup_button = driver.find_element_by_xpath('//button[contains(text(), "Sign up")]')

        signup_username_field.send_keys(username)
        signup_email_field.send_keys(email)
        signup_password_field.send_keys(password)
        take_screenshot(driver, "signup_page_after_fill")
        signup_button.click()
        sleep(1)
        take_screenshot(driver, "after_signup")
        error_message = driver.find_element_by_xpath('//div[@class="swal-text"]')
        assert error_message.text == expected_message

@pytest.mark.skip()
def test_valid_signup(driver):
    assert True