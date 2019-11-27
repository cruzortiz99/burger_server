from flask import request


def user_routes(app):
    '''
    User routes
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
        return '<h1>Hola Mundo</h1>'
