from pages.user_home_page import session_id
from configparser import ConfigParser
from pages.base_page import BasePage
from requests import post

candidates = ['data/test_data', 'data/secure_data']


def initialization(section, variable):
    parser = ConfigParser()
    parser.read(candidates)
    return parser.get(section, variable)


def telegram(text, notification):
    chat_id = initialization('Telegram', 'chat_id')
    token = initialization('Telegram', 'token')
    params = {'chat_id': chat_id,  'text': text, 'disable_notification': notification}
    post(f'https://api.telegram.org/bot{token}/sendMessage', params)


def test_exception(e):
    # TODO mark case as FAILED
    # TODO BasePage.screenshot_to_allure_report("Exception!")
    print(e)
    # TODO telegram(f"Exception :( - {e}\nSession ID - {session_id}", True)


# if __name__ == '__main__':
#     print("test")
