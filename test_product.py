import pytest
from products import Product

def test_create_product():
    """ Test that when a product is created with valid inputs everything works. """
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() is True

def test_creating_product_with_invalid_details():
    """ Test that when a product is created with an invalid name or price it raises an error. """
    with pytest.raises(ValueError):
        # Empty name
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError):
        # Negative Price
        Product("MacBook Air M2", price=-10, quantity=100)

def test_product_with_zero_quantity_is_inactive():
    """ Test that when a products quantity is at 0 it is inactive. """
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.set_quantity(0) # Quantity set to zero, is_active should now be false
    assert product.is_active() is False

def test_product_purhcase_modifies_quantity():
    """ Test that when a product is purchased that the quantity and total price is returned correctly. """
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(10)
    assert product.get_quantity() == 90 # After 10 MacBooks are bought there should be 90 left in stock
    assert total_price == 1450 * 10 # Confirming that the total price is calculated correctly

def test_buying_larger_quantity_than_exist_raises_exception():
    """ Test that when a order amount is higher than the quantity that's available it raises an Exception. """
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(101) # Buy that is placed is a higher amount than quantity available