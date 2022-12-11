class Product:
    def funct1 (self, Product_name, quantity, Price):
        self.Product_name = Product_name
        self.quantity =quantity
        self.Price = Price

class subProduct(Product):
    def readValues(self):
        self.Product_name = input("Enter the product name: ")
        self.quantity = int(input("Enter the quantity of the product: "))
        self.price = float(input("Enter the product price: ")) 

    def calc_Cost(self):
        cost = self.quantity * self.price
        Vat = cost * 0.12
        total_cost = cost + Vat
        print("The total cost is: ", total_cost)
#Instantiate the class with one object
sub_Product = subProduct()
sub_Product.readValues()
sub_Product.calc_Cost()
          