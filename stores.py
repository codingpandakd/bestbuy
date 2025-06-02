from products import Product

class Store:
    def __init__(self, products):
        self._products = products
    def add_product(self, product):
        self._products.append(product)
    def remove_product(self, product):
        self._products.remove(product)
    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self._products)
    def get_all_products(self):
        return [product for product in self._products if product.is_active()]
    def list_products(self):
        for i, product in enumerate(self._products, start=1):
            print(f"{i}. {product.show()}")
    def order(self, shopping_list):
        total_payment = 0.0

        for product, quantity in shopping_list:
            if product not in self._products:
                raise ValueError(f"Product {product._name} is not available in the store.")
            if not product.is_active():
                raise ValueError(f"Product {product._name} is not active.")
            if quantity <= 0:
                raise ValueError("Quantity must be positive.")

            try:
                total_payment += product.buy(quantity)
            except Exception as e:
                print(f"Error purchasing {product._name}: {e}")

        return total_payment


