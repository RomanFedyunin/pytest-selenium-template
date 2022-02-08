from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    @allure.step('Открываем главную страницу по адрему')
    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, *locator, time=5):
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
        return element

    def find_elements(self, locator, time=5):
        elements = WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")
        return elements

    def fill_the_field(self, locator, value):
        field = self.find_element(*locator)
        field.click()
        field.send_keys(value)
