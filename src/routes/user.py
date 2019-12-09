from flask import request
from ..repository.user import User as repository
from ..models.users.user import User


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
        return repository.get_by_id(id='cruzortiz099@gmail.com')

    @app.route(f'{base_url}/logout', methods=['POST'])
    def logout():
        raise Exception('must implement this method')

    @app.route(f'{base_url}sign-in', methods=['POST'])
    def sign_in():
        user = User('Cruz', '123456', 'sdsdsa@gmail.com')
        raise repository.save(user)

    @app.route(f'{base_url}test', methods=['GET'])
    def test():
        user = User('Cruz', '123456', 'sdsdsa@gmail.com')
        return repository.save(user)
