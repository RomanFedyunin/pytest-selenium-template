import pytest
from pages.main_page import MainPage
from pages.register_page import RegisterPage


def test_fill_the_field(browser):
    main_page = MainPage(browser)
    register_page = RegisterPage(browser)
    main_page.go_to_site()
    main_page.click_sign_up_button()
    browser.switch_to.window(browser.window_handles[1])
    register_page.fill_last_name_field("Roman")