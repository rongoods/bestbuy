class Product:
    """ Displays the products available in the store. """
    def __init__(self, name: str, price: float, quantity: int):
        """ Initializes a new Product """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid Value")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """Returns a float of the quantity of the product"""
        return self.quantity

    def set_quantity(self, quantity):
        """Updates the quantity of the product and if the quantity is 0
            it will deactivate said product"""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Verifies if the product is active and returns a boolean"""
        return self.active

    def activate(self):
        """Sets product active"""
        self.active = True

    def deactivate(self):
        """" Sets product to inactive"""
        self.active = False

    def show(self) -> str:
        """Returns a string showing the products name, price and quantity"""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """Tracks the quantity of the product and returns the total price
            and handles and errors if the product isn't available or not active. """
        if quantity <= 0:
            raise ValueError("You must purchase a product to continue.")
        if quantity > self.quantity:
            raise ValueError("Error adding product!")
        if not self.active:
            raise Exception("Product is not currently (active) available for purchase.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price