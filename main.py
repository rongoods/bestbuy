from store import Store
from products import Product

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)

def start(store):
    while True:
        print()
        print("   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        selection = int(input("Please choose a number: "))

        if selection == 1:
            products = store.get_all_products()
            if products:
                for product in products:
                    print(product.show())
            else:
                print("No products available.")

        elif selection == 2:
            total_quantity = store.get_total_quantity()
            print(f"Total of {total_quantity} items in store")

        elif selection == 3:
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
                    shopping_list.append((products[product_number -1], quantity))
                except ValueError:
                    print("Invalid input.")

            if shopping_list:
                try:
                    store.order(shopping_list)
                except Exception as e:
                    print(f"Exception error: {e}")
            else:
                print("No order placed.")

        elif selection == 4:
            break

        else:
            start(best_buy)

if __name__ == "__main__":
    start(best_buy)

