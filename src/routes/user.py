from flask import request, make_response
from ..domain.entities.users.user import User
from ..controllers import user as user_controller
from numbers import Number
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

    @app.route(f'{base_url}login', methods=['POST'])
    def login():
        controller_response = user_controller.login(json.loads(request.data))
        response = controller_response[0]
        status = controller_response[1]
        response = make_response(response, status)
        response.headers['Content-Type'] = 'applicaiton/json'
        return response

    @app.route(f'{base_url}logout', methods=['POST'])
    def logout():
        return true

    @app.route(f'{base_url}sign-in', methods=['POST'])
    def sign_in():
        return user_controller.save_user(json.loads(request.data))

    @app.route(f'{base_url}test', methods=['GET'])
    def test():
        user = User('Cruz Ortiz', 'example@example.com', '123456')
        return user_controller.save_user(user)
