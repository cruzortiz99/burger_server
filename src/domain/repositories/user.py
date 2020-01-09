from json import load, dump
from pathlib import Path


path = Path(__file__).parent.joinpath('..', '..', 'db', 'user.json')


def save(user):
    json_file = open(path, 'r', encoding='utf-8')
    json_users = load(json_file)
    json_file.close()
    exists = len([json_user for json_user in json_users if json_user['email']
                  == user.email]) > 0
    if exists:
        for json_user in json_users:
            if json_user['email'] == user.email:
                json_user['name'] = user.name
                json_user['password'] = user.password
    else:
        json_users.append(user.__dict__)
    json_file = open(path, 'w', encoding='utf-8')
    dump(json_users, fp=json_file)
    json_file.close()
    return (json_user for json_user in json_users
            if json_user['email'] == user.email)


def get_by_id(id):
    json_file = open(path, 'r', encoding='utf-8')
    json_users = load(json_file)
    json_file.close()
    return (user for user in json_users if user['email'] == id)
