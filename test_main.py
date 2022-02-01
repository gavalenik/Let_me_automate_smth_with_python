from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import pytest
import allure
import time


def screenshot_to_allure_report(self, screenshot_name):
    allure.attach(self.browser.get_screenshot_as_png(), name=screenshot_name,
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.MINOR)
def test_main_check(browser):
    try:
        link = "http://mobile-foodriver.site/staging/adminpanel"
        page = LoginPage(browser, link)
        page.open()
        browser.find_element(By.CSS_SELECTOR, "div.input-group:nth-child(2) > input").send_keys("admin")
        browser.find_element(By.CSS_SELECTOR, "div.input-group:nth-child(3) > input").send_keys("admin")
        time.sleep(1)
        screenshot_to_allure_report("tuta")
        # browser.find_element(By.CSS_SELECTOR, ".btn-block").click()
        # time.sleep(5)
        # browser.find_element(By.CSS_SELECTOR, "div.input-group:nth-child(2) > input").send_keys("admin")
        # browser.find_element(By.CSS_SELECTOR, "div.input-group:nth-child(3) > input").send_keys("admin")
        # time.sleep(1)
        # browser.find_element(By.CSS_SELECTOR, ".btn-block").click()
        # page.screenshot_to_allure_report("Test Screenshot")
        # allure.attach(browser.get_screenshot_as_png(), name="TestScreenshot",
        #               attachment_type=AttachmentType.PNG)
        # time.sleep(2)
        # assert browser.is_element_present(
        #     By.CSS_SELECTOR, "ul.navbar-nav:nth-child(2) > li:nth-child(5) > a:nth-child(1) > span"), "fu"
        # browser.find_element(
        #     By.CSS_SELECTOR, "ul.navbar-nav:nth-child(2) > li:nth-child(5) > a:nth-child(1) > span").click()
        # time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        time.sleep(2)
        browser.quit()


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.skip(reason="just for displaying in allure report")
def test_skipped():
    print("test")


@allure.severity(allure.severity_level.BLOCKER)
def test_always_done():
    print("test")
