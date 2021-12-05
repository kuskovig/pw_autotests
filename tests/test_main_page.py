from page_objects.main_page import MainPage
from page_objects.locators import TrelloAuthorizeWindowLocators
import allure
import pytest


@allure.title("Test user can login with correct credentials")
def test_user_can_login(browser, url):
    page = MainPage(browser, url)
    page.open()
    page.login(TrelloAuthorizeWindowLocators.VALID_TRELLO_USER)

@pytest.mark.help
@allure.title("User can go to the Help page from main page")
def test_user_can_open_help_page(browser, url):
    page = MainPage(browser, url)
    page.open()
    page.go_to_help_page()
