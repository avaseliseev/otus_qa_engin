import requests


def get_headers() -> dict:
    return {'Content-type': 'application/json; charset=UTF-8'}


def get_body(user_id: int, body: str, title: str) -> dict:
    return {
        'title': title,
        'body': body,
        'userId': user_id,
    }


def get_request(url: str, params=None):
    return requests.request('get', url=url, params=params)


def post_request(url: str, headers=None, data=None, json=None):
    return requests.request('post', url=url, headers=headers, data=data, json=json)


def put_request(url: str, headers=None, data=None, json=None):
    return requests.request('put', url=url, headers=headers, data=data, json=json)


def patch_request(url: str, headers=None, data=None, json=None):
    return requests.request('patch', url=url, headers=headers, data=data, json=json)


def delete_request(url: str, headers=None):
    return requests.request('delete', url=url, headers=headers)
