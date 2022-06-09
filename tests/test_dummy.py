"""
Dummy module for pytest, needed to set up github actions
"""
from time import sleep
import allure
from allure_commons.types import AttachmentType
import pytest
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = "http://localhost:1667/"
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument(f"--window-size={WINDOW_SIZE}")

@pytest.fixture(autouse=True, scope='module')
def driver():
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options
        )
        yield driver
        driver.quit()

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
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"Dummy_test",
                attachment_type=AttachmentType.PNG,
            )
        except Exception as ex:  # pylint: disable=W0703
            print(ex)
    sleep(5)
    return True
