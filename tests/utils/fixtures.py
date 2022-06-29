import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from .constants import URL

WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument(f"--window-size={WINDOW_SIZE}")


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    # pass driver to calling test
    yield driver
    # quit after test finished
    driver.quit()


@pytest.fixture()
def create_user(driver):
    driver.get(URL)
    signup_link = driver.find_element_by_xpath('//a[@href="#/register"]')
    signup_link.click()
    signup_username_field = driver.find_element_by_xpath(
        '//input[@placeholder="Username"]'
    )
    signup_email_field = driver.find_element_by_xpath('//input[@placeholder="Email"]')
    signup_password_field = driver.find_element_by_xpath(
        '//input[@placeholder="Password"]'
    )
    signup_button = driver.find_element_by_xpath(
        '//button[contains(text(), "Sign up")]'
    )

    signup_username_field.send_keys("testuser1")
    signup_email_field.send_keys("testuser1@mailinator.com")
    signup_password_field.send_keys("TestUserPass1")
    signup_button.click()
    sleep(2)
    ok_link = driver.find_element_by_xpath(
        '//button[@class="swal-button swal-button--confirm"]'
    )
    ok_link.click()
    logout_link = driver.find_element_by_xpath('//a[@active-class="active"]')
    logout_link.click()
    sleep(1)
    yield
    # deleting the user should come here, but there's no such option in Conduit


@pytest.fixture()
def login_driver(driver):
    driver.get(URL)
    login_link = driver.find_element_by_xpath('//a[@href="#/login"]')
    login_link.click()
    login_email_field = driver.find_element_by_xpath('//input[@placeholder="Email"]')
    login_password_field = driver.find_element_by_xpath(
        '//input[@placeholder="Password"]'
    )
    login_button = driver.find_element_by_xpath('//button[contains(text(), "Sign in")]')
    login_email_field.send_keys("testuser1@mailinator.com")
    login_password_field.send_keys("TestUserPass1")
    login_button.click()
    # sleep one second to wait for animation to end
    sleep(1)
    # pass control to test
    yield driver


@pytest.fixture()
def login_logout_driver(driver):
    driver.get(URL)
    login_link = driver.find_element_by_xpath('//a[@href="#/login"]')
    login_link.click()
    login_email_field = driver.find_element_by_xpath('//input[@placeholder="Email"]')
    login_password_field = driver.find_element_by_xpath(
        '//input[@placeholder="Password"]'
    )
    login_button = driver.find_element_by_xpath('//button[contains(text(), "Sign in")]')
    login_email_field.send_keys("testuser1@mailinator.com")
    login_password_field.send_keys("TestUserPass1")
    login_button.click()
    # sleep one second to wait for animation to end
    sleep(1)
    # pass control to test
    yield driver
    # logout after test
    logout_link = driver.find_element_by_xpath('//a[@active-class="active"]')
    logout_link.click()
