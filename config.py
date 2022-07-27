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


def create_new_list(list_of_dict, args):
    for dictionary in list_of_dict:
        for key in list(dictionary.keys()):
            if key not in args:
                del dictionary[key]
    return list_of_dict


USERS_ARGS = ['name', 'gender', 'address', 'age']
BOOKS_ARGS = ['Title', 'Author', 'Pages', 'Genre']
USERS_JSON = create_new_list(json_load_user(), USERS_ARGS)
BOOKS_JSON = create_new_list(csv_load_books(), BOOKS_ARGS)
PATH_JSON_RESULT = f'{root_project_path}/result.json'
