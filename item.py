# base class for a store item

class Item:
    def __init__(self, name, quantity, old_price, price):
        self.name = name
        self.quantity = quantity
        self.old_price = old_price
        self.price = price

    def __str__(self):
        return "\nName: " + self.name + \
            "\nQuantity: " + str(self.quantity) + \
            "\nOld price: " + str(self.old_price) + \
            "\nPrice: " + str(self.price)

    def __repr__(self):
        return "\nName: " + self.name + \
            "\nQuantity: " + str(self.quantity) + \
            "\nOld price: " + str(self.old_price) + \
            "\nPrice: " + str(self.price)

    def get_discount_level(self):
        return self.price / self.old_price
