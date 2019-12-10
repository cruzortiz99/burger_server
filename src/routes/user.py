from flask import request
from ..domain.entities.users.user import User
from ..controllers import user as user_controller


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

    @app.route(f'{base_url}/login', methods=['POST'])
    def login():
        return user_controller.get_by_id('cruzortiz099@gmail.com')

    @app.route(f'{base_url}/logout', methods=['POST'])
    def logout():
        return true

    @app.route(f'{base_url}sign-in', methods=['POST'])
    def sign_in():
        return user_controller.save_user(user)

    @app.route(f'{base_url}test', methods=['GET'])
    def test():
        return user_controller.save_user(user)
