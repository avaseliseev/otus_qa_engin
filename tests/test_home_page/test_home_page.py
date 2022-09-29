import pytest
from page_object.HomePage import HomePage


def test_check_page_title(run_driver_home_page: HomePage):
    home_page = run_driver_home_page
    home_page.waiting_title(home_page.TITLE)
    home_page.waiting_element(home_page.CSS_LOGO).click()


@pytest.mark.parametrize('name', ['apple', 'samsung', 'test', 'tab'])
def test_search_bar(run_driver_home_page: HomePage, name: str):
    home_page = run_driver_home_page
    home_page.input_search_bar(name)


@pytest.mark.parametrize('position', range(0, 4))
def test_click_random_product(run_driver_home_page: HomePage, position: int):
    home_page = run_driver_home_page
    home_page.click_on_the_specified_item(position)


@pytest.mark.parametrize('currency', ['EUR', 'GBR', 'US'])
def test_click_payment_unit(run_driver_home_page: HomePage, currency: str):
    home_page = run_driver_home_page
    home_page.input_currency(currency)


@pytest.mark.parametrize('param', ['Information', 'Customer Service', 'Extras', 'My Account'])
def test_check_footer(run_driver_home_page: HomePage, param: str):
    home_page = run_driver_home_page
    assert param in home_page.get_footer.text
