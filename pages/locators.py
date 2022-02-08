from selenium.webdriver.common.by import By


class MainPageLocators:
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, '.lvl-0.signup-free')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.lvl-0.sign-in')


class RegisterPageLocators:
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#inputFirstName')
    LAST_NAME_FIELD = (By.ID, 'inputLastName')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '.btn-primary.btn-block')


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, 'inputEmail')
    PASSWORD_FIELD = (By.ID, 'inputPassword')
    ALERT_MESSAGE = (By.CSS_SELECTOR, '.login .alert-body')
    LOGIN_SUBMIT_FORM_BUTTON = (By.CSS_SELECTOR, '.login .btn-primary')
