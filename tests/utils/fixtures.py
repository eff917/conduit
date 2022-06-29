import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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
    pass
