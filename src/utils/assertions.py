from http import HTTPStatus


def assert_response_dogs(res):
    assert res.status_code == HTTPStatus.OK
    assert 'message' in res.json()
    assert res.json()['status'] == 'success'


def _expected_params(res, url):
    if 'brewery' in url:
        params = ['name', 'city', 'state', 'country', 'created_at']
    else:
        params = ['userId', 'id', 'title', 'body']
    for param in params:
        assert param in res


def _check_is_list(res):
    if isinstance(res.json(), list):
        for dict_res in res.json():
            _expected_params(dict_res, res.url)
    else:
        _expected_params(res.json(), res.url)


def assert_response_brew_hold(res):
    assert res.status_code == HTTPStatus.OK
    _check_is_list(res)


def assert_response_created(res):
    assert res.status_code == HTTPStatus.CREATED
    _check_is_list(res)


def assert_response_delete(res):
    assert res.status_code == HTTPStatus.OK
    assert len(res.json()) == 0
