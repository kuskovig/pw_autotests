import allure

from page_objects.boards_page import BoardsPage
from page_objects.home_page import HomePage


@allure.title("Test user can delete board")
def test_user_can_delete_board(browser, url, auth_cookie):
    page = HomePage(browser, url)
    page.add_auth_cookie(auth_cookie)
    page.open("/app")
    page.create_board("NewBoard123", 10)
    page = BoardsPage(browser, url)
    page.delete_board(10)


@allure.title("Test user can create card")
def test_user_can_edit_board(browser, url, auth_cookie):
    page = HomePage(browser, url)
    page.add_auth_cookie(auth_cookie)
    page.open("/app")
    page.create_board("NewBoard123", 10)
    page = BoardsPage(browser, url)
    page.edit_board(10)

