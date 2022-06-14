"""
Test main page with selenium
"""
from time import sleep
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .utils.fixtures import driver
from .utils.allure_wrappers import take_screenshot
URL = "http://localhost:1667/"

def test_wait_for_main_page_load(driver):
    """
    Wait for docker container to load
    """
    driver.get(URL)
    with allure.step(f"open conduit and take screenshot after main page loaded"):
        page_loaded_successfully = False
        # test if immediate refresh solves the problem
        driver.refresh()
        i = 1
        while not page_loaded_successfully:
            try:
                element = WebDriverWait(driver, timeout=5, poll_frequency=1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "logo-font"))
                )
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"Screenshot_after_wait_{i}",
                    attachment_type=AttachmentType.PNG,
                )
                # if the fluent wait doesn't raise an exception, break the cycle, else try again.
                page_loaded_successfully = True
            except TimeoutException:
                driver.refresh()
                i += 1


# conduit starts after 20-30seconds
def test_login(driver):
    """
    Dummy test 1
    """
    with allure.step(f"test login"):
        try:
            driver.get(URL)
            login_link = driver.find_element_by_xpath('//a[@href="#/login"]')
            login_link.click()
            take_screenshot(driver, "login_page")
            login_email_field = driver.find_element_by_xpath('//input[@placeholder="Email"]')
            login_password_field = driver.find_element_by_xpath('//input[@placeholder="Password"]')
            login_button = driver.find_element_by_xpath('//button[contains(text(), "Sign in")]')
            login_email_field.send_keys("user32@hotmail.com")
            login_password_field.send_keys("Userpass1")
            take_screenshot(driver, "login_page_after_fill")
            login_button.click()
            take_screenshot(driver, "after_login")

        except Exception as ex:  # pylint: disable=W0703
            print(ex)
    sleep(5)
    return True
