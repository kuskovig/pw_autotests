from selenium.webdriver.common.by import By


class HeaderLocators:
    FEATURES_DROPDOWN = (By.CSS_SELECTOR, ".page-header__navigation--desktop ul li:nth-child(1)")
    SOLUTIONS_DROPDOWN = (By.CSS_SELECTOR, ".page-header__navigation--desktop ul li:nth-child(2)")
    RECOURCES_DROPDOWN = (By.CSS_SELECTOR, ".page-header__navigation--desktop ul li:nth-child(3)")
    RECOUCES_HELP = (By.CSS_SELECTOR, ".page-header__navigation--desktop ul li:nth-child(3) a[href='/help']")


class MainPageLocators:
    SIGNIN_BUTTON_HEADER = (By.CSS_SELECTOR, ".home__main a.button")
    SIGN_WITH_TRELLO_BUTTON = (By.CSS_SELECTOR, ".pw-dialog-content button")
    HEADER_USER_AVATAR = (By.CSS_SELECTOR, "header .avatar-container")
    PROFILE_POPUP_PROFILE = (By.CSS_SELECTOR, ".profile-popup__actions a[href='/profile']")


class TrelloAuthorizeWindowLocators:
    AUTHORIZE_TRELLO = (By.CSS_SELECTOR, ".buttons a")
    ACCEPT_AUTHORIZED_TRELLO = (By.CSS_SELECTOR, ".buttons input[name='approve']")
    USERNAME_FIELD = (By.CSS_SELECTOR, "input#user")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input#password")
    LOGIN_WITH_ATLASSIAN_BUTTON = (By.CSS_SELECTOR, "input#login")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button#login-submit")
    VALID_TRELLO_USER = {"username": "forpwtest@yandex.ru",
                         "password": "MyPWPassword"}

    INVALID_TRELLO_USER = {"username": "not-a-real-user123@yandex.ru",
                           "password": "not-a-valid-password"}








