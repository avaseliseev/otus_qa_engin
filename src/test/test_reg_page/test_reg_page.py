import pytest
from selenium import webdriver

from config import URL_LOGIN_PAGE
from service import wait_element, wait_title
from src.test.test_reg_page.user_data import send_personal_details, send_password


@pytest.mark.parametrize('num, name', [
    (3, 'First Name'),
    (4, 'Last Name'),
    (5, 'E-Mail'),
    (6, 'Telephone')
])
def test_check_personal_details(base_url: str, driver: webdriver, timeout: float, num: int, name: str):
    driver.get(f'{base_url}{URL_LOGIN_PAGE}')
    _element = wait_element(f'#account > div:nth-child({num})', driver, timeout=timeout)
    assert _element.text == name


@pytest.mark.parametrize('num, password', [
    (2, 'Password'),
    (3, 'Password Confirm')
])
def test_check_password(base_url: str, driver: webdriver, timeout: float,  num: int, password: str):
    driver.get(f'{base_url}{URL_LOGIN_PAGE}')
    _element = wait_element(f'.form-horizontal > fieldset:nth-child(2) > div:nth-child({num})', driver, timeout=timeout)
    assert _element.text == password


def test_click_subscribe(base_url: str, driver: webdriver, timeout: float, flag=False):
    if not flag:
        driver.get(f'{base_url}{URL_LOGIN_PAGE}')
    _element = wait_element(f'.form-horizontal > fieldset:nth-child(3) > div:nth-child(2) > label:nth-child(1)',
                            driver, timeout=timeout)
    wait_element(f'label.radio-inline [value="0"]', driver, timeout=timeout).click()
    wait_element(f'label.radio-inline [value="1"]', driver, timeout=timeout).click()
    assert _element.text == 'Subscribe'


def test_check_privacy_policy(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{URL_LOGIN_PAGE}')
    _element = wait_element(f'.buttons .pull-right', driver, timeout=timeout)

    assert _element.text == 'I have read and agree to the Privacy Policy  '


def test_click_privacy_policy(base_url: str, driver: webdriver, timeout: float, flag=False):
    if not flag:
        driver.get(f'{base_url}{URL_LOGIN_PAGE}')
    wait_element(f'[type=checkbox]', driver, timeout=timeout).click()
    wait_element(f'.agree', driver, timeout=timeout).click()
    wait_element(f'.close', driver, timeout=timeout).click()


def test_click_login_page(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{URL_LOGIN_PAGE}')
    wait_element(f'#content > p:nth-child(2) > a', driver, timeout=timeout).click()


def test_created_account(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{URL_LOGIN_PAGE}')
    send_personal_details(driver, timeout)
    send_password(driver, timeout)
    test_click_subscribe(base_url=f'{base_url}{URL_LOGIN_PAGE}', driver=driver, timeout=timeout, flag=True)
    test_click_privacy_policy(base_url=f'{base_url}{URL_LOGIN_PAGE}', driver=driver, timeout=timeout, flag=True)
    wait_element(f'[type=submit]', driver, timeout=timeout).click()
    wait_title('Your Account Has Been Created!', driver, timeout=timeout)
