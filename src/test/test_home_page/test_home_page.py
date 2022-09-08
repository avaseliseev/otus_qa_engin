import random

import pytest
from selenium import webdriver

from service import wait_title, wait_element

_list_nav_down = ['Information', 'Customer Service', 'Extras', 'My Account']


def test_check_page_title(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}')
    wait_title('Your Store', driver, timeout=timeout)
    wait_element(' #logo > a > img', driver, timeout=timeout).click()


@pytest.mark.parametrize('product', ['MacBook', 'iPhone'])
def test_add_basket_product(base_url: str, driver: webdriver, timeout: float, product: str):
    driver.get(f'{base_url}')
    wait_element(f'[title^="{product}"]', driver, timeout=timeout).click()
    rand_count = random.randint(2, 5)
    wait_element(f'#input-quantity', driver, timeout=timeout).send_keys(rand_count)
    wait_element(f'.thumbnail img', driver, timeout=timeout).click()
    wait_element(f'[title^="Close"]', driver, timeout=timeout).click()
    wait_element(f'#button-cart.btn', driver, timeout=timeout).click()


@pytest.mark.parametrize('param', ['apple', 'samsung', 'test', 'tab'])
def test_search_bar(base_url: str, driver: webdriver, timeout: float, param: str):
    driver.get(f'{base_url}')
    wait_element('[name=search]', driver, timeout=timeout).send_keys(param)
    wait_element('.input-group-btn [type=button]', driver, timeout=timeout).click()


@pytest.mark.parametrize('currency', range(1, 4), ids=['EUR', 'GBR', 'US'])
def test_click_payment_unit(base_url: str, driver: webdriver, timeout: float, currency: int):
    driver.get(f'{base_url}')
    wait_element(f'.btn-group', driver, timeout=timeout).click()
    wait_element(f'li:nth-child({currency}) [type="button"]', driver, timeout=timeout).click()


@pytest.mark.parametrize('param', range(1, 6))
def test_click_nav_pull_right(base_url: str, driver: webdriver, timeout: float, param: int):
    driver.get(f'{base_url}')
    wait_element(f'#top-links > ul > li:nth-child({param}) > a > i', driver, timeout=timeout).click()


@pytest.mark.parametrize('param', _list_nav_down)
def test_check_nav_down(base_url: str, driver: webdriver, timeout: float, param: str):
    driver.get(f'{base_url}')
    element = wait_element(f'h5', driver, timeout=timeout)
    assert element.text in _list_nav_down
