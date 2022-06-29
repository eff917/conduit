from time import sleep
import pytest
import allure
from allure_commons.types import AttachmentType

from .utils.fixtures import driver, login_logout_driver
from .utils.allure_wrappers import take_screenshot
#test_05_list_data.py
#test_06_multi_page_list.py
#test_07_new_data.py
#test_08_new_data_from_file.py
#test_09_modify_data.py
#test_10_download_data.py
#test_11_delete_data.py

URL = "http://localhost:1667/"

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
            sleep(2)
            actual_page = login_logout_driver.find_element_by_xpath('//li[@class="page-item active"]')
            assert page.text == actual_page.text

def test_insert_data(login_logout_driver):
    new_article_link = login_logout_driver.find_element_by_xpath('//a[@href="#/editor"]')
    new_article_link.click()
    sleep(2)
    take_screenshot(login_logout_driver, "before_fill")
    title_field = login_logout_driver.find_element_by_xpath('//input[@placeholder="Article Title"]')
    about_field = login_logout_driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]')
    article_field = login_logout_driver.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]')
    tags_field = login_logout_driver.find_element_by_xpath('//input[@class="ti-new-tag-input ti-valid"]')
    publish_button = login_logout_driver.find_element_by_xpath('//button[@type="submit"]')

    article_title = "Test Article"
    article_about = "about testing"
    article_body = "## Markdown Title\n### Markdown subtitle"
    tags_list = ["testtag", "testtag2"]

    title_field.send_keys(article_title)
    about_field.send_keys(article_about)
    article_field.send_keys(article_body)
    tags_field.send_keys("\n".join(tags_list))
    take_screenshot(login_logout_driver, "after_fill")
    publish_button.click()
    sleep(2)
    take_screenshot(login_logout_driver, "after_publish")
    actual_title = login_logout_driver.find_element_by_xpath('//h1')
    actual_tags_list = login_logout_driver.find_elements_by_xpath('//a[@class="tag-pill tag-default"]')

    for actual_tag, expected_tag in zip(actual_tags_list, tags_list):
        assert actual_tag.text == expected_tag

    assert actual_title.text == article_title

def test_update_data(login_logout_driver):
    login_logout_driver.get(URL + '#/articles/test-article')
    sleep(2)
    edit_button = login_logout_driver.find_element_by_xpath('//a[@href="#/editor/test-article"]')
    edit_button.click()
    sleep(2)
    title_field = login_logout_driver.find_element_by_xpath('//input[@placeholder="Article Title"]')
    publish_button = login_logout_driver.find_element_by_xpath('//button[@type="submit"]')

    title_field.send_keys(" Modified")
    publish_button.click()
    sleep(2)
    actual_title = login_logout_driver.find_element_by_xpath('//h1')
    assert actual_title.text == "Test Article Modified"


def test_download_data(login_logout_driver):
    title_list = login_logout_driver.find_elements_by_xpath('//h1')
    titles = []
    for a_title in title_list:
        titles.append(a_title.text)
    with open('article_titles.txt', 'w', encoding='utf8') as outfile:
            for a_title in titles:
                outfile.write(f"{a_title}\n")
    with open('article_titles.txt', 'r', encoding='utf8') as infile:
        for index, line in enumerate(infile):
            assert line.rstrip("\n") == titles[index]

    allure.attach.file(
        "article_titles.txt",
        name="article_titles.txt",
        attachment_type=AttachmentType.TEXT,
    )
    

def test_delete_data(login_logout_driver):
    login_logout_driver.get(URL + '#/articles/test-article')
    sleep(2)
    delete_button = login_logout_driver.find_element_by_xpath('//button[@class="btn btn-outline-danger btn-sm"]')
    delete_button.click()
    sleep(2)
    title_list = login_logout_driver.find_elements_by_xpath('//h1')
    titles = []
    for a_title in title_list:
        titles.append(a_title.text)
    assert "Test Article Modified" not in titles

def test_bulk_insert_data_from_file(login_logout_driver):
    new_article_link = login_logout_driver.find_element_by_xpath('//a[@href="#/editor"]')
    new_article_link.click()
    sleep(1)
    title_field = login_logout_driver.find_element_by_xpath('//input[@placeholder="Article Title"]')
    about_field = login_logout_driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]')
    article_field = login_logout_driver.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]')
    tags_field = login_logout_driver.find_element_by_xpath('//input[@class="ti-new-tag-input ti-valid"]')
    publish_button = login_logout_driver.find_element_by_xpath('//button[@type="submit"]')

    with open('./tests/data/input.csv', 'r', encoding='utf8') as inputfile:
        for line in inputfile:
            # parse inputs
            article_title, article_about, article_body, tags_list = line.split(',')
            tags_list = tags_list.rstrip("\n").split(" ")
            
            new_article_link.click()
            sleep(1)
            take_screenshot(login_logout_driver, "before_fill")

            title_field.send_keys(article_title)
            about_field.send_keys(article_about)
            article_field.send_keys(article_body)
            tags_field.send_keys("\n".join(tags_list))
            take_screenshot(login_logout_driver, "after_fill")
            publish_button.click()
            sleep(1)
            take_screenshot(login_logout_driver, "after_publish")
            actual_title = login_logout_driver.find_element_by_xpath('//h1')
            actual_tags_list = login_logout_driver.find_elements_by_xpath('//a[@class="tag-pill tag-default"]')

            for actual_tag, expected_tag in zip(actual_tags_list, tags_list):
                assert actual_tag.text == expected_tag

            assert actual_title.text == article_title


