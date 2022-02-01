from pages.user_home_page import UserHomePage
from pages.login_page import LoginPage
from pages.sign_page import SignPage
import allure
import pytest
import main

# variables initialization_
url = main.initialization('Portal', 'portal_url')
user_login = main.initialization('User', 'user.login')
user_password = main.initialization('User', 'user.password')
user_vo = user_login[:5]


def successful_login_to_tvpp(browser, login, password, vo):
    try:
        page = LoginPage(browser, url)
        page.open()
        page.should_be_login_page()
        page.input_login(login)
        page.input_password(password)
        page.input_vo(vo)
        page.go_to_user_home_page()
        user_home_page = UserHomePage(browser, browser.current_url)
        user_home_page.should_be_user_home_page()
        return user_home_page
    except Exception as e:
        main.test_exception(e)


def unlock_user_in_sign(browser, locked_user_login):
    try:
        sign_url = main.initialization('Sign', 'sign_url')
        page = SignPage(browser, sign_url)
        page.open()
        page.should_be_sign_login_page()
        page.login_to_sign()
        page.should_be_sign_home_page()
        page.unlock_process(locked_user_login)
        page.sign_logout()
    except Exception as e:
        main.test_exception(e)


@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
class TestLoginPage:
    @pytest.mark.positive
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('Successful login to portal')
    def test_successful_login_to_tvpp(self, browser):
        user_home_page = successful_login_to_tvpp(browser, user_login, user_password, user_vo)
        user_home_page.portal_logout()

    @pytest.mark.positive
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('Login to portal with remember me checkbox')
    def test_successful_login_to_tvpp(self, browser):
        page = LoginPage(browser, url)
        page.open()
        page.should_be_login_page()
        page.input_login(user_login)
        page.input_password(user_password)
        page.input_vo(user_vo)
        page.select_checkbox_remember_me()
        page.go_to_user_home_page()
        user_home_page = UserHomePage(browser, browser.current_url)
        user_home_page.should_be_user_home_page()
        user_home_page.portal_logout()
        page = LoginPage(browser, browser.current_url)
        page.should_be_login_page()
        page.check_for_login_vo_rememberme_filled(user_login, user_vo)
        page.deselect_checkbox_remember_me()
        page.input_password(user_password)
        page.go_to_user_home_page()
        user_home_page = UserHomePage(browser, browser.current_url)
        user_home_page.should_be_user_home_page()
        user_home_page.portal_logout()
        page = LoginPage(browser, browser.current_url)
        page.should_be_login_page()
        page.check_that_all_fields_are_empty()

    @pytest.mark.negative
    @allure.title('Login to portal with empty fields')
    def test_empty_fields(self, browser):
        try:
            page = LoginPage(browser, url)
            page.open()
            page.should_be_login_page()
            page.go_to_user_home_page()
            page.error_message_all_fields_are_empty()
        except Exception as e:
            main.test_exception(e)

    @pytest.mark.negative
    @allure.title('Login to portal with wrong login')
    def test_wrong_login_attribute_during_login_to_tvpp(self, browser):
        try:
            page = LoginPage(browser, url)
            page.open()
            page.should_be_login_page()
            page.input_login("wrong_login")
            page.input_password(user_password)
            page.input_vo(user_vo)
            page.go_to_user_home_page()
            page.login_error_message(1)
        except Exception as e:
            main.test_exception(e)

    @pytest.mark.negative
    @allure.title('Login to portal with wrong vo')
    def test_wrong_vo_attribute_during_login_to_tvpp(self, browser):
        try:
            page = LoginPage(browser, url)
            page.open()
            page.should_be_login_page()
            page.input_login(user_login)
            page.input_password(user_password)
            page.input_vo("wrong_vo")
            page.go_to_user_home_page()
            page.login_error_message(1)
        except Exception as e:
            main.test_exception(e)

    @pytest.mark.negative
    @allure.title('Login to portal with wrong password 5 times')
    def test_wrong_password_five_times_during_login_to_tvpp(self, browser):
        try:
            lock_user_login = main.initialization('User', 'lock_user.login')
            lock_user_password = user_password
            lock_user_vo = lock_user_login[:5]
            page = LoginPage(browser, url)
            page.open()
            page.should_be_login_page()
            for i in range(5):
                page.input_login(lock_user_login)
                page.input_password("wrong_password")
                page.input_vo(lock_user_vo)
                page.go_to_user_home_page()
                page.login_error_message(i + 1)
                page.page_refresh()
            unlock_user_in_sign(browser, lock_user_login)
            user_home_page = successful_login_to_tvpp(browser, lock_user_login, lock_user_password, lock_user_vo)
            user_home_page.portal_logout()
        except Exception as e:
            main.test_exception(e)
