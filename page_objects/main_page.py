import allure
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import TrelloAuthorizeWindowLocators
from .locators import HeaderLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException


class MainPage(BasePage):

    def login(self, credentials):
        self.wait_for_element_and_click(*MainPageLocators.SIGNIN_BUTTON_HEADER)  # Go to app page to login
        self.wait_for_element_and_click(*MainPageLocators.SIGN_WITH_TRELLO_BUTTON, 5)  # Open login popup
        self.browser.switch_to.window(self.browser.window_handles[1])  # Switch to Trello auth popup
        self.wait_for_element_and_click(*TrelloAuthorizeWindowLocators.AUTHORIZE_TRELLO)  # Accept login with Trello
        self.enter_data(*TrelloAuthorizeWindowLocators.USERNAME_FIELD, credentials["username"])  # Pass Trello login
        self.wait_for_element_to_be_invisible(*TrelloAuthorizeWindowLocators.PASSWORD_FIELD)  # Wait for Trello to
        # recognize atlassian username which leads to replacing password field to the next page
        self.wait_for_element_and_click(*TrelloAuthorizeWindowLocators.LOGIN_WITH_ATLASSIAN_BUTTON)  # Accept login
        # with Atlassian username
        self.enter_data(*TrelloAuthorizeWindowLocators.PASSWORD_FIELD, credentials["password"])  # Pass Trello password
        self.wait_for_element_and_click(*TrelloAuthorizeWindowLocators.LOGIN_BUTTON)  # Send login + password
        self.wait_for_element_and_click(*TrelloAuthorizeWindowLocators.ACCEPT_AUTHORIZED_TRELLO, 5)  # Authorize app

    @allure.step("Hovering over '{_selector}' element")
    def open_header_dropdown(self, _by, _selector):
        self.logger.info(f"Hovering over '{_selector}' element")
        element = self.wait_for_element(_by, _selector)
        ActionChains(self.browser).move_to_element(element).pause(0.1).perform()

    def go_to_help_page(self, timeout=2):
        self.open_header_dropdown(*HeaderLocators.RECOURCES_DROPDOWN)
        self.wait_for_element_and_click(*HeaderLocators.RECOUCES_HELP)
        try:
            WebDriverWait(self.browser, timeout).until(EC.title_is("Planyway Team Calendar - Planyway Help center"))
        except TimeoutException:
            self.logger.warning(f"Title didn't change in {timeout} seconds")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Title didn't change in {timeout} seconds")
        assert self.browser.current_url == self.url + "/help", "Current url doesnt match"

    @allure.step("Opening user profile popup")
    def open_profile(self):
        self.wait_for_element_and_click(*MainPageLocators.HEADER_USER_AVATAR)
        self.wait_for_element_and_click(*MainPageLocators.PROFILE_POPUP_PROFILE)

