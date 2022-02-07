from selenium.webdriver.common.by import By


class MainPageLocators:
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, '.lvl-0.signup-free')


class RegisterPageLocators:
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#inputFirstName')
    LAST_NAME_FIELD = (By.ID, 'inputLastName')
