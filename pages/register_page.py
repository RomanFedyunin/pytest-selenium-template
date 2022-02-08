from pages.locators import RegisterPageLocators
from base import BasePage
import allure


class RegisterPage(BasePage, RegisterPageLocators):
    @allure.step('Заполняем поле "First name" формы регистрации значением {value}')
    def fill_first_name_field(self, value):
        self.fill_the_field(self.FIRST_NAME_FIELD, value)

    @allure.step('Заполняем поле "Last name" формы регистрации значением {value}')
    def fill_last_name_field(self, value):
        self.fill_the_field(self.LAST_NAME_FIELD, value)

    @allure.step('Подтверждаем отправку формы регистрации кликом на кнопку "Register"')
    def submit_register_form(self):
        self.find_element(*self.REGISTER_BUTTON).click()

    @allure.step('Проверяем значение в поле "First name". Ожидаем {expected_value}')
    def check_value_in_field(self, expected_value):
        first_name_field = self.find_element(*self.FIRST_NAME_FIELD)
        real_value = first_name_field.get_attribute('value')
        assert real_value == expected_value, f'В поле "First Name" введено некорректное значение. ' \
                                             f'Ожидали: {expected_value}, получили: {real_value}'