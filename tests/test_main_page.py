from page_objects.main_page import MainPage
from page_objects.locators import TrelloAuthorizeWindowLocators
import allure
import pytest
import time
from page_objects.locators import HeaderLocators

@pytest.mark.login
@allure.title("Test user can login with correct credentials")
def test_user_can_login(browser, url):
    page = MainPage(browser, url)
    page.open()
    page.login(TrelloAuthorizeWindowLocators.VALID_TRELLO_USER)
    page.should_be_logged_user_avatar()

@pytest.mark.profile
@allure.title("User can open profile via his avatar from main page")
def test_user_can_open_profile(browser, url, auth_cookie):
    page = MainPage(browser, url)
    page.add_auth_cookie(auth_cookie)
    page.open()
    page.open_profile(5)
    time.sleep(5)


@pytest.mark.parametrize("dropdown_block", [HeaderLocators.FEATURES_DROPDOWN,
                                            HeaderLocators.SOLUTIONS_DROPDOWN,
                                            HeaderLocators.RESOURCES_DROPDOWN],
                         ids=["Features links", "Solutions links", "Resources links"])
@allure.title("User can navigate through links in header dropdowns")
def test_user_can_open_dropdown_links(browser, url, dropdown_block):
    page = MainPage(browser, url)
    page.open()
    page.check_header_dropdown_links(dropdown_block)


@allure.title("Checking there is no 'Go to app' button when user logs out")
def test_user_can_logout(browser, url, auth_cookie):
    page = MainPage(browser, url)
    page.add_auth_cookie(auth_cookie)
    page.open()
    page.logout()
