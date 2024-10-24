

class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        total_cost = 0.0
        for product, quantity in shopping_list:
            total_cost += product.buy(quantity)
        return total_cost

def main():
    class Employee:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

        def show(self):
            print(f"Name: {self.name}, Salary: {self.salary}")
            return True  # Ensure it returns True after printing

    # Object creation at the end
    new_emp = Employee("Aharon", 2000)
    # Now calling the method and checking its return value
    result = new_emp.show()
    # Check if the result is True
    print(result)  # Should output True

if __name__ == "__main__":
    main()