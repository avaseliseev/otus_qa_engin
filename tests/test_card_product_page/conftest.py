import pytest
from selenium import webdriver

from config import URL_CARD_PRODUCT
from page_object.CardProductPage import CardProductPage


@pytest.fixture
def run_driver_card_page(base_url: str, _get_path: str, driver: webdriver, timeout: float) -> CardProductPage:
    card_product_page = CardProductPage(driver)
    card_product_page.open_browser(base_url=base_url, driver=driver, path=_get_path)
    return card_product_page


@pytest.fixture
def _get_path() -> str:
    return URL_CARD_PRODUCT


@pytest.fixture
def name_product() -> str:
    return 'iMac'


@pytest.fixture
def text_for_review() -> str:
    return 'Very nice!!!!!' * 10
