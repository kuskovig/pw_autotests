import logging
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.logger = logging.getLogger(type(self).__name__)

    def open(self, relative_url=""):
        with allure.step(f"Opening {self.url}{relative_url} url"):
            self.logger.info(f"Opening {self.url}{relative_url} url")
            self.browser.get(self.url + relative_url)

    @allure.step("Checking if the {_selector} element is present on page")
    def is_element_present(self, _by, _selector):
        self.logger.info(f"Trying to find '{_selector}' element by '{_by}'")
        try:
            self.browser.find_element(_by, _selector)
        except NoSuchElementException:
            self.logger.warning(f"Couldn't find element")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            return False
        return True

    @allure.step("Waiting for the {_selector} element for {timeout} seconds")
    def wait_for_element(self, _by, _selector, timeout=2):
        self.logger.info(f"Waiting for {_selector} element by {_by} for {timeout} seconds")
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((_by, _selector)))
        except TimeoutException:
            self.logger.warning(f"Element wasn't found in {timeout} seconds")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Couldn't find element for {timeout} seconds")
        return element

    @allure.step("Waiting for '{_selector}' element to appear and then clicking on it when it becomes clickable")
    def wait_for_element_and_click(self, _by, _selector, timeout=2):
        element = self.wait_for_element(_by, _selector, timeout)
        self.logger.info(f"clicking '{element}' element")
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((_by, _selector))).click()
        except ElementNotInteractableException:
            self.logger.warning(f"Cannot click on element {element}")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Cannot click on element {element}")

    @allure.step("Waiting for '{_selector}' element to disappear for {timeout} seconds")
    def wait_for_element_to_disappear(self, _by, _selector, timeout=2):
        self.logger.info(f"Waiting for {_selector} element by {_by} for {timeout} seconds to disappear")
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((_by, _selector)))
        except TimeoutException:
            self.logger.warning(f"Element didn't disappear in {timeout} seconds")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element didn't disappear in {timeout} seconds")

    @allure.step("Waiting for '{element}' element to be stale")
    def wait_for_element_to_stale(self, element, timeout=2):
        self.logger.info(f"Waiting for '{element}' element to be stale")
        try:
            WebDriverWait(self.browser, timeout).until(EC.staleness_of(element))
        except TimeoutException:
            self.logger.warning(f"Element didn't stale in {timeout} seconds")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element didn't stale in {timeout} seconds")

    @allure.step("Waiting for element with selector '{_selector} to be invisible'")
    def wait_for_element_to_be_invisible(self, _by, _selector, timeout=2):
        self.logger.info(f"Waiting for element with selector'{_selector} to be invisible'")
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.visibility_of_element_located((_by, _selector)))
        except TimeoutException:
            self.logger.warning(f"Element with selector {_selector} is still visible after {timeout} seconds")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element  with selector {_selector} was still visible after {timeout} seconds")

    @allure.step("Sending data = '{data}' into '{_locator}' element")
    def enter_data(self, _by, _locator, data):
        element = self.wait_for_element(_by, _locator)
        element.clear()
        self.logger.info(f"Sending data = '{data}' into '{_locator}' element")
        element.send_keys(data)
