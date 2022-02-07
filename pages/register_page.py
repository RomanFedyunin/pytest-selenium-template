from locators import RegisterPageLocators
from base import BasePage


class RegisterPage(BasePage):
    def fill_first_name_field(self, value):
        first_name_field = self.find_element(*RegisterPageLocators.FIRST_NAME_FIELD)
        first_name_field.click()
        first_name_field.send_keys(value)

    def fill_last_name_field(self, value):
        last_name_field = self.find_element(*RegisterPageLocators.LAST_NAME_FIELD)
        last_name_field.click()
        last_name_field.send_keys(value)
