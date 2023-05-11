import json
import jsonschema

def readJson(name):
    with open(name, 'r') as fd:
        spec = json.load(fd)
    return spec

def writeToJson(name, spec):
    with open(name, 'w') as fd:
        fd.write(json.dumps(spec, indent=4))

def validateJson(spec, schema_spec):
    jsonschema.validate(instance=spec, schema = schema_spec)


class ShoppingCart:

    product_list_schema = "product_list_schema.json"
    shopping_cart_schema = "shopping_cart_schema.json"

    def __init__(self, product_list_file, shopping_cart_file):
        self.product_list_file = product_list_file
        self.load_product_list()

        self.shopping_cart_file = shopping_cart_file
        self.load_shopping_cart()

    def load_product_list(self):
        spec = readJson(self.product_list_file)

        schema_spec = readJson(self.product_list_schema)
        validateJson(spec, schema_spec)

        self.product_list = {}#Product Name:Price
        for product_dict in spec["product_list"]:
            self.product_list[product_dict["name"]] = product_dict["value"]

        print("Loading Product List ", self.product_list)


    def load_shopping_cart(self):
        spec = readJson(self.shopping_cart_file)

        schema_spec = readJson(self.shopping_cart_schema)
        validateJson(spec, schema_spec)

        self.shopping_cart = {}#Product Name:Quantity
        for item_dict in spec["cart"]:
            self.shopping_cart[item_dict["name"]] = item_dict["quantity"]

        print("Loading Shopping Cart", self.shopping_cart)

    def write_shopping_cart(self):
        cart = []
        for product, quantity in self.shopping_cart.items():
            product = {"name":product, "quantity":quantity}
            cart.append(product)
        writeToJson(self.shopping_cart_file, {"cart":cart})

    def add_to_cart(self, product, quantity):
        print(f"Adding {quantity} {product} {self.shopping_cart}")
        if product in self.shopping_cart:
            self.shopping_cart[product] += quantity
        else:
            self.shopping_cart[product] = quantity
        print(f"Added {quantity} {product} {self.shopping_cart}")
        self.write_shopping_cart()

    def delete_from_cart(self, product, quantity):
        print(f"Deleting {quantity} {product} {self.shopping_cart}")
        if self.shopping_cart[product] > quantity:
            self.shopping_cart[product] -= quantity
        else:
            self.shopping_cart.pop(product)
        print(f"Deleted {quantity} {product} {self.shopping_cart}")

        self.write_shopping_cart()

    def sum_of_cart(self):
        total = 0
        for product, quantity in self.shopping_cart.items():
            total += self.product_list[product]*quantity
        return total

    def show_cart(self):
        print("Showing Shopping Cart", self.shopping_cart)


a = ShoppingCart("product_list.json", "shopping_cart.json")

a.add_to_cart("apples", 10)
a.add_to_cart("soap", 2)
a.add_to_cart("cake", 3)
a.add_to_cart("apples", 3)

a.delete_from_cart("apples", 3)
a.show_cart()
print("Total", a.sum_of_cart())
