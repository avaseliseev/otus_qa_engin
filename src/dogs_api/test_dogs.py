import pytest

from src.dogs_api.conftest import get_hound_names, get_terrier_names
from src.utils.assertions import assert_response_dogs
from src.utils.req_sender import get_request


def test_get_random_image(base_url_dog: str):
    r = get_request(f'{base_url_dog}breeds/image/random')
    assert_response_dogs(r)


@pytest.mark.parametrize('breeds', get_hound_names())
def test_get_image_dogs_by_breed(base_url_dog: str, breeds: dict):
    r = get_request(f'{base_url_dog}breed/hound/{breeds}/images/random')
    assert_response_dogs(r)


def test_get_list_all_breeds(base_url_dog: str):
    r = get_request(f'{base_url_dog}breeds/list/all')
    assert_response_dogs(r)
    return r.json()['message']


@pytest.mark.parametrize('breeds', get_hound_names())
def test_check_hound(base_url_dog: str, breeds: dict):
    r = test_get_list_all_breeds(base_url_dog)
    assert breeds in r['hound']


def test_get_all_terrier_image(base_url_dog: str):
    r = get_request(f'{base_url_dog}breed/terrier/images')
    assert_response_dogs(r)


@pytest.mark.parametrize('breeds', get_terrier_names())
def test_check_terriers(base_url_dog: str, breeds: dict):
    r = test_get_list_all_breeds(base_url_dog)
    assert breeds in r['terrier']
