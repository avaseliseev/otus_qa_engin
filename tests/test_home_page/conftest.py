import pytest
from selenium import webdriver

from page_object.HomePage import HomePage


@pytest.fixture
def run_driver_home_page(base_url: str, driver: webdriver, timeout: float) -> HomePage:
    home_page = HomePage(driver)
    home_page.open_browser(base_url=base_url, driver=driver)
    return home_page
