import allure
from allure_commons.types import AttachmentType


def take_screenshot(driver, name):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=AttachmentType.PNG,
    )
