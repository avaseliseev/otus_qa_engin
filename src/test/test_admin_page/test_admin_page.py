from selenium import webdriver

from config import LOGIN, PASSWORD, EMAIL, URL_ADMIN_PAGE
from service import wait_title, wait_element


def test_check_page_title(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{URL_ADMIN_PAGE}')
    wait_title('Administration', driver, timeout=timeout)
    assert wait_element('.panel-title', driver, timeout=timeout).text == 'Please enter your login details.'


def test_check_username(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{URL_ADMIN_PAGE}')
    wait_element('#input-username', driver, timeout=timeout).send_keys(LOGIN)


def test_check_password(base_url: str, driver: webdriver, timeout: float, get_login=None):
    if get_login:
        test_check_username(base_url, driver, timeout=timeout)
    else:
        driver.get(f'{base_url}{URL_ADMIN_PAGE}')
    wait_element('#input-password', driver, timeout=timeout).send_keys(PASSWORD)


def test_button_login(base_url: str, driver: webdriver, timeout: float):
    test_check_password(base_url, driver, timeout=timeout, get_login=True)
    wait_element('[type=submit]', driver, timeout=timeout).click()


def test_forgotten_password(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{URL_ADMIN_PAGE}')
    wait_element('.help-block [href]', driver, timeout=timeout).click()
    wait_element('[for=input-email]', driver, timeout=timeout)
    wait_element('#input-email', driver, timeout=timeout).send_keys(EMAIL)
    wait_element('[type=submit]', driver, timeout=timeout).click()


def test_check_footer(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{URL_ADMIN_PAGE}')
    _element = wait_element('#footer', driver, timeout=timeout)
    assert _element.text == 'OpenCart © 2009-2022 All Rights Reserved.'
