from selenium.webdriver.common.by import By


class HeaderLocators:
    FEATURES_DROPDOWN = (By.CSS_SELECTOR, ".page-header__navigation--desktop ul li:nth-child(1)")
    SOLUTIONS_DROPDOWN = (By.CSS_SELECTOR, ".page-header__navigation--desktop ul li:nth-child(2)")
    RESOURCES_DROPDOWN = (By.CSS_SELECTOR, ".page-header__navigation--desktop ul li:nth-child(3)")
    DROPDOWN_LINKS = (By.CSS_SELECTOR, "dropdown a")
    GO_TO_APP_BUTTON = (By.CSS_SELECTOR, "header app-button")


class MainPageLocators:
    SIGNIN_BUTTON_HEADER = (By.CSS_SELECTOR, ".home__main a.button")
    SIGN_WITH_TRELLO_BUTTON = (By.CSS_SELECTOR, ".pw-dialog-content button")
    HEADER_USER_AVATAR = (By.CSS_SELECTOR, "header profile-menu")
    PROFILE_POPUP_PROFILE = (By.CSS_SELECTOR, ".profile-popup__actions a[href='/profile']")
    PROFILE_POPUP_SIGNOUT = (By.CSS_SELECTOR, ".profile-popup__actions button")


class HomePageLocators:
    HOME_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "pw-home .pw-board-picker__account-btn")
    NEW_BOARD_BUTTON = (By.CSS_SELECTOR, "div.pw-board-picker__organization-board-new")
    CREATEBOARD_POPUP_NAME = (By.CSS_SELECTOR, "md-dialog input.pw-input__control")
    CREATEBOARD_POPUP_COLOR = (By.CSS_SELECTOR, "div.pw-dialog-board__backgrounds "
                                                "div:not(.pw-dialog-board__background-tick)")
    CREATEBOARD_POPUP_CREATE_BUTTON = (By.CSS_SELECTOR, ".pw-dialog-footer button:nth-child(2)")
    HOMEPAGE_BOARDS = (By.CSS_SELECTOR, "a.pw-board-picker__organization-board")
    CONTACT_SUPPORT_BUTTON = (By.CSS_SELECTOR, ".pw-home-sidebar div.pw-home-sidebar__button:nth-child(6)")
    CONTACT_SUPPORT_DIALOG = (By.CSS_SELECTOR, "md-dialog.pw-dialog")
    CONTACT_SUPPORT_DIALOG_TITLE = (By.CSS_SELECTOR, ".pw-dialog-header__title")
    CONTACT_SUPPORT_TEXTAREA = (By.CSS_SELECTOR, ".pw-dialog-feedback__input textarea")
    CONTACT_SUPPORT_SEND_BUTTON = (By.CSS_SELECTOR, ".pw-dialog-footer button:nth-child(2)")
    WRONG_LOCATOR = (By.CSS_SELECTOR, "123qwe")


class TrelloAuthorizeWindowLocators:
    AUTHORIZE_TRELLO = (By.CSS_SELECTOR, ".buttons a")
    ACCEPT_AUTHORIZED_TRELLO = (By.CSS_SELECTOR, ".buttons input[name='approve']")
    USERNAME_FIELD = (By.CSS_SELECTOR, "input#user")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input#password")
    LOGIN_WITH_ATLASSIAN_BUTTON = (By.CSS_SELECTOR, "input#login")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button#login-submit")
    VALID_TRELLO_USER = {"username": "//",
                         "password": "//",
                         "first_name": "Forpw",
                         "second_name": "Test"}

    INVALID_TRELLO_USER = {"username": "not-a-real-user123@yandex.ru",
                           "password": "not-a-valid-password"}


class BoardsPageLocators:
    BOARD_ACTIONS = (By.CSS_SELECTOR, " .pw-scheduler-sidebar__board-actions-btn")
    REMOVE_BOARD_BUTTON = (By.CSS_SELECTOR, ".pw-menu-trello-lists-content > md-menu-item:nth-child(2) > "
                                            "button:nth-child(1)")
    EDIT_BOARD_BUTTON = (By.CSS_SELECTOR, ".pw-menu-trello-lists-content > md-menu-item:nth-child(1) > "
                                          "button:nth-child(1)")
    CONFIRM_BOARD_REMOVE_BUTTON = (By.CSS_SELECTOR, "button.pw-btn:nth-child(2)")
    ADD_CARD_BUTTON = (By.CSS_SELECTOR, ".pw-split-btn__main-btn-text")
