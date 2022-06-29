"""
Test main page with selenium
"""
import allure
import pytest
import time
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .utils.fixtures import driver
from .utils.allure_wrappers import take_screenshot
from .utils.constants import URL


def test_wait_for_main_page_load(driver):
    """
    Wait for docker container to load
    """
    start_time = time.time()
    driver.get(URL)
    with allure.step(f"open conduit and take screenshot after main page loaded"):
        page_loaded_successfully = False
        # test if immediate refresh solves the problem
        driver.refresh()
        i = 1
        while not page_loaded_successfully:
            try:
                _ = WebDriverWait(driver, timeout=5, poll_frequency=1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "logo-font"))
                )
                elapsed_time = int(time.time() - start_time)
                take_screenshot(driver, f"Screenshot_after_{elapsed_time}s")
                # if the fluent wait doesn't raise an exception, break the cycle, else try again.
                page_loaded_successfully = True
            except TimeoutException:
                driver.refresh()
                i += 1
