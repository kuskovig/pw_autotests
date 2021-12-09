import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import HomePageLocators


class HomePage(BasePage):

    @allure.step("Creating new board in first available workspace")
    def create_board(self, name, timeout=2):
        button = self.pick_random_element(HomePageLocators.NEW_BOARD_BUTTON, timeout)
        self.logger.info(f"Clicking '{button}' create board button")
        button.click()
        color = self.pick_random_element(HomePageLocators.CREATEBOARD_POPUP_COLOR, timeout)
        self.logger.info(f"Clicking '{color}' color")

        self.enter_data(*HomePageLocators.CREATEBOARD_POPUP_NAME, name)
        self.wait_for_element_and_click(*HomePageLocators.CREATEBOARD_POPUP_CREATE_BUTTON)
        try:
            WebDriverWait(self.browser, timeout).until(lambda x: self.browser.title == f"{name} | Planyway")
        except TimeoutException:
            self.logger.warning(f"Title didn't change in {timeout} seconds")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Title didn't change in {timeout} seconds")

    @allure.step("Opening board from home page")
    def go_to_created_board_from_homepage(self, href, timeout=2):
        self.open("/app")
        self.wait_for_element_and_click(By.CSS_SELECTOR,
                                        f"{HomePageLocators.HOMEPAGE_BOARDS[1]}[href='{href}']", timeout)
        assert self.browser.current_url == href

    @allure.step("Opening support form")
    def open_contact_support_popup(self, timeout=2):
        self.wait_for_element_and_click(*HomePageLocators.CONTACT_SUPPORT_BUTTON, timeout)
        dialog_popup = self.wait_for_element(*HomePageLocators.CONTACT_SUPPORT_DIALOG)
        dialog_title = dialog_popup.find_element(*HomePageLocators.CONTACT_SUPPORT_DIALOG_TITLE).text
        assert dialog_title == "Contact Support",\
            f"{dialog_title} != Contact Support"
    
    @allure.step("Sending contact form")
    def try_send_empty_form(self):
        self.enter_data(*HomePageLocators.CONTACT_SUPPORT_TEXTAREA, "")
        assert self.wait_for_element(*HomePageLocators.CONTACT_SUPPORT_SEND_BUTTON).get_property("disabled") is True
