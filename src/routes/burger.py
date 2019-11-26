from flask import request


def burger_routes(app):
    '''
    Burger routes
    - app: Flask object

    * post:/burger
    * get:/burger
    * get:/burger/{id}
    '''
    base_url = '/burger'
    @app.route(f'{base_url}', methods=['POST'])
    def new_burger():
        raise Exception("must implement this method")

    @app.route(f'{base_url}', methods=['GET'])
    def get_burgers():
        raise Exception("must implement this method")

    @app.route(f'{base_url}/<int:burger>')
    def get_burger(burger):
        raise Exception("must implement this method")

    @app.route(f'{base_url}/test', methods=['GET'])
    def test():
        return '<h1>New Burger</h1>'
