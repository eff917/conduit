"""
Dummy module for pytest, needed to set up github actions
"""
import allure

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


URL = "http://localhost:1667/"
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument(f"--window-size={WINDOW_SIZE}")


def test_dummy():
    """
    Dummy test 1
    """
    with allure.step('open conduit and take screenshot'):
        try:
            browser = webdriver.Chrome(
                ChromeDriverManager().install(), options=chrome_options
            )
            browser.get(URL)
            allure.attach(browser.get_screenshot_as_png, name="Dummy_test_1", attachment_type=AttachmentType.PNG)
        except Exception as ex:  # pylint: disable=W0703
            print(ex)
    return True


def test_dummy2():
    """
    Dummy test 2
    """
    with allure.step('open conduit again, and take screenshot'):
        try:
            browser = webdriver.Chrome(
                ChromeDriverManager().install(), options=chrome_options
            )
            browser.get(URL)
            allure.attach(browser.get_screenshot_as_png(), name="Dummy_test_2", attachment_type=AttachmentType.PNG)
        except Exception as ex:  # pylint: disable=W0703
            print(ex)
    return True
