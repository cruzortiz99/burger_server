from .cobrable import Cobrable


class Ingrediente_Hamburguesa(Cobrable):
    def __init__(self, ingrediente, cantidad):
        '''
        Ingredientes por hamburguesa
        Parameters:
        ----
        - ingrediente: Ingrediente
        - cantidad: int
        '''
        self.ingrediente = ingrediente
        self.cantidad = cantidad

    @property
    def price(self):
        return self.ingrediente.price * self.cantidad
