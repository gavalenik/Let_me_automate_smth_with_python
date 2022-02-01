from .locators import MobileCustomerSearchPageLocators
from .base_page import BasePage


class MobileCustomerSearchPage(BasePage):
    def should_be_mobile_customer_search_page(self):
        remember_me = self.browser.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX)
        remember_me.click()
