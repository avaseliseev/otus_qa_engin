from config import LOGIN, TELEPHONE, EMAIL, PASSWORD

_user_data = {
    'First Name': LOGIN,
    'Last Name': LOGIN,
    'input email': EMAIL,
    'input telephone': TELEPHONE

}
_user_pass = {
    'password': PASSWORD
}


def get_user_data() -> dict:
    return _user_data


def get_pass() -> dict:
    return _user_pass
