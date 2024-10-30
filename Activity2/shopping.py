import json
class Product:
    exist_identifier = set()
    def __init__(self,name:str ,price:float ,quantity:int ,unique_identifier:str ,brand:str ):
        self.name= name
        self.price = price
        self.quantity = quantity
        valid_identifier = True
        while valid_identifier:
            if (len(unique_identifier) == 13 and
                    unique_identifier.isdigit() and
                    unique_identifier not in Product.exist_identifier):
                valid_identifier = False
            else:
                unique_identifier = input("Input valid identifier,"
                                          "identifier must consist with 13 characters "
                                          "which only 0-9 is allowed")
        self.unique_identifier = unique_identifier
        Product.exist_identifier.add(self.unique_identifier)
        self.brand = brand
    @classmethod
    def save_type_dic(cls):
        type_info = {
            'name' : str,
            'price' : float,
            'quantity' : int,
            'unique_identifier': str,
            'brand' : str
        }
        return type_info

    def to_json(self):
        data = {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "unique_identifier": self.unique_identifier,
            "brand": self.brand
        }
        return data

class Clothing(Product):
    def __init__(self,name:str ,price:float ,quantity:int ,unique_identifier:str ,brand:str, size:str, material:str):
        super().__init__(name, price, quantity, unique_identifier, brand)
        self.size = size
        self.material = material

    @classmethod
    def save_type_dic(cls):
        type_info = super().save_type_dic()
        type_info.update(
            {
                'size' : str,
                'material' : str
            })
        return type_info

    def to_json(self):
        clothing_data = super().to_json()
        clothing_data.update({
            "size" : self.size,
            "material" : self.material
        })
        return clothing_data

class Food(Product):
    def __init__(self,name,price, quantity, unique_identifier, brand, expiry_date:int, gluten_free:bool, suitable_for_vegans:bool):
        super().__init__(name, price, quantity, unique_identifier, brand)
        self.expiry_date = expiry_date
        self.gluten_free = gluten_free
        self.suitable_for_vegans = suitable_for_vegans

    @classmethod
    def save_type_dic(cls):
        type_info = super().save_type_dic()
        type_info.update({
            'expiry_date' : int,
            'gluten_free' : bool,
            'suitable_for_vegans' : bool
        })
        return type_info

    def to_json(self):
        food_data = super().to_json()
        food_data.update({
            'expiry_date': self.expiry_date,
            'gluten_free': self.gluten_free,
            'suitable_for_vegans': self.suitable_for_vegans

        })
        return food_data

class Electronic(Product):
    def __init__(self, name, price, quantity, unique_identifier, brand, battery_life:float, connectivity:str):
        super().__init__(name, price, quantity, unique_identifier, brand)
        self.battery_life = battery_life
        self.connectivity = connectivity

    @classmethod
    def save_type_dic(cls):
        type_info = super().save_type_dic()
        type_info.update({
            'battery_life' :float,
            'connectivity' : str
        })
        return type_info

    def to_json(self):
        electric_data = super().to_json()
        electric_data.update({
            'battery_life': self.battery_life,
            'connectivity': self.connectivity,

        })
        return electric_data

class ShoppingCart:
    def __init__(self):
        self.product_in_cart = []
        self.product_dic = {} # to distinct specific name of product and product class

    def add_product(self,product):
        self.product_in_cart.append(product)
        self.product_dic[product.name] = product

    def remove_product(self,product_name):
        if product_name in self.product_dic.keys():
            self.product_in_cart.remove(self.product_dic[product_name])
            del self.product_dic[product_name]
        else: print(f'{product_name}(s) not in Shopping Cart')

    def get_contents(self):
        return print(f"Shopping Cart contains {self.product_dic.keys()}")

    def change_product_quantity(self,product,quantity):
        if product in self.product_dic.keys():
            product_class = self.product_dic[product]
            product_class.quantity = quantity
        else: print(f'{product}(s) not in Shopping Cart')

def change_type(string, type_for):
    if type_for == int:
        return int(string)

    elif type_for == float:
        return float(string)

    elif type_for == bool:
        if string.lower() == 'true':
            return True
        elif string.lower() == 'false':
            return False

    elif type_for == str:
        return string

def main():
    print('The program has started.')
    print('Insert your next command (H for help):')
    terminated = False
    valid_commend = ['A','a','R','r','S','s','Q','q','E','e','T','t','H','h']
    valid_type =['clothing', 'food' , 'electronic']
    cart = ShoppingCart()
    cart_quantity = 0
    while not terminated:
        c = input("Type your next command:")
        if c not in valid_commend:
            print(f'“Command not recognised. Please try again”.')

        elif c == 'A' or c == 'a':
            print('Adding a new product:')
            choose_type = input('Insert its type(\'Clothing\', \'Food\' , \'Electronic\'): ')
            if choose_type.lower() not in valid_type: print("We do not have these type of product")
            else:
                if choose_type.lower() == 'clothing':
                    store_info = []
                    parameter_list = list(Clothing.save_type_dic().keys())
                    for parameter in parameter_list:
                        answer = input(f'Insert its {parameter}({Clothing.save_type_dic()[parameter]})type: ')
                        new_answer = change_type(answer,Clothing.save_type_dic()[parameter])
                        store_info.append(new_answer)
                    cloth = Clothing(*store_info)
                    cart.add_product(cloth)
                    cart_quantity += cloth.quantity
                    print(f"The product {cloth.name} has been added to the cart")
                    print(f"The cart contains {cart_quantity} products.")

                elif choose_type.lower() == 'food':
                    store_info = []
                    parameter_list = list(Food.save_type_dic().keys())
                    for parameter in parameter_list:
                        answer = input(f'Insert its {parameter}({Food.save_type_dic()[parameter]})type: ')
                        new_answer = change_type(answer,Food.save_type_dic()[parameter])
                        store_info.append(new_answer)
                    food = Food(*store_info)
                    cart.add_product(food)
                    cart_quantity += food.quantity
                    print(f"The product {food.name} has been added to the cart")
                    print(f"The cart contains {cart_quantity} products.")

                elif choose_type.lower() == 'electronic':
                    store_info = []
                    parameter_list = list(Electronic.save_type_dic().keys())
                    for parameter in parameter_list:
                        answer = input(f'Insert its {parameter}({Electronic.save_type_dic()[parameter]})type: ')
                        new_answer = change_type(answer,Electronic.save_type_dic()[parameter])
                        store_info.append(new_answer)
                    electronic = Electronic(*store_info)
                    cart.add_product(electronic)
                    cart_quantity += electronic.quantity
                    print(f"The product {electronic.name} has been added to the cart")
                    print(f"The cart contains {cart_quantity} products.")

        elif c == 'R' or c == 'r':
            if not cart.product_in_cart:
                print(f'no removal should take place')

            else:
                cart.get_contents()
                remove = input(f'choose the product for remove: ')
                cart.remove_product(remove)

        elif c == 'S' or c == 's':
            if not cart.product_in_cart:
                print(f'No product in the cart')
            else:
                print(f'This is the total of expense:')
                total = 0
                num = 1
                product_dic = cart.product_dic
                for product in product_dic.keys():
                    print(f'{num} - {cart.product_dic[product].quantity} * {cart.product_dic[product].name}'
                          f'  =  {cart.product_dic[product].quantity*cart.product_dic[product].price}')
                    total += cart.product_dic[product].quantity*cart.product_dic[product].price
                print(f"Total = {total}")

        elif c == 'Q' or c == 'q':
            if not cart.product_in_cart:
                print(f'No product in the cart')
            else:
                cart.get_contents()
                product_change = input('Input the product you want to change quantity')
                product_quantity =int(input('Input the number how many you want to buy'))
                before_quantity = cart.product_dic[product_change].quantity
                cart.change_product_quantity(product_change,product_quantity)
                print(f'Quantity of {product_change} changed {before_quantity} to {cart.product_dic[product_change].quantity}')

        elif c == 'E' or c == 'e':
            cart_summary = []
            for product in cart.product_in_cart:
                cart_summary.append(product.to_json())

            print(json.dumps(cart_summary, indent=4))

        elif c == 'T' or c == 't':
            terminated = True

        elif c == 'H' or c == 'h':
            print(f""">>> The program supports the following commands:
>>> [A] - Add a new product to the cart
>>> [R] - Remove a product from the cart
>>> [S] - Print a summary of the cart
>>> [Q] - Change the quantity of a product
>>> [E] - Export a JSON version of the cart
>>> [T] - Terminate the program
>>> [H] - List the supported commands""")


    print('Goodbye.')

if __name__ == '__main__':
    main()
