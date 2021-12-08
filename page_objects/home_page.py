import allure

from .base_page import BasePage
from .locators import MainPageLocators
from .locators import TrelloAuthorizeWindowLocators
from .locators import HeaderLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



class HomePage(BasePage):

    @allure.step("Creating new board")
    def create_board(self):
