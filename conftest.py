import pytest
from selenium import webdriver

from config import BASE_URL, CHROME_DRIVER, FIREFOX_DRIVER, YANDEX_DRIVER


def pytest_addoption(parser):
    parser.addoption("--browser", default='firefox', choices=['chrome', 'firefox', 'yandex'],
                     help="Добавьте браузер")
    parser.addoption("--headless", action='store_true', help="не открывать окно браузера")
    parser.addoption("--url", default=BASE_URL, help="адресс страницы")
    parser.addoption("--time_out", default=2, help="тайм аут ожидания")


@pytest.fixture
def timeout(request) -> float:
    return request.config.getoption("--time_out")


@pytest.fixture
def base_url(request) -> str:
    return request.config.getoption('--url')


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    options_chrome = webdriver.ChromeOptions()
    options_firefox = webdriver.FirefoxOptions()

    if headless:
        options_chrome.headless = True
        options_firefox.headless = True

    if browser_name == 'chrome':
        _driver = webdriver.Chrome(options=options_chrome, executable_path=CHROME_DRIVER)
    elif browser_name == 'firefox':
        _driver = webdriver.Firefox(options=options_firefox, executable_path=FIREFOX_DRIVER)
    elif browser_name == 'yandex':
        _driver = webdriver.Chrome(options=options_chrome, executable_path=YANDEX_DRIVER)

    yield _driver

    _driver.close()

    return driver
