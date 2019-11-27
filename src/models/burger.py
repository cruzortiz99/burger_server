class Burger():
    def __init__(self, **kwargs):
        self.nro_carnes = kwargs['nro_carnes']
        self.nro_tocineta = kwargs['nro_tocineta']
        self.nro_queso = kwargs['nro_queso']
        self.nro_jamon = kwargs['nro_jamon']
        self.nro_pollo = kwargs['nro_pollo']
        self.nro_chuleta = kwargs['nro_chuleta']
        pass

    def price(self):
        price = (self.nro_carnes*1) + (self.nro_tocineta*1) + (self.nro_queso*1) + \
            (self.nro_jamon*1) + (self.nro_pollo*1) + (self.nro_chuleta*1)
        return price
