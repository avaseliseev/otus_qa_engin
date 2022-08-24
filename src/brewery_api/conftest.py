import pytest
import requests

CITY = ['Knox', 'Bend', 'Bend', 'Bend', 'Boise', 'Denver', 'Portland', 'San Diego', 'Reno', 'Quilcene', 'Petaluma',
        'Castle Rock', 'Anoka', 'Abington', 'Houston', 'John Day', 'Killeshin', 'Williamsville', 'Gilbert', 'Mesa']

TYPE = ['micro', 'nano', 'large', 'planning', 'bar', 'contract', 'proprieter', 'closed']


@pytest.fixture
def base_url_brewery() -> str:
    return 'https://api.openbrewerydb.org/breweries'


def get_all_brewery_id() -> list:
    r = requests.get('https://api.openbrewerydb.org/breweries/')
    return _list_id_brewery(r.json())


def _list_id_brewery(res_list_brewery) -> list:
    list_id = []
    for dict_brewery in res_list_brewery:
        for k, v in dict_brewery.items():
            if k == 'id':
                list_id.append(v)
    return list_id
