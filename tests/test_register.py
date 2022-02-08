import pytest


@pytest.mark.smoke
def test_fill_name_field(app, user_from_config):
    app.main_page.click_to_sign_up_button()
    app.register_page.fill_first_name_field(user_from_config.first_name)
    app.register_page.fill_last_name_field(user_from_config.last_name)
    app.register_page.check_value_in_field(user_from_config.first_name)


def test_faild_test_example(app, user_from_config):
    app.main_page.click_to_sign_up_button()
    app.register_page.fill_first_name_field(user_from_config.first_name)
    app.register_page.fill_last_name_field(user_from_config.last_name)
    app.register_page.check_value_in_field(user_from_config.last_name)


def test_error_test_example(app, user_from_confic):
    app.register_page.fill_last_name_field(user_from_config.last_name)
    app.register_page.check_value_in_field(user_from_config.last_name)
