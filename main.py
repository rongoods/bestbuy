from store import Store
from products import Product, NonStockedProduct, LimitedProduct
from promotion import Promotion, SecondHalfPrice, ThirdOneFree, PercentDiscount


def default_stock():
    """Sets up the initial stock of inventory."""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    return Store(product_list)


def start(store):
    """Displays the store menu and handles the user's input."""
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        selection = input("Please choose a number: ")

        if selection == "1":
            products = store.get_all_products()
            if products:
                for product in products:
                    print(product.show())
            else:
                print("No products available.")

        elif selection == "2":
            total_quantity = store.get_total_quantity()
            print(f"Total of {total_quantity} items in store")

        elif selection == "3":
            products = store.get_all_products()
            if not products:
                print("There are currently no products available.")
                continue

            print("-----")
            for index, product in enumerate(products, start=1):
                print(f"{index}. {product.show()}")
            print("-----")

            shopping_list = []
            while True:
                print("When you want to finish order, enter empty text.")
                product_number = input("Which product # do you want? ")
                if product_number == "":
                    break
                try:
                    product_number = int(product_number)
                    if product_number < 1 or product_number > len(products):
                        print("Invalid selection, enter a valid product number.")
                        continue

                    quantity = int(input("What amount do you want? "))
                    if quantity <= 0:
                        print("Quantity entered must be greater than 0.")
                        continue

                    product = products[product_number - 1]
                    if product.is_limited() and quantity > product.get_maximum():
                        print(f"You can only order a maximum of {product.get_maximum()} of this item.")
                        continue
                    elif product.quantity < quantity:
                        print(f"Not enough stock available. Only {product.quantity} left.")
                        continue

                    shopping_list.append((product, quantity))
                except ValueError:
                    print("Invalid input.")

            if shopping_list:
                try:
                    total_price = store.order(shopping_list)
                    print(f"Order placed successfully! Total cost: ${total_price:.2f}")

                    # Print updated product quantities
                    print("Updated product quantities:")
                    for product, _ in shopping_list:
                        print(f"{product.name}: {product.get_quantity()} left")
                except Exception as e:
                    print(f"Error processing order: {str(e)}")
            else:
                print("No order placed.")

        elif selection == "4":
            break

        else:
            print("Invalid input, enter a number 1-4.")


if __name__ == "__main__":
    best_buy = default_stock()
    start(best_buy)