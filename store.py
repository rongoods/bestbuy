from products import Product


class Store:
    """ Keeps track of the list products in the store
        Adding products
        Removing products
        Displaying the total quantities"""

    def __init__(self, products):
        """Initializes the store with a list of products"""
        self.products = products

    def add_product(self, product):
        """Adds a new product to the inventory"""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the inventory"""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products"""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """Returns all active products in inventory"""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        """ Process the total cost of the order and returns a float
         Updates the quantity of products after the order """
        total_cost = 0.0
        for product, quantity in shopping_list:
            total_cost += product.buy(quantity)
        return total_cost
