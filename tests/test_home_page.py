from page_objects.home_page import HomePage
import allure


@allure.title("Test user can create board")
def test_user_can_create_board(browser, url, auth_cookie):
    page = HomePage(browser, url)
    page.add_auth_cookie(auth_cookie)
    page.open("/app")
    page.create_board("NewBoard123", 10)


@allure.title("Test user can open created board from the home page")
def test_user_can_open_created_board(browser, url, auth_cookie):
    page = HomePage(browser, url)
    page.add_auth_cookie(auth_cookie)
    page.open("/app")
    page.create_board("NewBoard123", 10)
    href = page.get_current_url()
    page.go_to_created_board_from_homepage(href, 10)


@allure.title("Test user can open contact support form within home page")
def test_user_can_open_contact_form(browser, url, auth_cookie):
    page = HomePage(browser, url)
    page.add_auth_cookie(auth_cookie)
    page.open("/app")
    page.open_contact_support_popup(10)


@allure.title("Test send form is disabled with empty message form")
def test_user_cannot_send_empty_form(browser, url, auth_cookie):
    page = HomePage(browser, url)
    page.add_auth_cookie(auth_cookie)
    page.open("/app")
    page.open_contact_support_popup(10)
    page.try_send_empty_form()
