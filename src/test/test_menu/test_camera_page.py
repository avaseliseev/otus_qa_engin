import pytest
from selenium import webdriver
from service import wait_title, wait_element, SORT_NAME_DICT, SHOW_NAME_DICT

_URL_PAGES = '/camera'


def test_check_page_title(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{_URL_PAGES}')
    wait_title('Cameras', driver, timeout=timeout)
    wait_element('#content', driver, timeout=timeout)
    wait_element('#content', driver, timeout=timeout)


@pytest.mark.parametrize('selector', SORT_NAME_DICT.values(), ids=SORT_NAME_DICT.keys())
def test_button_sort_by(base_url: str, driver: webdriver, timeout: float, selector: str):
    driver.get(f'{base_url}{_URL_PAGES}')
    wait_element(selector, driver, timeout=timeout).click()


@pytest.mark.parametrize('selector', SHOW_NAME_DICT.values(), ids=SHOW_NAME_DICT.keys())
def test_button_show(base_url: str, driver: webdriver, timeout: float, selector: str):
    driver.get(f'{base_url}{_URL_PAGES}')
    wait_element(selector, driver, timeout=timeout).click()


@pytest.mark.parametrize('selector', ('#list-view', '#grid-view'))
def test_display_table(base_url: str, driver: webdriver, timeout: float, selector: str):
    driver.get(f'{base_url}{_URL_PAGES}')
    wait_element(selector, driver, timeout=timeout).click()
