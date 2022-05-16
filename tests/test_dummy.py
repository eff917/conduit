"""
Dummy module for pytest, needed to set up github actions
"""
from time import sleep
import allure

from allure_commons.types import AttachmentType
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


URL = "http://localhost:1667/"
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument(f"--window-size={WINDOW_SIZE}")

@pytest.mark.parametrize("time", range(0,61,5))
def test_dummy(time):
    """
    Dummy test 1
    """
    with allure.step(f'open conduit and take screenshot after {time} seconds'):
        try:
            browser = webdriver.Chrome(
                ChromeDriverManager().install(), options=chrome_options
            )
            browser.get(URL)
            allure.attach(browser.get_screenshot_as_png(), name=f"Dummy_test_{time}", attachment_type=AttachmentType.PNG)
        except Exception as ex:  # pylint: disable=W0703
            print(ex)
    sleep(5)
    return True
