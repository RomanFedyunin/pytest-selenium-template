from pages.locators import MainPageLocators
from base import BasePage
import allure


class MainPage(BasePage):
    @allure.step('Переходим на страницу регистрации с главной страницы')
    def click_to_sign_up_button(self):
        sign_up_button = self.find_element(*MainPageLocators.SIGN_UP_BUTTON)
        sign_up_button.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Переходим на страницу логина с главной страницы')
    def click_to_login_button(self):
        sign_up_button = self.find_element(*MainPageLocators.LOGIN_BUTTON)
        sign_up_button.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
