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


USERS_JSON = json_load_user()
BOOKS_JSON = csv_load_books()
PATH_JSON_RESULT = f'{root_project_path}/resources/reference.json'

