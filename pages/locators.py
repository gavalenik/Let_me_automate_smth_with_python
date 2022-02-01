from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_CONTAINER_TITLE = (By.CSS_SELECTOR, "#boxAnmeldung > div.panel-header > h2")
    CHANGE_FORGOT_PASSWORD_CONTAINER_TITLE = (By.CSS_SELECTOR, "#boxPassword > div.panel-header > h2")
    LOGIN_FIELD_TITLE = (By.CSS_SELECTOR, "#loginForm #j_username-lbl")
    PASSWORD_FIELD_TITLE = (By.CSS_SELECTOR, "#loginForm > fieldset > div:nth-child(3) > label")
    VO_FIELD_TITLE = (By.CSS_SELECTOR, "#loginForm > fieldset > div:nth-child(4) > label")
    REMEMBER_ME_CHECKBOX_TITLE = (By.CSS_SELECTOR, "#loginForm > fieldset > div:nth-child(5) > label")
    CHANGE_PASSWORD_TITLE = (By.CSS_SELECTOR, "#pwdHelp")
    FORGOT_PASSWORD_TITLE = (By.CSS_SELECTOR, "#pwdRemind")
    LOGIN_FIELD = (By.CSS_SELECTOR, "#loginForm #j_username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#j_password")
    VO_FIELD = (By.CSS_SELECTOR, "#j_vo")
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, "#j_rememberMe")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login[name='login_btn']")
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "#pwdHelp > a")
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, "#pwdRemind > form > fieldset > input.flowActiveButton")
    FIRST_ERROR_MESSAGE = (By.CSS_SELECTOR, "#errorPanel > ul > li:nth-child(1)")
    SECOND_ERROR_MESSAGE = (By.CSS_SELECTOR, "#errorPanel > ul > li:nth-child(2)")
    THIRD_ERROR_MESSAGE = (By.CSS_SELECTOR, "#errorPanel > ul > li:nth-child(3)")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#boxError > div > #errorPanel")


class MobileCustomerSearchPageLocators:
    MOBILE_CUSTOMER_SEARCH_PAGE_TITLE = (By.CSS_SELECTOR, ".blc-title-wrap > h1")  # Kundensuche Mobilfunk
    EDIT_PHONE_NUMBER_BUTTON = (By.CSS_SELECTOR,
                                "#customerDataForm\:customerInfo\:repeatedSearchTmo\:showSearchPanel-btn")  # Rufnummer korrigieren
    AUTHENTICATION_CHECK_BOX = (By.CSS_SELECTOR,
                                "#customerAuthentication-form\:customerAuthentication\:auth-ch-box")  # Authentifizierung durchgeführt
    BACK_BUTTON = (By.CSS_SELECTOR, "#customersearchForm\:reset")  # Abbrechen
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#customersearchForm\:gotoCustomerview")  # Weiter
    CUSTOMER_AGREES_RADIO_BUTTON = (By.CSS_SELECTOR,
                                    "#kevForm\:kev\:allowKev-rd-grp\:0")  # Kunde stimmt dem Datenzugriff für diese Session zu
    CUSTOMER_REFUSES_RADIO_BUTTON = (By.CSS_SELECTOR,
                                     "#kevForm\:kev\:allowKev-rd-grp\:1")  # Kunde lehnt den Datenzugriff ab


class SignPageLocators:
    LOGIN_FIELD = (By.ID, "login-form:j_idt23:username")
    PASSWORD_FIELD = (By.ID, "login-form:j_idt23:password")
    ANMELDEN_BUTTON = (By.CSS_SELECTOR, "[id='login-form:j_idt23:loginbutton'] > span")
    SIGN_USER_ALREADY_LOGGED = (By.ID, "alreadyLogged-pnl")
    SIGN_LOGIN_ANYWAY_RADIO_BUTTON = (By.ID, "j_idt11:selectKikUser:0")
    SIGN_LOGIN_ANYWAY_BUTTON = (By.ID, "j_idt11:j_idt18")
    LOGOUT_LINK = (By.LINK_TEXT, "Abmelden")
    SEARCH_FIELD = (By.ID, "accountQuickForm:accountIdentifier")
    ACCOUNT_ID_ATTRIBUTE = (By.CSS_SELECTOR, "#account-form > .row:nth-child(6) > label")
    TAB_STATUS = (By.ID, "j_idt61:statusTab")
    CURRENT_STATUS = (By.LINK_TEXT, "locked")
    HEAD_OF_DROPDOWN_LIST = (By.ID, "statuses-form:j_idt106:status-table:0:j_idt125:name")
    DROPDOWN_LIST = (By.ID, "statuses-form:j_idt106:status-table:0:j_idt125:name")
    SAVE_BUTTON = (By.ID, "statuses-form:j_idt106:status-table:0:j_idt141")


class UserHomePageLocators:
    LOGIN_ANYWAY_RADIO_BUTTON = (By.CSS_SELECTOR, "#j_idt32\:kickUser-rd-grp\:0")
    LOGIN_ANYWAY_CONFIRM_BUTTON = (By.CSS_SELECTOR, "#j_idt32\:submit-btn[class='flowActiveButton']")
    LOGOUT_LINK = (By.CSS_SELECTOR, "[id='5-lnk']")  # "[id='5-lnk'] > .ui-menuitem-text")
    MOBILE_NUMBER_INPUT_FIELD = (By.CSS_SELECTOR, "#customerSearchForm\:j_idt111\:customerSearchTmoBox\:numberEntry")
    MOBILE_NUMBER_SEARCH_BUTTON = (By.CSS_SELECTOR, "#customerSearchForm\:j_idt111\:customerSearchTmoBox\:searchButton")
    MOBILE_NUMBER_SEARCH_BUTTON_TITLE = (By.CSS_SELECTOR,
                                         "#customerSearchForm\:j_idt111\:customerSearchTmoBox\:searchButton > span")  # Zur Kundensicht
    SESSION_ID = (By.CSS_SELECTOR, "#j_idt144\:supportInfo-txt")
    USER_ALREADY_LOGGED = (By.CSS_SELECTOR, "#alreadyLogged-hdr")
    # TSG_FIX_LINE fix line tab
    FIX_LINE_TAB = (By.CSS_SELECTOR,
                    "#customerSearchForm\:j_idt111\:tab > ul > li.ui-state-default.ui-corner-top.f-tab")
    FIX_LINE_PHONE_NUMBER_RADIO_BUTTON = (By.CSS_SELECTOR,
                                          "#customerSearchForm\:j_idt111\:customerSearchThoBox\:searchTypeSelect > li:nth-child(1) > label")
    FIX_LINE_CUSTOMER_ID_RADIO_BUTTON = (By.CSS_SELECTOR,
                                         "#customerSearchForm\:j_idt111\:customerSearchThoBox\:searchTypeSelect > li:nth-child(2) > label")
    FIX_LINE_NUMBER_INPUT_FIELD = (By.CSS_SELECTOR,
                                   "#customerSearchForm\:j_idt111\:customerSearchThoBox\:numberEntry")
    FIX_LINE_SEARCH_BUTTON = (By.CSS_SELECTOR,
                              "#customerSearchForm\:j_idt111\:customerSearchThoBox\:searchButton")
    FIX_LINE_SEARCH_BUTTON_TITLE = (By.CSS_SELECTOR,
                                    "#customerSearchForm\:j_idt111\:customerSearchThoBox\:searchButton > span")  # Zur Kundensicht

    # TSG_MOBILE inside frame group
    TSG_MOBILE_FUNC_FRAME_LINK_1 = (By.CSS_SELECTOR,
                                    "#customerSearchForm\:j_idt111\:tab\:beforeCustomerSearchBoxTmo-menu > ul > li:nth-child(1) > a > span")  # Neugeschäft Prepaid >
    TSG_MOBILE_FUNC_FRAME_LINK_2 = (By.CSS_SELECTOR,
                                    "#customerSearchForm\:j_idt111\:tab\:beforeCustomerSearchBoxTmo-menu > ul > li:nth-child(2) > a > span")  # Neugeschäft Laufzeit >
    TSG_MOBILE_FUNC_FRAME_LINK_3 = (By.CSS_SELECTOR,
                                    "#customerSearchForm\:j_idt111\:tab\:beforeCustomerSearchBoxTmo-menu > ul > li:nth-child(3) > a > span")  # Vouchertool >
    TSG_MOBILE_FUNC_FRAME_LINK_4 = (By.CSS_SELECTOR,
                                    "#customerSearchForm\:j_idt111\:tab\:beforeCustomerSearchBoxTmo-menu > ul > li:nth-child(4) > a > span")  # Legitimierungsprüfung >
    TSG_MOBILE_FUNC_FRAME_LINK_5 = (By.CSS_SELECTOR,
                                    "#customerSearchForm\:j_idt111\:tab\:afterCustomerSearchBoxTmo-menu > ul > li:nth-child(1) > a > span")  # Datentarif suchen >
    TSG_MOBILE_FUNC_FRAME_LINK_6 = (By.CSS_SELECTOR,
                                    "#customerSearchForm\:j_idt111\:tab\:afterCustomerSearchBoxTmo-menu > ul > li:nth-child(2) > a > span")  # Ersatzkartentausch >
    TSG_MOBILE_FUNC_FRAME_LINK_7 = (By.CSS_SELECTOR,
                                    "#customerSearchForm\:j_idt111\:tab\:afterCustomerSearchBoxTmo-menu > ul > li:nth-child(3) > a > span")  # Auftragsverfolgung >
    TSG_MOBILE_FUNC_FRAME_LINK_8 = (By.CSS_SELECTOR,
                                    "#customerSearchForm\:j_idt111\:tab\:afterCustomerSearchBoxTmo-menu > ul > li:nth-child(4) > a > span")  # Kaufen & Abholen >
    TSG_MOBILE_FUNC_FRAME_LINK_9 = (By.CSS_SELECTOR,
                                    "#customerSearchForm\:j_idt111\:tab\:afterCustomerSearchBoxTmo-menu > ul > li:nth-child(5) > a > span:nth-child(1)")  # BSP Prozesse >
    # TSG other processes group 1
    TSG_OTHER_PROCESS_LINK_1 = (By.CSS_SELECTOR,
                                "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(1) > a > span")  # Zubehör-Vermarktung >
    TSG_OTHER_PROCESS_LINK_2 = (By.CSS_SELECTOR,
                                "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(2) > a > span")  # T-Shop Hardware Tool  >
    TSG_OTHER_PROCESS_LINK_3 = (By.CSS_SELECTOR,
                                "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(3) > a > span")  # Handyversicherung >
    TSG_OTHER_PROCESS_LINK_4 = (By.CSS_SELECTOR,
                                "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(4) > a > span")  # Handyankauf >
    TSG_OTHER_PROCESS_LINK_5 = (By.CSS_SELECTOR,
                                "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(5) > a > span")  # Handyankauf im Shop >
    TSG_OTHER_PROCESS_LINK_6 = (By.CSS_SELECTOR,
                                "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(6) > a > span")  # Payback >
    TSG_OTHER_PROCESS_LINK_7 = (By.CSS_SELECTOR,
                                "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(7) > a > span")  # congstar Buchung >
    TSG_OTHER_PROCESS_LINK_8 = (By.CSS_SELECTOR,
                                "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(8) > a > span")  # Wholebuy Portal >
    TSG_OTHER_PROCESS_LINK_9 = (By.CSS_SELECTOR,
                                "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(9) > a > span")  # Wholebuy DEV >
    TSG_OTHER_PROCESS_LINK_10 = (By.CSS_SELECTOR,
                                "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(10) > a > span")  # Vorvermarktung >
    TSG_OTHER_PROCESS_LINK_11 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(11) > a > span")  # VVM Festnetz >
    TSG_OTHER_PROCESS_LINK_12 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(12) > a > span")  # Telekom Angebots-Mail >
    TSG_OTHER_PROCESS_LINK_13 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(13) > a > span")  # Service Versand Tool >
    TSG_OTHER_PROCESS_LINK_14 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(14) > a > span")  # Prepaid Multibrand >
    TSG_OTHER_PROCESS_LINK_15 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(15) > a > span")  # SCA KSA-Aufträge >
    TSG_OTHER_PROCESS_LINK_16 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(16) > a > span")  # Solo Artikel >
    TSG_OTHER_PROCESS_LINK_17 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(17) > a > span")  # Mietkündigung >
    TSG_OTHER_PROCESS_LINK_18 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(18) > a > span")  # 14 Tages Retoure >
    TSG_OTHER_PROCESS_LINK_19 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(19) > a > span")  # Handy-Reparatur für Fremdkunden >
    TSG_OTHER_PROCESS_LINK_20 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(20) > a > span:nth-child(1)")  # Redaktionssystem >
    # TSG other processes group 2
    TSG_OTHER_PROCESS_LINK_21 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses2-menu > ul > li:nth-child(1) > a > span")  # Leadmanagement M2M >
    TSG_OTHER_PROCESS_LINK_22 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses2-menu > ul > li:nth-child(2) > a > span")  # T-Map Portal >
    TSG_OTHER_PROCESS_LINK_23 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses2-menu > ul > li:nth-child(3) > a > span")  # Breitbandausbau >
    TSG_OTHER_PROCESS_LINK_24 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses2-menu > ul > li:nth-child(4) > a > span")  # VAS für Fremdkunden >
    TSG_OTHER_PROCESS_LINK_25 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses2-menu > ul > li:nth-child(5) > a > span")  # OTV >
    TSG_OTHER_PROCESS_LINK_26 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses2-menu > ul > li:nth-child(6) > a > span")  # RV Anträge >
    # TSG other processes group 3
    TSG_OTHER_PROCESS_LINK_27 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(1) > a > span")  # MoFu Kontakt erfassen >
    TSG_OTHER_PROCESS_LINK_28 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(2) > a > span")  # Formularverwaltung >
    TSG_OTHER_PROCESS_LINK_29 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(3) > a > span")  # Kontaktgründe verwalten >
    TSG_OTHER_PROCESS_LINK_30 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(4) > a > span")  # Umzugs - Service >
    TSG_OTHER_PROCESS_LINK_31 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(5) > a > span")  # Bauherren - Service >
    TSG_OTHER_PROCESS_LINK_32 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(6) > a > span")  # PARK >
    TSG_OTHER_PROCESS_LINK_33 = (By.CSS_SELECTOR,
                                 "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(7) > a > span")  # Direkt-Service MF >
    # TSG_FIX_LINE inside frame group
    TSG_FIX_LINE_FUNC_FRAME_LINK_1 = (By.CSS_SELECTOR,
                                      "#customerSearchForm\:j_idt111\:tab\:beforeCustomerSearchBoxTho-menu > ul > li:nth-child(1) > a > span")  # Neugeschäft >
    TSG_FIX_LINE_FUNC_FRAME_LINK_2 = (By.CSS_SELECTOR,
                                      "#customerSearchForm\:j_idt111\:tab\:beforeCustomerSearchBoxTho-menu > ul > li:nth-child(2) > a > span")  # Vouchertool >
    TSG_FIX_LINE_FUNC_FRAME_LINK_3 = (By.CSS_SELECTOR,
                                      "#customerSearchForm\:j_idt111\:tab\:afterCustomerSearchBoxTho-menu > ul > li > a > span")  # Aufträge >
    #
    # PARTNER_MOBILE inside frame group
    PARTNER_MOBILE_FUNC_FRAME_LINK_1 = (By.CSS_SELECTOR,
                                        "#customerSearchForm\:j_idt111\:tab\:beforeCustomerSearchBoxTmo-menu > ul > li:nth-child(1) > a > span")  # Neugeschäft Prepaid >
    PARTNER_MOBILE_FUNC_FRAME_LINK_2 = (By.CSS_SELECTOR,
                                        "#customerSearchForm\:j_idt111\:tab\:beforeCustomerSearchBoxTmo-menu > ul > li:nth-child(2) > a > span")  # Neugeschäft Laufzeit >
    PARTNER_MOBILE_FUNC_FRAME_LINK_3 = (By.CSS_SELECTOR,
                                        "#customerSearchForm\:j_idt111\:tab\:afterCustomerSearchBoxTmo-menu > ul > li:nth-child(1) > a > span")  # Datentarif suchen >
    PARTNER_MOBILE_FUNC_FRAME_LINK_4 = (By.CSS_SELECTOR,
                                        "#customerSearchForm\:j_idt111\:tab\:afterCustomerSearchBoxTmo-menu > ul > li:nth-child(2) > a > span")  # Auftragsverfolgung >
    # PARTNER other processes group 1
    PARTNER_OTHER_PROCESS_LINK_1 = (By.CSS_SELECTOR,
                                    "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(1) > a > span")  # Zubehör-Vermarktung >
    PARTNER_OTHER_PROCESS_LINK_2 = (By.CSS_SELECTOR,
                                    "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(2) > a > span")  # Handyankauf im Shop >
    PARTNER_OTHER_PROCESS_LINK_3 = (By.CSS_SELECTOR,
                                    "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(3) > a > span")  # Payback >
    PARTNER_OTHER_PROCESS_LINK_4 = (By.CSS_SELECTOR,
                                    "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(4) > a > span")  # congstar Buchung >
    PARTNER_OTHER_PROCESS_LINK_5 = (By.CSS_SELECTOR,
                                    "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(5) > a > span")  # Vorvermarktung >
    PARTNER_OTHER_PROCESS_LINK_6 = (By.CSS_SELECTOR,
                                    "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(6) > a > span")  # SCA KSA-Aufträge >
    PARTNER_OTHER_PROCESS_LINK_7 = (By.CSS_SELECTOR,
                                    "#otherProcesses-form\:otherProcesses\:otherProcesses1-menu > ul > li:nth-child(7) > a > span")  # Partnershop >
    # PARTNER other processes group 2
    PARTNER_OTHER_PROCESS_LINK_8 = (By.CSS_SELECTOR,
                                    "#otherProcesses-form\:otherProcesses\:otherProcesses2-menu > ul > li:nth-child(1) > a > span")  # HandyCheck >
    PARTNER_OTHER_PROCESS_LINK_9 = (By.CSS_SELECTOR,
                                     "#otherProcesses-form\:otherProcesses\:otherProcesses2-menu > ul > li:nth-child(2) > a > span")  # Breitbandausbau >
    PARTNER_OTHER_PROCESS_LINK_10 = (By.CSS_SELECTOR,
                                     "#otherProcesses-form\:otherProcesses\:otherProcesses2-menu > ul > li:nth-child(3) > a > span")  # Handy Konfiguration >
    PARTNER_OTHER_PROCESS_LINK_11 = (By.CSS_SELECTOR,
                                     "#otherProcesses-form\:otherProcesses\:otherProcesses2-menu > ul > li:nth-child(4) > a > span")  # VAS für Fremdkunden >
    PARTNER_OTHER_PROCESS_LINK_12 = (By.CSS_SELECTOR,
                                     "#otherProcesses-form\:otherProcesses\:otherProcesses2-menu > ul > li:nth-child(5) > a > span")  # RV Anträge >
    # PARTNER other processes group 3
    PARTNER_OTHER_PROCESS_LINK_13 = (By.CSS_SELECTOR,
                                     "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(1) > a > span")  # Gutschriftenfreigabe >
    PARTNER_OTHER_PROCESS_LINK_14 = (By.CSS_SELECTOR,
                                     "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(2) > a > span")  # Formularverwaltung >
    PARTNER_OTHER_PROCESS_LINK_15 = (By.CSS_SELECTOR,
                                     "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(3) > a > span")  # Kontaktgründe verwalten >
    PARTNER_OTHER_PROCESS_LINK_16 = (By.CSS_SELECTOR,
                                     "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(4) > a > span")  # Partnershop XU8 >
    PARTNER_OTHER_PROCESS_LINK_17 = (By.CSS_SELECTOR,
                                     "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(5) > a > span")  # ADV Self-Assessment - Selbstprogrammierer >
    PARTNER_OTHER_PROCESS_LINK_18 = (By.CSS_SELECTOR,
                                     "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(6) > a > span")  # SIM-Service Tool >
    PARTNER_OTHER_PROCESS_LINK_19 = (By.CSS_SELECTOR,
                                     "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(7) > a > span")  # Forecast-Tool CC >
    PARTNER_OTHER_PROCESS_LINK_20 = (By.CSS_SELECTOR,
                                     "#otherProcesses-form\:otherProcesses\:otherProcesses3-menu > ul > li:nth-child(8) > a > span")  # PARK >
    # PARTNER_FIX_LINE inside frame group
    PARTNER_FIX_LINE_FUNC_FRAME_LINK_1 = (By.CSS_SELECTOR,
                                          "#customerSearchForm\:j_idt111\:tab\:beforeCustomerSearchBoxTho-menu > ul > li:nth-child(1) > a > span")  # Neugeschäft >
    PARTNER_FIX_LINE_FUNC_FRAME_LINK_2 = (By.CSS_SELECTOR,
                                          "#customerSearchForm\:j_idt111\:tab\:beforeCustomerSearchBoxTho-menu > ul > li:nth-child(2) > a > span")  # EG-Neukunde >
    PARTNER_FIX_LINE_FUNC_FRAME_LINK_3 = (By.CSS_SELECTOR,
                                          "#customerSearchForm\:j_idt111\:tab\:afterCustomerSearchBoxTho-menu > ul > li:nth-child(1) > a > span")  # Aufträge >
    PARTNER_FIX_LINE_FUNC_FRAME_LINK_4 = (By.CSS_SELECTOR,
                                          "#customerSearchForm\:j_idt111\:tab\:afterCustomerSearchBoxTho-menu > ul > li:nth-child(2) > a > span")  # Reportdaten >

