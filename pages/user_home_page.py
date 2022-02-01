from .locators import UserHomePageLocators
from .base_page import BasePage
import allure

session_id = ""


class UserHomePage(BasePage):
    def check_all_links_inside_fix_line_frame_for_partner_user(self):
        assert self.is_element_present(*UserHomePageLocators.PARTNER_FIX_LINE_FUNC_FRAME_LINK_1), "Link_1 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_FIX_LINE_FUNC_FRAME_LINK_1).text
        assert title == "Neugeschäft >", "Partner fix-line frame link_1 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_FIX_LINE_FUNC_FRAME_LINK_2), "Link_2 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_FIX_LINE_FUNC_FRAME_LINK_2).text
        assert title == "EG-Neukunde >", "Partner fix-line frame link_2 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_FIX_LINE_FUNC_FRAME_LINK_3), "Link_3 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_FIX_LINE_FUNC_FRAME_LINK_3).text
        assert title == "Aufträge >", "Partner fix-line frame link_3 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_FIX_LINE_FUNC_FRAME_LINK_4), "Link_4 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_FIX_LINE_FUNC_FRAME_LINK_4).text
        assert title == "Reportdaten >", "Partner fix-line frame link_4 text is wrong"

    def check_all_links_inside_fix_line_frame_for_tsg_user(self):
        assert self.is_element_present(*UserHomePageLocators.TSG_FIX_LINE_FUNC_FRAME_LINK_1), "Link_1 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_FIX_LINE_FUNC_FRAME_LINK_1).text
        assert title == "Neugeschäft >", "TSG fix-line frame link_1 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_FIX_LINE_FUNC_FRAME_LINK_2), "Link_2 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_FIX_LINE_FUNC_FRAME_LINK_2).text
        assert title == "Vouchertool >", "TSG fix-line frame link_2 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_FIX_LINE_FUNC_FRAME_LINK_3), "Link_3 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_FIX_LINE_FUNC_FRAME_LINK_3).text
        assert title == "Aufträge >", "TSG fix-line frame link_3 text is wrong"

    def check_all_links_inside_mobile_frame_for_partner_user(self):
        assert self.is_element_present(*UserHomePageLocators.PARTNER_MOBILE_FUNC_FRAME_LINK_1), "Link_1 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_MOBILE_FUNC_FRAME_LINK_1).text
        assert title == "Neugeschäft Prepaid >", "Partner mobile frame link_1 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_MOBILE_FUNC_FRAME_LINK_2), "Link_2 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_MOBILE_FUNC_FRAME_LINK_2).text
        assert title == "Neugeschäft Laufzeit >", "Partner mobile frame link_2 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_MOBILE_FUNC_FRAME_LINK_3), "Link_3 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_MOBILE_FUNC_FRAME_LINK_3).text
        assert title == "Datentarif suchen >", "Partner mobile frame link_3 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_MOBILE_FUNC_FRAME_LINK_4), "Link_4 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_MOBILE_FUNC_FRAME_LINK_4).text
        assert title == "Auftragsverfolgung >", "Partner mobile frame link_4 text is wrong"

    def check_all_links_inside_mobile_frame_for_tsg_user(self):
        assert self.is_element_present(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_1), "Link_1 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_1).text
        assert title == "Neugeschäft Prepaid >", f"TSG mobile frame link_1 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_2), "Link_2 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_2).text
        assert title == "Neugeschäft Laufzeit >", f"TSG mobile frame link_2 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_3), "Link_3 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_3).text
        assert title == "Vouchertool >", f"TSG mobile frame link_3 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_4), "Link_4 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_4).text
        assert title == "Legitimierungsprüfung >", f"TSG mobile frame link_4 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_5), "Link_5 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_5).text
        assert title == "Datentarif suchen >", f"TSG mobile frame link_5 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_6), "Link_6 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_6).text
        assert title == "Ersatzkartentausch >", f"TSG mobile frame link_6 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_7), "Link_7 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_7).text
        assert title == "Auftragsverfolgung >", f"TSG mobile frame link_7 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_8), "Link_8 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_8).text
        assert title == "Kaufen & Abholen >", f"TSG mobile frame link_8 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_9), "Link_9 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_MOBILE_FUNC_FRAME_LINK_9).text
        assert title == "BSP Prozesse >", f"TSG mobile frame link_9 text is wrong"

    def check_all_other_process_links_for_partner_user(self):
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_1), "Link_1 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_1).text
        assert title == "Zubehör-Vermarktung >", "Partner other process link_1 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_2), "Link_2 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_2).text
        assert title == "Handyankauf im Shop >", "Partner other process link_2 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_3), "Link_3 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_3).text
        assert title == "Payback >", "Partner other process link_3 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_4), "Link_4 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_4).text
        assert title == "congstar Buchung >", "Partner other process link_4 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_5), "Link_5 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_5).text
        assert title == "Vorvermarktung >", "Partner other process link_5 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_6), "Link_6 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_6).text
        assert title == "SCA KSA-Aufträge >", "Partner other process link_6 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_7), "Link_7 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_7).text
        assert title == "Partnershop >", "Partner other process link_7 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_8), "Link_8 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_8).text
        assert title == "HandyCheck >", "Partner other process link_8 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_9), "Link_9 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_9).text
        assert title == "Breitbandausbau >", "Partner other process link_9 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_10), "Link_10 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_10).text
        assert title == "Handy Konfiguration >", "Partner other process link_10 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_11), "Link_11 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_11).text
        assert title == "VAS für Fremdkunden >", "Partner other process link_11 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_12), "Link_12 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_12).text
        assert title == "RV Anträge >", "Partner other process link_12 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_13), "Link_13 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_13).text
        assert title == "Gutschriftenfreigabe >", "Partner other process link_13 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_14), "Link_14 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_14).text
        assert title == "Formularverwaltung >", "Partner other process link_14 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_15), "Link_15 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_15).text
        assert title == "Kontaktgründe verwalten >", "Partner other process link_15 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_16), "Link_16 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_16).text
        assert title == "Partnershop XU8 >", "Partner other process link_16 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_17), "Link_17 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_17).text
        assert title == "ADV Self-Assessment - Selbstprogrammierer >", "Partner other process link_17 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_18), "Link_18 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_18).text
        assert title == "SIM-Service Tool >", "Part other proc link_18 text wron"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_19), "Link_19 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_19).text
        assert title == "Forecast-Tool CC >", "Partner other process link_19 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_20), "Link_20 is not present"
        title = self.browser.find_element(*UserHomePageLocators.PARTNER_OTHER_PROCESS_LINK_20).text
        assert title == "PARK >", "Partner other process link_20 text is wrong"

    def check_all_other_process_links_for_tsg_user(self):
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_1), "Link_1 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_1).text
        assert title == "Zubehör-Vermarktung >", "TSG other process link_1 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_2), "Link_2 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_2).text
        assert title == "T-Shop Hardware Tool  >", "TSG other process link_2 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_3), "Link_3 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_3).text
        assert title == "Handyversicherung >", "TSG other process link_3 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_4), "Link_4 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_4).text
        assert title == "Handyankauf >", "TSG other process link_4 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_5), "Link_5 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_5).text
        assert title == "Handyankauf im Shop >", "TSG other process link_5 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_6), "Link_6 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_6).text
        assert title == "Payback >", "TSG other process link_6 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_7), "Link_7 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_7).text
        assert title == "congstar Buchung >", "TSG other process link_7 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_8), "Link_8 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_8).text
        assert title == "Wholebuy Portal >", "TSG other process link_8 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_9), "Link_9 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_9).text
        assert title == "Wholebuy DEV >", "TSG other process link_9 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_10), "Link_10 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_10).text
        assert title == "Vorvermarktung >", "TSG other process link_10 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_11), "Link_11 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_11).text
        assert title == "VVM Festnetz >", "TSG other process link_11 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_12), "Link_12 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_12).text
        assert title == "Telekom Angebots-Mail >", "TSG other process link_12 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_13), "Link_13 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_13).text
        assert title == "Service Versand Tool >", "TSG other process link_13 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_14), "Link_14 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_14).text
        assert title == "Prepaid Multibrand >", "TSG other process link_14 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_15), "Link_15 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_15).text
        assert title == "SCA KSA-Aufträge >", "TSG other process link_15 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_16), "Link_16 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_16).text
        assert title == "Solo Artikel >", "TSG other process link_16 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_17), "Link_17 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_17).text
        assert title == "Mietkündigung >", "TSG other process link_17 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_18), "Link_18 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_18).text
        assert title == "14 Tages Retoure >", "TSG other process link_18 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_19), "Link_19 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_19).text
        assert title == "Handy-Reparatur für Fremdkunden >", "TSG other process link_19 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_20), "Link_20 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_20).text
        assert title == "Redaktionssystem >", "TSG other process link_20 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_21), "Link_21 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_21).text
        assert title == "Leadmanagement M2M >", "TSG other process link_21 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_22), "Link_22 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_22).text
        assert title == "T-Map Portal >", "TSG other process link_22 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_23), "Link_23 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_23).text
        assert title == "Breitbandausbau >", "TSG other process link_23 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_24), "Link_24 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_24).text
        assert title == "VAS für Fremdkunden >", "TSG other process link_24 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_25), "Link_25 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_25).text
        assert title == "OTV >", "TSG other process link_25 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_26), "Link_26 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_26).text
        assert title == "RV Anträge >", "TSG other process link_26 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_27), "Link_27 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_27).text
        assert title == "MoFu Kontakt erfassen >", "TSG other process link_27 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_28), "Link_28 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_28).text
        assert title == "Formularverwaltung >", "TSG other process link_28 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_29), "Link_29 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_29).text
        assert title == "Kontaktgründe verwalten >", "TSG other process link_29 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_30), "Link_30 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_30).text
        assert title == "Umzugs - Service >", "TSG other process link_30 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_31), "Link_31 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_31).text
        assert title == "Bauherren - Service >", "TSG other process link_31 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_32), "Link_32 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_32).text
        assert title == "PARK >", "TSG other process link_32 text is wrong"
        assert self.is_element_present(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_33), "Link_33 is not present"
        title = self.browser.find_element(*UserHomePageLocators.TSG_OTHER_PROCESS_LINK_33).text
        assert title == "Direkt-Service MF >", "TSG other process link_33 text is wrong"

    @allure.step('Go to fix-line tab')
    def click_on_fix_line_tab(self):
        assert self.is_element_present(*UserHomePageLocators.FIX_LINE_TAB), "Fix-line tab is not present"
        self.browser.find_element(*UserHomePageLocators.FIX_LINE_TAB).click()
        print('Fix line tab is displayed')
        self.screenshot_to_allure_report("Fix line tab is displayed")

    @allure.step('Portal logout')
    def portal_logout(self):
        self.browser.find_element(*UserHomePageLocators.LOGOUT_LINK).click()
        print('Portal logout')
        self.screenshot_to_allure_report("Portal logout")

    def search_for_customer_with_mobile_number(self):
        print("1")
        # TODO

    def should_be_logout_link(self):
        assert self.is_element_present(*UserHomePageLocators.LOGOUT_LINK), "Logout link is not present"

    def should_be_session_id(self):
        assert self.is_element_present(*UserHomePageLocators.SESSION_ID), "Session ID is not present"
        return self.browser.find_element(*UserHomePageLocators.SESSION_ID).text

    @allure.step('Page is user home page')
    def should_be_user_home_page(self):
        if self.is_element_present(*UserHomePageLocators.USER_ALREADY_LOGGED):  # if user is logged we will login anyway
            self.browser.find_element(*UserHomePageLocators.LOGIN_ANYWAY_RADIO_BUTTON).click()
            self.is_element_present(*UserHomePageLocators.LOGIN_ANYWAY_CONFIRM_BUTTON)
            self.browser.find_element(*UserHomePageLocators.LOGIN_ANYWAY_CONFIRM_BUTTON).click()
        session_id = self.should_be_session_id()
        self.should_be_logout_link()
        print('Page is user home page (UHP) ' + session_id)
        self.screenshot_to_allure_report("Page is user home page " + session_id)

    @allure.step('Partner user has all fix-line links on UHP')
    def should_be_all_fix_line_links_on_uhp_for_partner_user(self):
        self.check_all_links_inside_fix_line_frame_for_partner_user()
        print('UHP contains all fix-line links')
        self.screenshot_to_allure_report("UHP contains all fix-line links")

    @allure.step('TSG user has all fix-line links on UHP')
    def should_be_all_fix_line_links_on_uhp_for_tsg_user(self):
        self.check_all_links_inside_fix_line_frame_for_tsg_user()
        print('UHP contains all fix-line links')
        self.screenshot_to_allure_report("UHP contains all fix-line links")

    @allure.step('Partner user has all mobile links on UHP')
    def should_be_all_mobile_links_on_uhp_for_partner_user(self):
        self.check_all_links_inside_mobile_frame_for_partner_user()
        self.check_all_other_process_links_for_partner_user()
        print('UHP contains all mobile links')
        self.screenshot_to_allure_report("UHP contains all mobile links")

    @allure.step('TSG user has all mobile links on UHP')
    def should_be_all_mobile_links_on_uhp_for_tsg_user(self):
        self.check_all_links_inside_mobile_frame_for_tsg_user()
        self.check_all_other_process_links_for_tsg_user()
        print('UHP contains all mobile links')
        self.screenshot_to_allure_report("UHP contains all mobile links")
