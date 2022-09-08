from selenium import webdriver
from service import wait_title, wait_element

_URL_PAGES = '/component'


def test_check_page_title(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{_URL_PAGES}')
    wait_title('Components', driver, timeout=timeout)
    wait_element('#content', driver, timeout=timeout)


def test_check_refine_search(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{_URL_PAGES}')
    assert wait_element('#content > h3', driver, timeout=timeout).text == 'Refine Search'
