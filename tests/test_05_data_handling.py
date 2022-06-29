from time import sleep
import pytest
from .utils.fixtures import driver, login_logout_driver
from .utils.allure_wrappers import take_screenshot
#test_05_list_data.py
#test_06_multi_page_list.py
#test_07_new_data.py
#test_08_new_data_from_file.py
#test_09_modify_data.py
#test_10_download_data.py
#test_11_delete_data.py

def test_list_data(login_logout_driver):
    lorem_tag = login_logout_driver.find_element_by_xpath(
            '//div[@class="sidebar"]/div[@class="tag-list"]/a[text()="lorem"]')
    lorem_tag.click()
    sleep(2)
    take_screenshot(login_logout_driver, 'list_articles_after_login')
    article_list = login_logout_driver.find_elements_by_xpath('//a[@class="preview-link"]/h1')
    assert len(article_list) != 0

def test_list_multi_page_data(login_logout_driver):
        page_nr_list = login_logout_driver.find_elements_by_xpath('//a[@class="page-link"]')
        for page in page_nr_list:
            page.click()
            sleep(1)
            actual_page = login_logout_driver.find_element_by_xpath('//li[@class="page-item active"]')
            assert page.text == actual_page.text

@pytest.mark.skip()
def test_insert_data(driver):
    assert True

@pytest.mark.skip()
def test_bulk_insert_data_from_file(driver):
    assert True

@pytest.mark.skip()
def test_update_data(driver):
    assert True

@pytest.mark.skip()
def test_download_data(driver):
    assert True

@pytest.mark.skip()
def test_delete_data(driver):
    assert True
