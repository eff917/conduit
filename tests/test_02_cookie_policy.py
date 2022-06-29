from time import sleep

import pytest
from .utils.fixtures import driver
from .utils.allure_wrappers import take_screenshot
from .utils.constants import URL


def test_learn_more_link(driver):
    """
    Test Learn more... link on cookie policy bar
    """

    driver.delete_all_cookies()
    driver.get(URL)
    learn_more_link = driver.find_element_by_xpath(
        '//a[@href="https://cookiesandyou.com/"]'
    )
    learn_more_link.click()
    tab_titles = []
    for tab in driver.window_handles:
        driver.switch_to.window(tab)
        take_screenshot(driver=driver, name=f"{tab}")
        tab_titles.append(driver.title)

    assert "What are cookies? | Cookies & You" in tab_titles


@pytest.mark.parametrize(
    "element_xpath, cookie_value",
    [
        ('//div[contains(text(), "I decline!")]', "decline"),
        ('//div[contains(text(), "I accept!")]', "accept"),
    ],
)
def test_cookie_policy(driver, element_xpath, cookie_value):
    """
    Test decline button on cookie policy bar
    """
    driver.delete_all_cookies()
    driver.get(URL)
    button = driver.find_element_by_xpath(element_xpath)
    button.click()
    for cookie in driver.get_cookies():
        if cookie["name"] == "vue-cookie-accept-decline-cookie-policy-panel":
            policy_accepted = cookie["value"]
    assert policy_accepted == cookie_value
