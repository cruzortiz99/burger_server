from flask import Blueprint, request, make_response, Response
from src.modules.users.domain.entities.user import User
from src.modules.users.controllers import user as user_controller
from src.utils.cors import add_cors_to_response, cors_preflight_response
from numbers import Number
from typing import Tuple
import json

router: Blueprint = Blueprint('user', __name__)


@router.route('login', methods=['POST', 'OPTIONS'])
def login() -> Response:
    '''
    Login method
    '''
    if request.method.upper() == 'OPTIONS'.upper():
        return cors_preflight_response()
    controller_response: Tuple[dict, int] = user_controller.login(
        json.loads(request.data))
    response: Response = make_response(
        controller_response[0], controller_response[1])
    response.headers['Content-Type'] = 'applicaiton/json'
    return add_cors_to_response(response)


@router.route('logout', methods=['POST', 'OPTIONS'])
def logout() -> Response:
    '''
    Logout function
    '''
    if request.method.upper() == 'OPTIONS'.upper():
        return cors_preflight_response()
    return add_cors_to_response(make_response(True, 200))


@router.route('sign-in', methods=['POST', 'OPTIONS'])
def sign_in() -> Response:
    '''
    Registration process
    '''
    if request.method.upper() == 'OPTIONS'.upper():
        return cors_preflight_response()
    controller_response: Tuple[dict, int] = user_controller.save_user(
        json.loads(request.data))
    response: Response = make_response(
        controller_response[0], controller_response[1])
    response.headers["Content-Type"] = "application/json"
    return add_cors_to_response(response)


@router.route('user/<email>', methods=['GET', 'OPTIONS'])
def getUser(email: str) -> Response:
    '''
    Get one user by email
    '''
    if request.method.upper() == 'OPTIONS'.upper():
        return cors_preflight_response()
    controller_response: Tuple[dict, int] = user_controller.getUser(email)
    response: Response = make_response(
        controller_response[0], controller_response[1])
    return add_cors_to_response(response)


@router.route('user/<email>', methods=['POST', 'OPTIONS'])
def updateUser(email: str) -> Response:
    '''
    Update user, by email
    '''
    if request.method.upper() == 'OPTIONS'.upper():
        return cors_preflight_response()
    controller_response: Tuple[dict, int] = user_controller.updateUser(
        email, json.loads(request.data))
    response: Response = make_response(controller_response)
    return add_cors_to_response(response)


@router.route('test', methods=['GET', 'OPTIONS'])
def test() -> Response:
    '''
    Test api method
    '''
    if request.method.upper() == 'options'.upper():
        return cors_preflight_response()
    user: User = User('Cruz Ortiz', 'example@example.com', '123456')
    controller_response: Tuple[dict,
                               int] = user_controller.save_user(user.__dict__)
    response: Response = make_response(
        controller_response[0], controller_response[1])
    return add_cors_to_response(response)
