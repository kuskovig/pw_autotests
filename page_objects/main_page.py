import allure

from .base_page import BasePage
from .locators import MainPageLocators, HomePageLocators, TrelloAuthorizeWindowLocators, HeaderLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


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
        self.browser.switch_to.window(self.browser.window_handles[0])
        self.wait_for_element(*HomePageLocators.HOME_ACCOUNT_BUTTON, 5)  # assert there is user profile button

    @allure.step("Hovering over '{_selector}' element")
    def open_header_dropdown(self, _by, _selector):
        self.logger.info(f"Hovering over '{_selector}' element")
        element = self.wait_for_element(_by, _selector)
        ActionChains(self.browser).move_to_element(element).pause(0.1).perform()

    @allure.step("Checking header dropdown links to be valid")
    def check_header_dropdown_links(self, locator, timeout=2):
        dropdown_element = self.wait_for_element(*locator)
        for i in range(len(dropdown_element.find_elements(*HeaderLocators.DROPDOWN_LINKS))):
            dropdown_element = self.wait_for_element(*locator)
            link = dropdown_element.find_elements(*HeaderLocators.DROPDOWN_LINKS)[i]
            destination_href = link.get_property("href")
            self.open_header_dropdown(*locator)
            self.logger.info(f"clicking link n={i}")
            link.click()
            try:
                WebDriverWait(self.browser, timeout).until(lambda x: self.browser.current_url == destination_href)
            except TimeoutException:
                self.logger.warning(f"URL didn't change in {timeout} seconds")
                allure.attach(
                    name=self.browser.session_id,
                    body=self.browser.get_screenshot_as_png(),
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(f"URL didn't change in {timeout} seconds")
            self.browser.back()

    @allure.step("Opening user profile popup")
    def open_profile(self, timeout=2):
        self.wait_for_element_and_click(*MainPageLocators.HEADER_USER_AVATAR, timeout)
        self.wait_for_element_and_click(*MainPageLocators.PROFILE_POPUP_PROFILE, timeout)

    @allure.step("Logging out of user account")
    def logout(self, timeout=2):
        self.wait_for_element_and_click(*MainPageLocators.HEADER_USER_AVATAR, timeout)
        self.wait_for_element_and_click(*MainPageLocators.PROFILE_POPUP_SIGNOUT, timeout)
        self.wait_for_element_to_disappear(*MainPageLocators.HEADER_USER_AVATAR, timeout)
