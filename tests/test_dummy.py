"""
Dummy module for pytest, needed to set up github actions
"""
from time import sleep
import allure
from allure_commons.types import AttachmentType
import pytest
import selenium
from selenium import webdriver
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


def test_if_main_page_loads():
    """
    Wait for docker container to load
    """
    with allure.step(f"open conduit and take screenshot after main page loaded"):
        try:
            driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=chrome_options
            )
            driver.get(URL)
            element = WebDriverWait(driver, 70, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "logo-font")))
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"main_page",
                attachment_type=AttachmentType.PNG,
            )
        except Exception as ex:  # pylint: disable=W0703
            print(ex)
        finally:
            driver.quit()


# conduit starts after 20-30seconds
@pytest.mark.parametrize("time", range(0, 10, 5))
def test_dummy(time):
    """
    Dummy test 1
    """
    with allure.step(f"open conduit and take screenshot after {time} seconds"):
        try:
            browser = webdriver.Chrome(
                ChromeDriverManager().install(), options=chrome_options
            )
            browser.get(URL)
            allure.attach(
                browser.get_screenshot_as_png(),
                name=f"Dummy_test_{time}",
                attachment_type=AttachmentType.PNG,
            )
        except Exception as ex:  # pylint: disable=W0703
            print(ex)
        finally:
            browser.quit()
    sleep(5)
    return True
