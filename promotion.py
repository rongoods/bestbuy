from abc import ABC, abstractmethod


class Promotion(ABC):
    """ Making an Abstract Base Class for all promotions """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """ Calculates the discount after checking the quantity """
        pass


class PercentDiscount(Promotion):
    """ Applies the calculated percentage (Promotion) to the price"""

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        discount = (self.percent / 100) * product.price
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    """ Calculates the 50% off promotion for the second item """

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        full_price_quantity = quantity // 2 + quantity % 2
        half_price_quantity = quantity // 2
        return (full_price_quantity * product.price) + (half_price_quantity * product.price * 0.5)


class ThirdOneFree(Promotion):
    """ Calculates the free third item promotion for the third item """

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        paid_items = quantity - (quantity // 3)
        return paid_items * product.price
