from src.module_4.conftest import assert_response
from src.utils.req_sender import get_request


def test_get_url(base_url: str, status_code: int):
    r = get_request(base_url)
    assert_response(r, status_code)
