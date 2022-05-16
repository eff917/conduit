"""
Dummy module for pytest, needed to set up github actions
"""
import traceback
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
    try:
        browser = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options
        )
        browser.get(URL)
    except Exception as ex:  # pylint: disable=W0703
        print(traceback.format_exc(ex))
    return True


def test_dummy2():
    """
    Dummy test 2
    """
    try:
        browser = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options
        )
        browser.get(URL)
    except Exception as ex:  # pylint: disable=W0703
        print(traceback.format_exc(ex))
    return True
