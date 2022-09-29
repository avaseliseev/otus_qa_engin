import pytest
from selenium import webdriver

from config import URL_DESKTOP_PAGE
from page_object.CatalogPage import CatalogPage


@pytest.fixture
def run_driver_catalog_page(base_url: str, _get_path: str, driver: webdriver, timeout: float) -> CatalogPage:
    catalog_page = CatalogPage(driver, path=_get_path)
    catalog_page.open_browser(base_url=base_url, driver=driver, path=_get_path)
    return catalog_page


@pytest.fixture
def _get_path() -> str:
    return URL_DESKTOP_PAGE


@pytest.fixture
def dict_of_sorting_elements():
    return {
        'Default': 'option:nth-of-type(1)',
        'Name (A - Z)': 'option:nth-of-type(2)',
        'Name (Z - A)': 'option:nth-of-type(3)',
        'Price (Low > High)': 'option:nth-of-type(4)',
        'Price (High > Low)': 'option:nth-of-type(5)',
        'Rating (Highest)': 'option:nth-of-type(6)',
        'Rating (Lowest)': 'option:nth-of-type(7)',
        'Model (A - Z)': 'option:nth-of-type(8)',
        'Model (Z - A)': 'option:nth-of-type(9)'
    }


@pytest.fixture
def dict_of_show_elements():
    return {
        'show 15': '[value*="limit=15"]',
        'show 25': '[value*="limit=25"]',
        'show 50': '[value*="limit=50"]',
        'show 75': '[value*="limit=75"]',
        'show 100': '[value*="limit=100"]'
    }


@pytest.fixture
def dict_view_elements():
    return {
        'list-view': '#list-view',
        'grid-view': '#grid-view'
    }
