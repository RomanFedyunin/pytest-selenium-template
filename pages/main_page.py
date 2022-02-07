from locators import MainPageLocators
from base import BasePage


class MainPage(BasePage):
    def click_sign_up_button(self):
        sign_up_button = self.find_element(*MainPageLocators.SIGN_UP_BUTTON)
        sign_up_button.click()
