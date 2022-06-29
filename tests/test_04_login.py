"""
Test conduit app login
"""

from time import sleep
import allure
import pytest
from .utils.fixtures import create_user, driver
from .utils.allure_wrappers import take_screenshot
from .utils.constants import URL


@pytest.mark.parametrize(
    "email, password, expected_message",
    [
        ("", "", "Email field required."),
        ("", "asdf", "Email field required."),
        ("testuser1@example.com", "", "Password field required."),
        ("testuser1@example.com", "asdf", "Invalid user credentials."),
        ("invalidmail", "Userpass1", "Email must be a valid email."),
        ("user32@hotmail.com", "Userpass1", "Invalid user credentials."),
    ],
    ids=[
        "Empty fields",
        "Empty email",
        "Empty password",
        "Invalid password",
        "Invalid email format",
        "Not registered email",
    ],
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
        login_email_field = driver.find_element_by_xpath(
            '//input[@placeholder="Email"]'
        )
        login_password_field = driver.find_element_by_xpath(
            '//input[@placeholder="Password"]'
        )
        login_button = driver.find_element_by_xpath(
            '//button[contains(text(), "Sign in")]'
        )
        login_email_field.send_keys(email)
        login_password_field.send_keys(password)
        take_screenshot(driver, "login_page_after_fill")
        login_button.click()
        # sleep one second to wait for animation to end
        sleep(1)
        take_screenshot(driver, "after_login")
        error_message = driver.find_element_by_xpath('//div[@class="swal-text"]')
        assert error_message.text == expected_message


@pytest.mark.parametrize(
    "email, password, expected_element, expected_username",
    [
        (
            "testuser1@mailinator.com",
            "TestUserPass1",
            '//a[@href="#/@testuser1/"]',
            "testuser1",
        ),
    ],
)
def test_valid_login(
    driver, create_user, email, password, expected_element, expected_username
):
    """
    Test valid login
    """
    with allure.step(f"test login"):
        driver.get(URL)
        login_link = driver.find_element_by_xpath('//a[@href="#/login"]')
        login_link.click()
        sleep(1)
        take_screenshot(driver, "login_page")
        login_email_field = driver.find_element_by_xpath(
            '//input[@placeholder="Email"]'
        )
        login_password_field = driver.find_element_by_xpath(
            '//input[@placeholder="Password"]'
        )
        login_button = driver.find_element_by_xpath(
            '//button[contains(text(), "Sign in")]'
        )
        login_email_field.send_keys(email)
        login_password_field.send_keys(password)
        take_screenshot(driver, "login_page_after_fill")
        login_button.click()
        # sleep one second to wait for animation to end
        sleep(1)
        take_screenshot(driver, "after_login")
        profile_link = driver.find_element_by_xpath(expected_element)
        assert profile_link.text == expected_username
