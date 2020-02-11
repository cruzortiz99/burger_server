from json import load, dump
from pathlib import Path
from src.modules.users.domain.entities.user import User
from typing import Any, List, Iterable

path = Path(__file__).parent.joinpath(
    '..', '..', '..', '..', 'db', 'user.json')


def save(user: User) -> Iterable:
    '''
    Saves user in db
    '''
    json_file = open(path, 'r', encoding='utf-8')
    json_users: Any = load(json_file)
    json_file.close()
    exists: bool = len([json_user for json_user in json_users if json_user['email']
                        == user.email]) > 0
    if exists:
        raise PermissionError("User already on db")
    else:
        json_users.append(user.__dict__)
    json_file = open(path, 'w', encoding='utf-8')
    dump(json_users, fp=json_file)
    json_file.close()
    return (json_user for json_user in json_users
            if json_user['email'] == user.email)


def get_by_id(id: str) -> Iterable:
    '''
    Get user by email
    '''
    json_file = open(path, 'r', encoding='utf-8')
    json_users: Any = load(json_file)
    json_file.close()
    return (user for user in json_users if user['email'] == id)


def update(email: str, user: User) -> Iterable:
    '''
    Updates user by email
    '''
    json_file = open(path, 'r', encoding='utf-8')
    json_users: Any = load(json_file)
    json_file.close()
    users_with_same_email: List[dict] = [
        json_user for json_user in json_users if json_user['email'] == email]
    exists: bool = len(users_with_same_email) > 0
    if exists is False:
        raise FileNotFoundError('user doesn\'t exists')
    for user_find in users_with_same_email:
        user_find['name'] = user.name
    json_file = open(path, 'w', encoding='utf-8')
    dump(json_users, fp=json_file)
    json_file.close()
    return (json_user for json_user in json_users if json_user['email']
            == email)
