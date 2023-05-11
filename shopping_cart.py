class ShoppingCart:

    product_list = {"apples":1, "soap":5, "cake":20} #Product Name:Price

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.shopping_cart = {} #Product Name:Quantity

    def add_to_cart(self, product, quantity):
        print(f"Adding {quantity} {product} {self.shopping_cart}")
        if product in self.shopping_cart:
            self.shopping_cart[product] += quantity
        else:
            self.shopping_cart[product] = quantity
        print(f"Added {quantity} {product} {self.shopping_cart}")

    def delete_from_cart(self, product, quantity):
        print(f"Deleting {quantity} {product} {self.shopping_cart}")
        if self.shopping_cart[product] > quantity:
            self.shopping_cart[product] -= quantity
        else:
            self.shopping_cart.pop(product)
        print(f"Deleted {quantity} {product} {self.shopping_cart}")

    def sum_of_cart(self):
        total = 0
        for product, quantity in self.shopping_cart.items():
            total += self.product_list[product]*quantity
        return total

    def show_cart(self):
        print("Showing Shopping Cart", self.shopping_cart)


a = ShoppingCart("A")
a.add_to_cart("apples", 10)
a.add_to_cart("soap", 2)
a.add_to_cart("cake", 3)
a.add_to_cart("apples", 3)

a.delete_from_cart("apples", 3)
a.show_cart()
print("Total", a.sum_of_cart())


