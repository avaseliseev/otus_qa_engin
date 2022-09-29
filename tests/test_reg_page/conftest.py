import pytest
from selenium import webdriver

from config import URL_REGISTR_PAGE
from page_object.RegPage import RegPage


@pytest.fixture
def run_driver_reg_page(base_url: str, _get_path: str, driver: webdriver, timeout: float) -> RegPage:
    reg_page = RegPage(driver, path=_get_path)
    reg_page.open_browser(base_url=base_url, driver=driver, path=_get_path)
    return reg_page


@pytest.fixture
def _get_path() -> str:
    return URL_REGISTR_PAGE
