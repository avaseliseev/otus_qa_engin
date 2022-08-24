import pytest


def pytest_addoption(parser):
    parser.addoption('--url', default='https://ya.ru', help='This is request url')
    parser.addoption('--status_code', default=200, help='This is response status')


@pytest.fixture
def base_url(pytestconfig) -> str:
    return pytestconfig.option.url


@pytest.fixture
def status_code(pytestconfig) -> int:
    return int(pytestconfig.option.status_code)


def assert_response(res, status_code):
    assert res.status_code == status_code
