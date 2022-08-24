import pytest

from src.brewery_api.conftest import get_all_brewery_id, CITY, TYPE
from src.utils.assertions import assert_response_brew_hold
from src.utils.req_sender import get_request
from src.utils.utils import generate_list_numbers


def test_get_all_brewery(base_url_brewery: str):
    r = get_request(f'{base_url_brewery}')
    assert_response_brew_hold(r)


@pytest.mark.parametrize('id_brewery', get_all_brewery_id())
def test_get_single_brewery(base_url_brewery: str, id_brewery):
    r = get_request(f'{base_url_brewery}/{id_brewery}')
    assert_response_brew_hold(r)


@pytest.mark.parametrize('count', generate_list_numbers(1, 15))
def test_get_list_breweries(base_url_brewery: str, count):
    r = get_request(f'{base_url_brewery}', params={'per_page': count})
    assert_response_brew_hold(r)
    assert count == len(r.json())


@pytest.mark.parametrize('city', CITY)
def test_get_list_breweries_by_city(base_url_brewery: str, city):
    r = get_request(f'{base_url_brewery}', params={'by_city': city})
    assert_response_brew_hold(r)


@pytest.mark.parametrize('type_brewery', TYPE)
def test_get_list_breweries_by_type(base_url_brewery: str, type_brewery):
    r = get_request(f'{base_url_brewery}', params={'by_type': type_brewery})
    assert_response_brew_hold(r)


def test_get_random_brewery(base_url_brewery: str):
    r = get_request(f'{base_url_brewery}/random')
    assert_response_brew_hold(r)
