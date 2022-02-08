import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.application import Application
from models.user import User


def load_config():
    with open('config.json') as config_json:
        config = json.load(config_json)
    return config


def pytest_addoption(parser):
    config = load_config()
    users = [user for user in config['user'].keys()]
    stands = [stand for stand in config['stand'].keys()]
    browsers = [browser for browser in config['browser'].keys()]
    parser.addoption('--browser', action='store', default='chrome', choices=browsers, help=f'Название браузера')
    parser.addoption('--headless', action='store_true', default=False,
                     help='Запуск без реального открытия окна браузера')
    parser.addoption('--stand', action='store', default='demo',
                     help=f'Доступные стенды в конфиге: {stands}; или произвольный url (без "/")')
    user_group = parser.getgroup(name='profile',
                                 description=f'Доступные пользователи в конфиге (через --user):\n  {users}\n'
                                             f'Или отдельно username и password через соответствующие ключи'
                                 )
    user_group.addoption('--user', action='store', default='test_admin')
    user_group.addoption('--username', action='store')
    user_group.addoption('--password', action='store')


def get_option_from_cmd_or_config(key, request):
    try:
        from_cmd = request.config.getoption('--' + key)
        value = load_config()[key][from_cmd]
    except KeyError:
        value = request.config.getoption('--' + key)
    return value


# @pytest.fixture(scope='session', autouse=True)
# def create_allure_environment(request, web_driver):
#     env_from_config = load_config()['allure_env']
#     if request.config.getoption('--alluredir'):
#         environment = request.config.getoption('--alluredir')
#     else:
#         environment = env_from_config
#     browser_name = web_driver.name
#     stand = get_option_from_cmd_or_config('stand', request)
#     with open(environment, 'w', encoding='utf-8') as f:
#         if browser_name == 'chrome':
#             f.write(
#                 f'Browser= {browser_name} \n'
#                 # f'Browser_Version= {web_driver.capabilities["version"]} \n'
#                 f'Stand= {stand} \n'
#                 # f'Platform= {web_driver.capabilities["platform"]}'
#             )
#         elif browser_name == 'firefox':
#             f.write(
#                 f'Browser= {browser_name} \n'
#                 f'Browser_Version= {web_driver.capabilities["browserVersion"]} \n'
#                 f'Stand= {stand} \n'
#                 f'Platform= {web_driver.capabilities["platformName"]} \n'
#                 f'Platform_Version= {web_driver.capabilities["platformVersion"]}')


@pytest.fixture(scope="session")
def web_driver(request):
    browser_name = request.config.getoption('--browser')
    path_to_driver = load_config()['browser'][browser_name]
    service = Service(path_to_driver)

    if browser_name == "firefox":
        from selenium.webdriver.firefox.options import Options
        wd = webdriver.Firefox

    elif browser_name == "chrome":
        from selenium.webdriver.chrome.options import Options
        wd = webdriver.Chrome

    else:
        raise ValueError(f"Unrecognized browser {browser_name}")

    options = Options()
    if request.config.getoption('--headless'):
        options.add_argument('--headless')
    driver = wd(service=service, options=options)
    driver.set_window_size(1920, 1080)
    return driver


@pytest.fixture(scope="session", autouse=True)
def stop(request, web_driver):
    def fin():
        web_driver.quit()

    request.addfinalizer(fin)


@pytest.fixture(scope='session', autouse=True)
def user_from_config(request):
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    user = User()
    if username is None and password is None:
        user.email = load_config()['user'][request.config.getoption("--user")]['username']
        user.password = load_config()['user'][request.config.getoption("--user")]['password']
    else:
        user.email, user.password = username, password
    return user


@pytest.fixture(scope='function')
def app(request, user_from_config, web_driver):
    url = get_option_from_cmd_or_config('stand', request)
    app = Application(base_url=url, driver=web_driver)
    app.go_to_site()
    app.driver.switch_to.window(app.driver.window_handles[-1])
    return app
