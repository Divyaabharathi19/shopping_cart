from xml.dom import minidom

def readXml(name):
   minidom.parse(name).documentElement
   return dict( minidom.parse(name).documentElement.attributes.items())

def writeToXml(name, spec):
    doc = minidom.Document()
    root = doc.createElement("shopping_cart")
    doc.appendChild(root)

    for k,v in spec.items():
        root.setAttribute(k,v)

    doc.writexml( open(name, 'w'), indent="  ", addindent="  ", newl='\n')
    doc.unlink()

class ShoppingCart:

    def __init__(self, product_list_file, shopping_cart_file):
        self.product_list_file = product_list_file
        self.load_product_list()

        self.shopping_cart_file = shopping_cart_file
        self.load_shopping_cart()

    def load_product_list(self):

        xml_dict = readXml(self.product_list_file)

        self.product_list = {k:int(v) for k,v in xml_dict.items()}

        print("Loading Product List ", self.product_list)


    def load_shopping_cart(self):
        xml_dict = readXml(self.shopping_cart_file)

        self.shopping_cart = {k:int(v) for k,v in xml_dict.items()}

        print("Loading Shopping Cart", self.shopping_cart)

    def write_shopping_cart(self):
        cart = {k:str(v) for k,v in self.shopping_cart.items()}

        writeToXml(self.shopping_cart_file, cart)

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


a = ShoppingCart("product_list.xml", "shopping_cart.xml")

a.add_to_cart("apples", 10)
a.add_to_cart("soap", 2)
a.add_to_cart("cake", 3)
a.add_to_cart("apples", 3)

a.delete_from_cart("apples", 3)
a.show_cart()
print("Total", a.sum_of_cart())

