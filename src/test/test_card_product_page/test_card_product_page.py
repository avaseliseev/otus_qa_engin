import random

from selenium import webdriver

from config import URL_CARD_PRODUCT, LOGIN
from service import wait_element


def test_check_name_product(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{URL_CARD_PRODUCT}')
    _element_in_header = wait_element('.breadcrumb > li:nth-child(4) > a', driver, timeout=timeout)
    _element_in_right_bar = wait_element('div.col-sm-4:nth-child(2) > h1', driver, timeout=timeout)
    assert _element_in_header.text == 'iMac'
    assert _element_in_right_bar.text == 'iMac'


def test_check_description(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{URL_CARD_PRODUCT}')
    wait_element('li.active > a', driver, timeout=timeout)
    wait_element('#tab-description.active', driver, timeout=timeout)


def test_post_review(base_url: str, driver: webdriver, timeout: float):
    _text = 'Very nice!!!!!' * 10
    driver.get(f'{base_url}{URL_CARD_PRODUCT}')
    wait_element('ul.nav:nth-child(2) > li:nth-child(2) > a', driver, timeout=timeout).click()
    wait_element('#input-name', driver, timeout=timeout).send_keys(LOGIN)
    wait_element('#input-review', driver, timeout=timeout).send_keys(_text)
    wait_element('div.form-group:nth-child(5) > div:nth-child(1) > input:nth-child(6)', driver, timeout=timeout).click()
    wait_element('#button-review.btn-primary', driver, timeout=timeout).click()
    wait_element('.alert-success', driver, timeout=timeout)


def test_click_image(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{URL_CARD_PRODUCT}')
    wait_element('.thumbnails > li:nth-child(1) > a:nth-child(1) > img', driver, timeout=timeout).click()
    wait_element('button.mfp-arrow:nth-child(4)', driver, timeout=timeout).click()
    wait_element('button.mfp-arrow:nth-child(3)', driver, timeout=timeout).click()
    wait_element('.mfp-close', driver, timeout=timeout).click()


def test_check_tax_product(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{URL_CARD_PRODUCT}')
    wait_element('li h2', driver, timeout=timeout)
    wait_element('div.col-sm-4:nth-child(2) > ul:nth-child(4) > li:nth-child(2)', driver, timeout=timeout)


def test_product_add_basket(base_url: str, driver: webdriver, timeout: float):
    driver.get(f'{base_url}{URL_CARD_PRODUCT}')
    wait_element('#input-quantity', driver, timeout=timeout).send_keys(random.randint(1, 10))
    wait_element('#button-cart', driver, timeout=timeout).click()
    wait_element('.alert.alert-success', driver, timeout=timeout)

