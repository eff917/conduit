from time import sleep
from .utils.fixtures import driver
from .utils.allure_wrappers import take_screenshot

URL = "http://localhost:1667/"

def test_learn_more_link(driver):
    driver.delete_all_cookies()
    driver.get(URL)
    learn_more_link = driver.find_element_by_xpath('//a[@href="https://cookiesandyou.com/"]')
    learn_more_link.click()
    tab_titles = []
    for tab in driver.window_handles:
        driver.switch_to.window(tab)
        take_screenshot(driver=driver, name=f'{tab}')
        tab_titles.append(driver.title)

    assert 'What are cookies? | Cookies & You' in tab_titles

def test_decline_cookie_policy(driver):
    driver.delete_all_cookies()
    driver.get(URL)
    decline_button = driver.find_element_by_xpath('//div[contains(text(), "I decline!")]')
    decline_button.click()
    for cookie in driver.get_cookies():
        if cookie["name"] == 'vue-cookie-accept-decline-cookie-policy-panel':
            policy_accepted = cookie['value']
    assert policy_accepted == 'decline'

def test_accept_cookie_policy(driver):
    driver.delete_all_cookies()
    driver.get(URL)
    accept_button = driver.find_element_by_xpath('//div[contains(text(), "I accept!")]')
    accept_button.click()
    policy_accepted = ''
    for cookie in driver.get_cookies():
        if cookie["name"] == 'vue-cookie-accept-decline-cookie-policy-panel':
            policy_accepted = cookie['value']
    assert policy_accepted == 'accept'
