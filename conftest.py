import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def browser():
    service = Service('/home/roman/webdrivers/chromedriver')
    service.start()
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(service.service_url, options=options)
    yield driver
    driver.quit()