from flask import request


def burger_routes(app):
    '''
    Burger routes

    - post:/burger
    - get:/burger
    - get:/burger/{id}

    Parameters
    ----

    - app: Flask object

    '''
    base_url = '/burger'

    @app.route(f'{base_url}', methods=['POST'])
    def new_burger():
        raise Exception("must implement this method")

    @app.route(f'{base_url}', methods=['GET'])
    def get_burgers():
        raise Exception("must implement this method")

    @app.route(f'{base_url}/<int:burger>', methods=['GET'])
    def get_burger(burger):
        raise Exception("must implement this method")

    @app.route(f'{base_url}/test', methods=['GET'])
    def test_burger():
        return '<h1>New Burger</h1>'
