import json
from csv import DictReader
from pathlib import Path

root_project_path = str(Path(__file__).parent)


def json_load_user():
    with open(f'{root_project_path}/resources/users.json', 'r') as file:
        return json.load(file)


def csv_load_books():
    with open(f'{root_project_path}/resources/books.csv', newline='') as f:
        reader = DictReader(f)
        return [row for row in reader]


def create_new_list_users(users_list):
    for user in users_list:
        for key in list(user.keys()):
            if key not in ['name', 'gender', 'address', 'age']:
                del user[key]
    return users_list


def create_new_list_books(books_list):
    for book in books_list:
        for key in list(book.keys()):
            if key not in ['Title', 'Author', 'Pages', 'Genre']:
                del book[key]
    return books_list


USERS_JSON = create_new_list_users(json_load_user())
BOOKS_JSON = create_new_list_books(csv_load_books())
PATH_JSON_RESULT = f'{root_project_path}/result.json'
