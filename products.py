class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()

    def is_active(self):
        return self._active

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def show(self):
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}"

    def buy(self, quantity):
        if not self._active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")
        if quantity > self._quantity:
            raise Exception("Insufficient quantity available.")

        total_price = quantity * self._price
        self.set_quantity(self._quantity - quantity)
        return total_price

# # Example usage:
# bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# mac = Product("MacBook Air M2", price=1450, quantity=100)
#
# print(bose.buy(50))
# print(mac.buy(100))
# print(mac.is_active())
#
# print(bose.show())
# print(mac.show())
# #
# bose.set_quantity(1000)
# print(bose.show())