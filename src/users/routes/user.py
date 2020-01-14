from flask import Blueprint, request, make_response
from src.users.domain.entities.user import User
from src.users.controllers import user as user_controller
from src.utils.cors import add_cors_to_response, cors_preflight_response
from numbers import Number
import json

router = Blueprint('user', __name__)


@router.route('login', methods=['POST', 'OPTIONS'])
def login():
    '''
    Login method
    ----
    Return:
    ----
    - response object
    '''
    if request.method.upper() == 'OPTIONS'.upper():
        return cors_preflight_response()
    controller_response = user_controller.login(json.loads(request.data))
    response = make_response(
        controller_response[0], controller_response[1])
    response.headers['Content-Type'] = 'applicaiton/json'
    return add_cors_to_response(response)


@router.route('logout', methods=['POST', 'OPTIONS'])
def logout():
    '''
    Logout function
    ----
    Return:
    ----
    - response object
    '''
    if request.method.upper() == 'OPTIONS'.upper():
        return cors_preflight_response()
    return add_cors_to_response(make_response(True, 200))


@router.route('sign-in', methods=['POST', 'OPTIONS'])
def sign_in():
    '''
    Registration process
    ----
    Return:
    ----
    - response object
    '''
    if request.method.upper() == 'OPTIONS'.upper():
        return cors_preflight_response()
    controller_response = user_controller.save_user(
        json.loads(request.data))
    response = make_response(
        controller_response[0], controller_response[1])
    response.headers["Content-Type"] = "application/json"
    return add_cors_to_response(response)


@router.route('user/<email>', methods=['GET', 'OPTIONS'])
def getUser(email):
    '''
    Get one user by email
    ----
    Parameters:
    ----
    - email: str, identifier of the user
    Return:
    ----
    - response object
    '''
    if request.method.upper() == 'OPTIONS'.upper():
        return cors_preflight_response()
    controller_response = user_controller.getUser(email)
    response = make_response(
        controller_response[0], controller_response[1])
    return add_cors_to_response(response)


@router.route('user/<email>', methods=['POST', 'OPTIONS'])
def updateUser(email):
    '''
    Update user, by email
    ----
    Parameters:
    ----
    - email: str, email of the user
    Return:
    ----
    - response object
    '''
    if request.method.upper() == 'OPTIONS'.upper():
        return cors_preflight_response()
    controller_response = user_controller.updateUser(
        email, json.loads(request.data))
    response = make_response(controller_response)
    return add_cors_to_response(response)


@router.route('test', methods=['GET', 'OPTIONS'])
def test():
    '''
    Test api method
    '''
    if request.method.upper() == 'options'.upper():
        return cors_preflight_response()
    user = User('Cruz Ortiz', 'example@example.com', '123456')
    controller_response = user_controller.save_user(user.__dict__)
    response = make_response(
        controller_response[0], controller_response[1])
    return add_cors_to_response(response)
