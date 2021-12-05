import socket
import pytest
import logging
import requests

from test_data.payload import payload
from selenium import webdriver

logging.basicConfig(level=logging.INFO, filename="logs/selenium.log", filemode="w")
browser_logger = logging.getLogger("BROWSER_LOGGER")


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     choices=["chrome", "firefox", "opera", "edge"],
                     default="chrome")
    parser.addoption("--url",
                     action="store",
                     default="planyway.com")
    parser.addoption("--executor",
                     action="store",
                     default="local")
    parser.addoption("--bversion",
                     action="store")
    parser.addoption("--vnc",
                     action="store_true",
                     default=False)
    parser.addoption("--video",
                     action="store_true",
                     default=False)
    parser.addoption("--logs",
                     action="store_true",
                     default=False)


@pytest.fixture
def browser(request, auth=False):
    test_name = request.node.name

    def teardown():
        browser_logger.info("==============> CLOSING DRIVER")
        driver.quit()

    driver = None
    browser_choice = request.config.getoption("--browser")
    executor_choice = request.config.getoption("--executor")
    browser_version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    video = request.config.getoption("--video")
    logs = request.config.getoption("--logs")

    if executor_choice == "local":

        if browser_choice == "chrome":
            driver = webdriver.Chrome()
        elif browser_choice == "firefox":
            driver = webdriver.Firefox()
        elif browser_choice == "opera":
            driver = webdriver.Opera()
        elif browser_choice == "edge":
            driver = webdriver.Edge()
    else:
        executor_url = f"http://{executor_choice}:4444/wd/hub"
        caps = {
            "browserName": browser_choice,
            "browserVersion": browser_version,
            "name": test_name,
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": video,
                "enableLog": logs
            }
        }
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps)

    request.addfinalizer(teardown)
    driver.set_window_size(1960, 1080)
    browser_logger.info(f"==============> Starting {test_name}")
    if auth:
        r = requests.request('POST', 'https://planyway.com/api/b/planyway/auth', json=payload)
        auth_cookie = {i.name: i.value for i in r.cookies}
        driver.add_cookie(auth_cookie)
    return driver


@pytest.fixture(scope='session')
def browser_auth(request):
    browser(request, auth=True)


@pytest.fixture
def url(request):
    return f'https://{request.config.getoption("--url")}'
