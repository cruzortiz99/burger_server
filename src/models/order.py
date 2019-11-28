from models.cobrable import Cobrable


class Order(Cobrable):
    '''
    Client order
    Parameters:
    ----
    - burgers: Burger[]
    - client: str
    '''
    _last_nro = 0

    def __init__(self, burgers, client):
        self.nro = Order._last_nro + 1
        Order._last_nro = self.nro
        self.burgers = burgers
        self.client = client

    @property
    def price(self):
        price = 0
        for burger in self.burgers:
            price += burger.price
        return price
