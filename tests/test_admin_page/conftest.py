import pytest
from selenium import webdriver

from config import URL_ADMIN_PAGE
from page_object.AdminPage import AdminPage


@pytest.fixture
def run_driver_admin_page(base_url: str, _get_path: str, driver: webdriver, timeout: float) -> AdminPage:
    admin_page = AdminPage(driver)
    admin_page.open_browser(base_url=base_url, driver=driver, path=_get_path)
    return admin_page


@pytest.fixture
def _get_path() -> str:
    return URL_ADMIN_PAGE


@pytest.fixture
def data_for_page_general() -> dict:
    return {'product_name': ['Mobile', '[id=input-name1]'],
            'description': ['Test product', '[role=textbox]'],
            'mega_tag_title': ['Super mobile', '[id*=title1]'],
            'product_tag': ['test', '[id*=tag1]']
            }


@pytest.fixture
def data_for_page_data() -> dict:
    return {'model': ['t1000', '[id*=model]'],
            'price': ['5555', '[id*=price]']
            }


@pytest.fixture
def check_title(timeout: float) -> tuple:
    return 'Administration', timeout
