from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://phptravels.com/demo/"

    def find_element(self, *locator, time=2):
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
        return element

    def find_elements(self, locator, time=10):
        elements = WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")
        return elements

    def go_to_site(self):
        return self.driver.get(self.base_url)