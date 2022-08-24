import pytest

from src.utils.req_sender import get_request, post_request, get_headers, get_body


@pytest.fixture
def base_url_json_pl_hl() -> str:
    return 'https://jsonplaceholder.typicode.com/posts'


def get_all_resources(id=''):
    r = get_request(url=f'https://jsonplaceholder.typicode.com/posts/{id}')
    return r


def post_resource(user_id: int, body: str, title: str):
    headers = get_headers()
    json_body = get_body(user_id=user_id, body=body, title=title)
    r = post_request(url='https://jsonplaceholder.typicode.com/posts', headers=headers, json=json_body)
    return r
