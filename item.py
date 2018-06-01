# base class for a store item

class Item:
    def __init__(self, name, quantity, price, discount_factor):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount_factor = discount_factor

    def __str__(self):
        return "\nName: " + self.name + \
            "\nQuantity: " + str(self.quantity) + \
            "\nPrice: " + str(self.price) + \
            "\nDiscount factor: " + str(self.discount_factor)

    def __repr__(self):
        return "\nName: " + self.name + \
            "\nQuantity: " + str(self.quantity) + \
            "\nPrice: " + str(self.price) + \
            "\nDiscount factor: " + str(self.discount_factor)
