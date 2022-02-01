from .locators import LoginPageLocators
from .base_page import BasePage
import allure


class LoginPage(BasePage):
    def check_for_login_vo_rememberme_filled(self, user_login, user_vo):
        self.is_element_present(*LoginPageLocators.LOGIN_FIELD), "Login Field is not displayed"
        login_text = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD).get_attribute("value")
        assert login_text == user_login, "Login is different"
        vo_text = self.browser.find_element(*LoginPageLocators.VO_FIELD).get_attribute("value")
        assert vo_text == user_vo, "VO is different"
        remember_me_checked = self.browser.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX).get_attribute("checked")
        assert remember_me_checked is not None, "Remember me checkbox is not selected"
        print("Login and VO fields are filled out")

    def check_that_all_fields_are_empty(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FIELD), "Login Field is not displayed"
        login_text = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD).get_attribute("value")
        assert login_text == "", "Login is not empty"
        vo_text = self.browser.find_element(*LoginPageLocators.VO_FIELD).get_attribute("value")
        assert vo_text == "", "VO is not empty"
        remember_me = self.browser.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX)
        remember_me_checked = remember_me.get_attribute("checked")
        assert remember_me_checked is None, "Remember me checkbox is selected"
        print("Success!! All fields are empty")

    def deselect_checkbox_remember_me(self):
        remember_me = self.browser.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX)
        remember_me.click()
        remember_me_checked = remember_me.get_attribute("checked")
        assert remember_me_checked is None, "Remember me checkbox is selected"

    @allure.step('Error message')
    def error_message_all_fields_are_empty(self):
        assert self.is_element_present(
            *LoginPageLocators.FIRST_ERROR_MESSAGE), "First error message is not presented"
        error_text = self.browser.find_element(*LoginPageLocators.FIRST_ERROR_MESSAGE).text
        assert error_text == "Benutzername: Eine Angabe in diesem Feld ist erforderlich.", "Wrong error text 1"
        assert self.is_element_present(
            *LoginPageLocators.SECOND_ERROR_MESSAGE), "Second error message is not presented"
        error_text = self.browser.find_element(*LoginPageLocators.SECOND_ERROR_MESSAGE).text
        assert error_text == "Passwort: Eine Angabe in diesem Feld ist erforderlich.", "Wrong error text 2"
        assert self.is_element_present(
            *LoginPageLocators.THIRD_ERROR_MESSAGE), "First error message is not presented"
        error_text = self.browser.find_element(*LoginPageLocators.THIRD_ERROR_MESSAGE).text
        assert error_text == "VO: Eine Angabe in diesem Feld ist erforderlich.", "Wrong error text 3"
        print('All error messages correct')
        self.screenshot_to_allure_report("All error messages correct")

    @allure.step('Go to user home page')
    def go_to_user_home_page(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        print('Go to user home page')

    @allure.step('Input login to field "Login"')
    def input_login(self, login):
        self.browser.find_element(*LoginPageLocators.LOGIN_FIELD).send_keys(login)
        print('Input login to field "Login"')

    @allure.step('Input password to field "Password"')
    def input_password(self, password):
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        print('Input password to field "Password"')

    @allure.step('Input password to field "VO"')
    def input_vo(self, vo):
        self.browser.find_element(*LoginPageLocators.VO_FIELD).send_keys(vo)
        print('Input VO to field "VO"')
        self.screenshot_to_allure_report("Input VO to field 'VO'")

    @allure.step('Error message')
    def login_error_message(self, attempt):
        assert self.is_element_present(
            *LoginPageLocators.ERROR_MESSAGE), "Error message is not presented"
        error_text = self.browser.find_element(*LoginPageLocators.ERROR_MESSAGE).text
        if attempt < 4:
            assert error_text == "Die Eingabe Ihrer VO-Kennung, Ihres Benutzernamens oder Passwortes ist nicht korrekt.", "Wrong error text"
        elif attempt == 4:
            assert error_text == "Die Eingabe Ihrer VO-Kennung, Ihres Benutzernamens oder Ihres Passwortes ist nicht korrekt. Sie haben nur noch einen Versuch.", "Wrong error text 4 time"
        elif attempt == 5:
            assert error_text == "Keine Anmeldung möglich, da der Zugang gesperrt ist. Bitte wenden Sie sich: fuer TSG/Handel an die Service Line Vertrieb und fuer DTKS an das Kennungsmanagement.", "Wrong error text 5 time"
        print(f'Error message number ' + str(attempt) +  ' is displayed')
        self.screenshot_to_allure_report("Error message")

    def select_checkbox_remember_me(self):
        remember_me = self.browser.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX)
        remember_me.click()
        remember_me_checked = remember_me.get_attribute("checked")
        assert remember_me_checked is not None, "Remember me checkbox is not selected"

    def should_be_change_forgot_password_container_title(self):
        assert self.is_element_present(
            *LoginPageLocators.CHANGE_FORGOT_PASSWORD_CONTAINER_TITLE), "Change pass container title is not presented"
        title = self.browser.find_element(*LoginPageLocators.CHANGE_FORGOT_PASSWORD_CONTAINER_TITLE).text
        assert title == "Passworthinweise", "Change/forgot password container title is wrong"

    def should_be_change_password_title(self):
        assert self.is_element_present(*LoginPageLocators.CHANGE_PASSWORD_TITLE), "Change password title is not present"
        title = self.browser.find_element(*LoginPageLocators.CHANGE_PASSWORD_TITLE).text
        assert title == "Lesen Sie hier, wie Sie z. B. ein neues Passwort vergeben.", "Change password title is wrong"

    def should_be_change_password_button(self):
        assert self.is_element_present(*LoginPageLocators.CHANGE_PASSWORD_BUTTON), "Change pass button is not presented"

    def should_be_forgot_password_title(self):
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_TITLE), "Forgot password title is not present"
        title = self.browser.find_element(*LoginPageLocators.FORGOT_PASSWORD_TITLE).text
        assert title == "Klicken Sie hier, wenn Sie Ihr Passwort vergessen haben.", "Forgot password title is wrong"

    def should_be_forgot_password_button(self):
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_BUTTON), "Forgot pass button is not presented"

    def should_be_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_login_container_title(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_CONTAINER_TITLE), "Login container title is not present"
        title = self.browser.find_element(*LoginPageLocators.LOGIN_CONTAINER_TITLE).text
        assert title == "Anmeldung", "Login container title is wrong"

    def should_be_login_field(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FIELD), "Login field is not presented"

    def should_be_login_field_title(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FIELD_TITLE), "Login field title is not presented"
        title = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD_TITLE).text
        assert title == "Benutzername *", "Login field title is wrong"

    @allure.step('Page is login page')
    def should_be_login_page(self):
        self.should_be_login_container_title()
        self.should_be_login_field_title()
        self.should_be_login_field()
        self.should_be_password_field_title()
        self.should_be_password_field()
        self.should_be_vo_field_title()
        self.should_be_vo_field()
        self.should_be_remember_me_checkbox_title()
        self.should_be_remember_me_checkbox()
        self.should_be_login_button()
        print('Page is login page')
        self.screenshot_to_allure_report("Page is login page")

    def should_be_password_field(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD), "Password field is not presented"

    def should_be_password_field_title(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD_TITLE), "Password field title is not presented"
        title = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_TITLE).text
        assert title == "Passwort *", "Password field title is wrong"

    def should_be_remember_me_checkbox(self):
        assert self.is_element_present(*LoginPageLocators.REMEMBER_ME_CHECKBOX), "RememberMe checkbox is not presented"

    def should_be_remember_me_checkbox_title(self):
        assert self.is_element_present(*LoginPageLocators.REMEMBER_ME_CHECKBOX_TITLE), "RememberMe title is not present"
        title = self.browser.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX_TITLE).text
        assert title == "Benutzerkennung merken?", "Remember me checkbox title is wrong"

    def should_be_vo_field(self):
        assert self.is_element_present(*LoginPageLocators.VO_FIELD), "VO field is not presented"

    def should_be_vo_field_title(self):
        assert self.is_element_present(*LoginPageLocators.VO_FIELD_TITLE), "VO field title is not presented"
        title = self.browser.find_element(*LoginPageLocators.VO_FIELD_TITLE).text
        assert title == "VO-Auswahl *", "VO field title is wrong"
