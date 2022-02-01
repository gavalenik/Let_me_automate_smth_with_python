from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from allure_commons.types import AttachmentType
from time import sleep
import allure


class BasePage():
    def __init__(self, browser, url):  #, timeout=5):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            # self.browser.find_element(how, what)
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:  # NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_element_clickable(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    @allure.step('Open URL in browser')
    def open(self):
        self.browser.get(self.url)
        print('URL is opened')
        self.screenshot_to_allure_report("URL is opened")

    @allure.step('Browser page refresh')
    def page_refresh(self):
        sleep(1)
        self.browser.refresh()
        self.screenshot_to_allure_report("Browser page refreshed")

    def screenshot_to_allure_report(self, screenshot_name):
        allure.attach(self.browser.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=AttachmentType.PNG)
