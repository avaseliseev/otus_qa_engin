import pytest
from selenium import webdriver

from config import URL_DESCTOP_PAGE
from service import wait_element, SORT_NAME_DICT, SHOW_NAME_DICT


def test_add_product_compare(base_url: str, driver: webdriver, timeout: float, flag=False):
    if not flag:
        driver.get(f'{base_url}{URL_DESCTOP_PAGE}')
    wait_element('[class="fa fa-exchange"]', driver, timeout=timeout).click()
    wait_element('.alert-success', driver, timeout=timeout)


def test_check_product_compare(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{URL_DESCTOP_PAGE}')
    test_add_product_compare(base_url, driver, timeout=timeout, flag=True)
    test_add_product_compare(base_url, driver, timeout=timeout, flag=True)
    wait_element('#compare-total', driver, timeout=timeout).click()


@pytest.mark.parametrize('selector', SORT_NAME_DICT.values(), ids=SORT_NAME_DICT.keys())
def test_button_sort_by(base_url: str, driver: webdriver, timeout: float, selector: str):
    driver.get(f'{base_url}{URL_DESCTOP_PAGE}')
    wait_element(selector, driver, timeout=timeout).click()


@pytest.mark.parametrize('selector', SHOW_NAME_DICT.values(), ids=SHOW_NAME_DICT.keys())
def test_click_button_show(base_url: str, driver: webdriver, timeout: float, selector: str):
    driver.get(f'{base_url}{URL_DESCTOP_PAGE}')
    wait_element(selector, driver, timeout=timeout).click()


@pytest.mark.parametrize('selector', ('#list-view', '#grid-view'))
def test_click_display(base_url: str, driver: webdriver, timeout: float, selector: str):
    driver.get(f'{base_url}{URL_DESCTOP_PAGE}')
    wait_element(selector, driver, timeout=timeout).click()
