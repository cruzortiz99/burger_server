from flask import request

from ..models.burger import Burger
from ..models.ingrediente import Ingrediente
from ..models.ingrediente_hamburgesa import Ingrediente_Hamburguesa


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
        ingrediente = Ingrediente('Carne', 50)
        ingrediente_hamburguesa = Ingrediente_Hamburguesa(ingrediente, 2)
        burger = Burger([ingrediente_hamburguesa])
        print(burger.__dict__, burger.price)
        return '<h1>New Burger</h1>'
