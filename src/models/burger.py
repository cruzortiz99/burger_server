from .cobrable import Cobrable


class Burger(Cobrable):
    def __init__(self, ingredientes):
        '''
        Build the burger
        Parameters:
        ----
        - ingredientes: Ingredientes_Hamburguesa[]
        '''
        self.ingredientes = ingredientes

    @property
    def price(self):
        price = 0
        for ingrediente in self.ingredientes:
            price += ingrediente.price
        return price
