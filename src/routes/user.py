from flask import request, make_response
from ..domain.entities.users.user import User
from ..controllers import user as user_controller
from numbers import Number
from .cors import add_cors_to_response, cors_preflight_response
import json


def user_routes(app):
    '''
    User routes
    - post:/login
    - post:/logout

    Parameters
    ----
    - app: Flask object
    '''
    base_url = '/'

    @app.route(f'{base_url}login', methods=['POST', 'OPTIONS'])
    def login():
        if request.method.upper() == 'OPTIONS'.upper():
            return cors_preflight_response()
        controller_response = user_controller.login(json.loads(request.data))
        response = make_response(
            controller_response[0], controller_response[1])
        response.headers['Content-Type'] = 'applicaiton/json'
        return add_cors_to_response(response)

    @app.route(f'{base_url}logout', methods=['POST', 'OPTIONS'])
    def logout():
        if request.method.upper() == 'OPTIONS'.upper():
            return cors_preflight_response()
        return add_cors_to_response(make_response(True, 200))

    @app.route(f'{base_url}sign-in', methods=['POST', 'OPTIONS'])
    def sign_in():
        if request.method.upper() == 'OPTIONS'.upper():
            return cors_preflight_response()
        controller_response = user_controller.save_user(
            json.loads(request.data))
        response = make_response(
            controller_response[0], controller_response[1])
        response.headers["Content-Type"] = "application/json"
        return add_cors_to_response(response)

    @app.route(f'{base_url}test', methods=['GET', 'OPTIONS'])
    def test():
        if request.method.upper() == 'options'.upper():
            return cors_preflight_response()
        user = User('Cruz Ortiz', 'example@example.com', '123456')
        response = make_response(user_controller.save_user(user), 200)
        return add_cors_to_response(response)
