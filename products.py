from promotion import Promotion, PercentDiscount, SecondHalfPrice, ThirdOneFree

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
        self.promotion = None

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

    def get_promotion(self) -> Promotion:
        """ Returns the promotion if it qualifies """
        return self.promotion

    def set_promotion(self, promotion: Promotion):
        """ Assigns the promotion to the product """
        self.promotion = promotion

    def show(self) -> str:
        """Returns a string showing the products name, price and quantity / if a promotion applies the promotion """
        if self.promotion:
            promotion_announcement = f"Promotion: {self.promotion.name}"
        else:
            promotion_announcement = ""
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

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    """ These products are not physical so the quantities are not tracked. """
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        self.quantity = 0 # Quantity set to 0 because products are not physical

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("You must purchase a product to continue.")
        return self.price * quantity

    def show(self) -> str:
        """ Show that the product is not in stock. """
        return f"{self.name} is not in stock."

class LimitedProduct(Product):
    """ Products that can be purchased a maximum amount of times. """
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity) -> float:
        """ Raises ValueError is the maximum quantity is reached. """
        if quantity > self.maximum:
            raise ValueError(f"Maximum amount that can be ordered for this item is {self.maximum}.")
        return super().buy(quantity)

    def show(self) -> str:
        """ Show the maximum limit for the Limited Product """
        return f"{self.name} has a max limit order or {self.maximum} per order, Price: {self.price}, Quantity: {self.quantity}."
