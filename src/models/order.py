class Order():
    def __init__(self, burgers):
        self.burgers = burgers

    def get_order_price(self):
        price = 0
        for burger in self.burgers:
            price += price + burger.price()
        return price
