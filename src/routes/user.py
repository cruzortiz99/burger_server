from flask import request
from ..repository.user import User


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
        raise Exception('must implement this method')

    @app.route(f'{base_url}/logout', methods=['POST'])
    def logout():
        raise Exception('must implement this method')

    @app.route(f'{base_url}test', methods=['GET'])
    def test():
        user = User('Cruz', '123456', 'sdsdsa@gmail.com')
        user.save()
        return '<h1>Hola Mundo</h1>'
