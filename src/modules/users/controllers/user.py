from src.modules.users.domain.repositories import user as repository
from src.modules.users.domain.entities.user import User
from typing import Tuple


def save_user(requestBody: dict) -> Tuple[dict, int]:
    '''
    Logical process to save a user
    '''
    local_user: User = User(requestBody['name'],
                            requestBody['email'], requestBody['password'])
    try:
        return next(repository.save(local_user)), 200
    except StopIteration:
        return {'msj': 'Request has an error'}, 400
    except PermissionError:
        return {'msj': 'User Already exists'}, 403


def login(requestBody: dict) -> Tuple[dict, int]:
    '''
    Logical process to get a user
    '''
    try:
        user_dic: dict = next(repository.get_by_id(requestBody['email']))
    except StopIteration:
        return {'msj': 'User was not found'}, 404
    if user_dic['password'] != requestBody['password']:
        return {'msj': 'User or password were wrong'}, 403
    name: str = user_dic['name']
    email: str = user_dic['email']
    password: str = user_dic['password']
    token: str = f'{name}{email}{password}'
    user_dic_with_token: dict = dict()
    user_dic_with_token.update(user_dic)
    user_dic_with_token.update(token=token)
    return user_dic_with_token, 200


def getUser(email: str) -> Tuple[dict, int]:
    '''
    Get user by email
    '''
    try:
        return next(repository.get_by_id(email)), 200
    except StopIteration:
        return {'msj': 'User not found'}, 404


def updateUser(email: str, requestBody: dict) -> Tuple[dict, int]:
    '''
    Update user by email
    '''
    local_user: User = User(requestBody['name'], requestBody['email'], '')
    try:
        return next(repository.update(email, local_user)), 200
    except (StopIteration, FileNotFoundError):
        return {'msj': 'User not found'}, 404
