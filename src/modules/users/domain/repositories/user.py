from json import load, dump
from pathlib import Path


path = Path(__file__).parent.joinpath(
    '..', '..', '..', '..', 'db', 'user.json')


def save(user):
    '''
    Saves user in db
    ----
    Params:
    ----
    :param User user: user to save

    Return:
    ----
    :return generator: users saved
    '''
    json_file = open(path, 'r', encoding='utf-8')
    json_users = load(json_file)
    json_file.close()
    exists = len([json_user for json_user in json_users if json_user['email']
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


def get_by_id(id):
    '''
    Get user by email
    ----
    Parameters:
    ----
    :param str id: email of the user
    Return:
    :return generator: users with the same email
    '''
    json_file = open(path, 'r', encoding='utf-8')
    json_users = load(json_file)
    json_file.close()
    return (user for user in json_users if user['email'] == id)


def update(email, user):
    '''
    Updates user by email
    ----
    Parameters:
    ----
    :param str email: user email

    :param User user: user model

    Return:
    ----
    :return generator: with user updated
    '''
    json_file = open(path, 'r', encoding='utf-8')
    json_users = load(json_file)
    json_file.close()
    users_with_same_email = [
        json_user for json_user in json_users if json_user['email'] == email]
    exists = len(users_with_same_email) > 0
    if exists is False:
        raise FileNotFoundError('user doesn\'t exists')
    for user_find in users_with_same_email:
        user_find['name'] = user.name
    json_file = open(path, 'w', encoding='utf-8')
    dump(json_users, fp=json_file)
    json_file.close()
    return (json_user for json_user in json_users if json_user['email']
            == email)
