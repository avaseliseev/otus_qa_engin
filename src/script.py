import json

from config import PATH_JSON_RESULT, USERS_JSON, BOOKS_JSON


def add_books_users(users, books):
    for user in users:
        user['books'] = []

    counter = 0

    for book in books:
        users[counter]['books'].append(book)
        counter += 1
        if counter >= len(users):
            counter = 0
    return users


def write_json_result(users):
    with open(PATH_JSON_RESULT, 'w') as file:
        json.dump(users, file, indent=4)


write_json_result(add_books_users(USERS_JSON, BOOKS_JSON))
