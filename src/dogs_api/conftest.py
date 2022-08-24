import pytest
import requests


@pytest.fixture
def base_url_dog() -> str:
    return 'https://dog.ceo/api/'


def get_hound_names() -> dict:
    r = requests.get('https://dog.ceo/api/breed/hound/list')
    return r.json()['message']


def get_terrier_names() -> dict:
    r = requests.get('https://dog.ceo/api/breed/terrier/list')
    return r.json()['message']
