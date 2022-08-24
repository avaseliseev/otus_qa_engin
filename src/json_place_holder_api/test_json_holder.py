import pytest

from src.json_place_holder_api.conftest import get_all_resources, post_resource
from src.utils.assertions import assert_response_brew_hold, assert_response_created, assert_response_delete
from src.utils.req_sender import patch_request, delete_request, get_request
from src.utils.utils import generate_list_numbers


def test_get_all_resources(base_url_json_pl_hl):
    r = get_all_resources()
    assert_response_brew_hold(r)


@pytest.mark.parametrize('user_id', generate_list_numbers(1, 25))
def test_get_resources_by_id(user_id: list):
    r = get_all_resources(user_id)
    assert_response_brew_hold(r)


@pytest.mark.parametrize('user_id, body, title',
                         [(5, 'binding', 'constipate'),
                          (6, 'cushion', 'assemble'),
                          (7, 'coble', 'boggle'),
                          (8, 'coming', 'dispeople'),
                          (9, 'desolation', 'enhance'),
                          (10, 'odio', 'unique'),
                          (11, 'skinny', 'snobbish'),
                          (12, 'light', 'wandering')])
def test_post_resources(user_id: int, body: str, title: str):
    r = post_resource(user_id=user_id, body=body, title=title)
    assert_response_created(r)


@pytest.mark.parametrize('id, title',
                         [(2, 'tough'),
                          (3, 'smart'),
                          (15, 'amusing'),
                          (9, 'functional'),
                          (8, 'old-fashioned'),
                          (3, 'wistful'),
                          (20, 'impressive'),
                          (12, 'draconian')])
def test_update_resources(base_url_json_pl_hl: str, id: int, title: str):
    dict_json = {'title': title}
    r = patch_request(f'{base_url_json_pl_hl}/{id}', json=dict_json)
    assert_response_brew_hold(r)


@pytest.mark.parametrize('id', generate_list_numbers(5, 13))
def test_deleting_resources(base_url_json_pl_hl: str, id: list):
    r = delete_request(f'{base_url_json_pl_hl}/{id}')
    assert_response_delete(r)


@pytest.mark.parametrize('user_id', generate_list_numbers(1, 11))
def test_get_posts_users(base_url_json_pl_hl: str, user_id: list):
    param = {'userId': user_id}
    r = get_request(url=base_url_json_pl_hl, params=param)
    assert_response_brew_hold(r)
