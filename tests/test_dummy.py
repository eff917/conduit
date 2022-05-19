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

# @pytest.mark.skip(reason="fluent wait always runs onto TimeoutException")
def test_if_main_page_loads():
    """
    Wait for docker container to load
    """
    with allure.step(f"open conduit and take screenshot after main page loaded"):
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options
        )
        driver.get(URL)
        # test if immediate refresh solves the problem
        driver.refresh()
        for i in range(4):
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"Screenshot_before_wait_{i}",
                    attachment_type=AttachmentType.PNG,
                )
                element = WebDriverWait(driver, timeout=5, poll_frequency=1, ignored_exceptions=[TimeoutException]).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "logo-font"))
                )
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"Screenshot_after_wait_{i}",
                    attachment_type=AttachmentType.PNG,
                )
                # if the fluent wait doesn't raise an exception, break the cycle, else try again.
                break
            except:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"Screenshot_after_wait_exception_{i}",
                    attachment_type=AttachmentType.PNG,
                )
                driver.refresh()

        driver.quit()


# conduit starts after 20-30seconds
@pytest.mark.parametrize("time", range(0, 10, 5))
def test_dummy(time):
    """
    Dummy test 1
    """
    with allure.step(f"open conduit and take screenshot after {time} seconds"):
        try:
            driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=chrome_options
            )
            driver.get(URL)
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"Dummy_test_{time}",
                attachment_type=AttachmentType.PNG,
            )
        except Exception as ex:  # pylint: disable=W0703
            print(ex)
        finally:
            driver.quit()
    sleep(5)
    return True
