# TODO cases empty phone numbers, wrong format numbers

from test_login_page import successful_login_to_tvpp
from pages.mobile_customer_search_page import MobileCustomerSearchPage
import allure
import pytest
import main

# variables initialization
url = main.initialization('Portal', 'portal_url')
tsg_user_login = main.initialization('User', 'user.login')
tsg_user_password = main.initialization('User', 'user.password')
tsg_user_vo = tsg_user_login[:5]
partner_user_login = main.initialization('User', 'partner_user.login')
partner_user_password = tsg_user_password
partner_user_vo = partner_user_login[:5]


# def successful_search_for_customer_with_mobile_number(browser, user_home_page):
#     try:
#         user_home_page.search_for_customer_with_mobile_number()
#         mobile_customer_search_page = MobileCustomerSearchPage(browser, browser.current_url)
#         mobile_customer_search_page.should_be_mobile_customer_search_page()
#         mobile_customer_search_page.customer_authentication()
#         mobile_customer_search_page.customer_agrees_to_enter_to_portal()
#         return mobile_customer_search_page
#     except Exception as e:
#         main.test_exception(e)


@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
class TestUserHomePage:
    @pytest.mark.positive
    @allure.title('Check all links on UHP for TSG user')
    def test_tsg_user_all_links_on_uhp(self, browser):
        try:
            user_home_page = successful_login_to_tvpp(browser, tsg_user_login, tsg_user_password, tsg_user_vo)
            user_home_page.should_be_all_mobile_links_on_uhp_for_tsg_user()
            user_home_page.click_on_fix_line_tab()
            user_home_page.should_be_all_fix_line_links_on_uhp_for_tsg_user()
            user_home_page.portal_logout()
        except Exception as e:
            main.test_exception(e)

    @pytest.mark.positive
    @allure.title('Check all links on UHP for partner user')
    def test_partner_user_all_links_on_uhp(self, browser):
        try:
            user_home_page = successful_login_to_tvpp(browser, partner_user_login, partner_user_password,
                                                      partner_user_vo)
            user_home_page.should_be_all_mobile_links_on_uhp_for_partner_user()
            user_home_page.click_on_fix_line_tab()
            user_home_page.should_be_all_fix_line_links_on_uhp_for_partner_user()
            user_home_page.portal_logout()
        except Exception as e:
            main.test_exception(e)

    # @pytest.mark.positive
    # @allure.title('')
    # def test_successful_search_for_customer_with_mobile_number(self, browser):
    #     try:
    #         user_home_page = successful_login_to_tvpp(browser, partner_user_login, partner_user_password,
    #                                                   partner_user_vo)
    #         mobile_customer_search_page = successful_search_for_customer_with_mobile_number(browser, user_home_page)
    #     except Exception as e:
    #         main.test_exception(e)
