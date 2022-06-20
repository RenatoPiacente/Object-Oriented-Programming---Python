class Item:
    discount_rate = 0.8 # The pay rate after 20% discount.

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >=0, f'Price {price} is not greater or equal to zero!'
        assert quantity >=0, f'Quantity {quantity} is not greater or equal to zero!'
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    

    def apply_discount(self):
        self.price *= self.discount_rate


item_1 = Item('Phone', 100, 1)
item_2 = Item('Laptop', 1000, 3)
item_3 = Item('Cabe', 10, 5)
item_4 = Item('Mouse', 50, 5)
item_5 = Item('Keyboard', 75, 5)
