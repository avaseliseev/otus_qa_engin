import pytest
from selenium import webdriver

from service import wait_title, wait_element

_URL_PAGES = '/index.php?route=account/login'
_LOGIN = 'test'
_PASSWORD = 'password'


def test_check_page_title(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{_URL_PAGES}')
    wait_title('Account Login', driver, timeout=timeout)
    wait_element('#content > div > div:nth-child(1) > div > h2', driver, timeout=timeout)
    wait_element('#content > div > div:nth-child(2) > div > h2', driver, timeout=timeout)


def test_check_description_customer(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{_URL_PAGES}')
    wait_element('#content > div > div:nth-child(1) > div > p:nth-child(3)', driver, timeout=timeout)


def test_button_customer(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{_URL_PAGES}')
    wait_element('a.btn', driver, timeout=timeout).click()


def test_check_email_and_password(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{_URL_PAGES}')
    wait_element('#input-email', driver, timeout=timeout)
    wait_element('#input-password', driver, timeout=timeout)


def test_click_button_login(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{_URL_PAGES}')
    wait_element('#input-email', driver, timeout=timeout).send_keys(_LOGIN)
    wait_element('#input-password', driver, timeout=timeout).send_keys(_PASSWORD)
    wait_element('[type=submit]', driver, timeout=timeout).click()


def test_check_table(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{_URL_PAGES}')
    wait_element('#column-right', driver, timeout=timeout)


@pytest.mark.parametrize('element', range(1, 14))
def test_click_button_table_base_url(base_url: str, driver: webdriver, timeout: float, element: int):
    driver.get(f'{base_url}{_URL_PAGES}')
    wait_element(f'.list-group-item:nth-child({element})', driver, timeout=timeout).click()
