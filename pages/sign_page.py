from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from .locators import SignPageLocators
from .base_page import BasePage
from main import initialization
from time import sleep
import allure


class SignPage(BasePage):
    @allure.step('Login to sign')
    def login_to_sign(self):
        login = initialization('Sign', 'sign_login')
        password = initialization('Sign', 'sign_password')
        self.browser.find_element(*SignPageLocators.LOGIN_FIELD).send_keys(login)
        self.browser.find_element(*SignPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*SignPageLocators.ANMELDEN_BUTTON).click()
        print('Login to Sign')
        self.screenshot_to_allure_report("Login to Sign")

    @allure.step('Sign logout')
    def sign_logout(self):
        self.browser.find_element(*SignPageLocators.LOGOUT_LINK).click()
        print('Sign logout')
        self.screenshot_to_allure_report("Sign logout")

    @allure.step('Page is sign home page')
    def should_be_sign_home_page(self):
        if self.is_element_present(*SignPageLocators.SIGN_USER_ALREADY_LOGGED):
            self.browser.find_element(*SignPageLocators.SIGN_LOGIN_ANYWAY_RADIO_BUTTON).click()
            sleep(1)
            self.browser.find_element(*SignPageLocators.SIGN_LOGIN_ANYWAY_BUTTON).click()
        assert self.is_element_present(*SignPageLocators.LOGOUT_LINK), "Logout link is not present"
        print('Page is Sign home page')
        self.screenshot_to_allure_report("Page is Sign home page")

    @allure.step('Page is sign login page')
    def should_be_sign_login_page(self):
        assert self.is_element_present(*SignPageLocators.LOGIN_FIELD), "Login field is not present"
        assert self.is_element_present(*SignPageLocators.PASSWORD_FIELD), "Password field is not present"
        print('Page is Sign login page')
        self.screenshot_to_allure_report("Page is Sign login page")

    @allure.step('Unlock user')
    def unlock_process(self, lock_user_login):
        self.browser.find_element(*SignPageLocators.SEARCH_FIELD).send_keys(lock_user_login)
        self.browser.find_element(*SignPageLocators.SEARCH_FIELD).send_keys(Keys.ENTER)
        assert self.is_element_present(*SignPageLocators.ACCOUNT_ID_ATTRIBUTE), "Search process is unsuccessful"
        self.browser.find_element(*SignPageLocators.TAB_STATUS).click()
        assert self.is_element_present(*SignPageLocators.CURRENT_STATUS), "Status locked is not found"
        self.browser.find_element(*SignPageLocators.CURRENT_STATUS).click()
        assert self.is_element_present(*SignPageLocators.DROPDOWN_LIST), "Dropdown with Statuses is not found"
        dropdown = Select(self.browser.find_element(*SignPageLocators.DROPDOWN_LIST))
        dropdown.select_by_value('active')
        self.browser.find_element(*SignPageLocators.SAVE_BUTTON).click()
        print('User has been unlocked')
        self.screenshot_to_allure_report("User has been unlocked")
