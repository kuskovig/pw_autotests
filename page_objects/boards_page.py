import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import BoardsPageLocators, HomePageLocators


class BoardsPage(BasePage):

    @allure.step("Deleting board")
    def delete_board(self, timeout=2):
        self.wait_for_element_and_click(*BoardsPageLocators.BOARD_ACTIONS)
        self.wait_for_element_and_click(*BoardsPageLocators.REMOVE_BOARD_BUTTON)
        self.wait_for_element_and_click(*BoardsPageLocators.CONFIRM_BOARD_REMOVE_BUTTON)
        try:
            WebDriverWait(self.browser, timeout).until(lambda x: self.browser.title == "Planyway")
        except TimeoutException:
            self.logger.warning(f"Title didn't change in {timeout} seconds")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Title didn't change in {timeout} seconds")

    @allure.step("Editing Board")
    def edit_board(self, timeout=2):
        self.wait_for_element_and_click(*BoardsPageLocators.BOARD_ACTIONS, timeout)
        self.wait_for_element_and_click(*BoardsPageLocators.EDIT_BOARD_BUTTON, timeout)
        self.enter_data(*HomePageLocators.CREATEBOARD_POPUP_NAME, "OtherName")
        self.wait_for_element_and_click(*HomePageLocators.CREATEBOARD_POPUP_CREATE_BUTTON, timeout)
