class Guest:

    reward_rate = 100
    redeem_rate = 1
    #format: guest_ID, guestname, reward rate,reward, and redeem rate.
    def __init__(self, ID, name, reward_rate, reward, redeem_rate):
        self.ID = ID
        self.name = name
        self.reward = reward
        self.reward_rate = reward_rate
        self.redeem_rate = redeem_rate
    def get_reward(self, total_cost):
        self.reward = round(total_cost * (self.reward_rate/100))

        print("Get rewards:{}".format(self.reward))
    
    def update_reward(self, new_reward):
        self.reward += new_reward
    
    def display_info(self):
        print("guestID: {:<5}\tname: {:>10}\n\tthe reward_rate: {}\tthe reward: {}\n\tthe redeem_rate{}\n".format(self.ID, self.name, self.reward_rate, self.reward, self.redeem_rate))
    
    def set_reward_rate(self, new_value):
        self.reward_rate = new_value
    
    def set_redeem_rate(self, new_value):
        self.redeem_rate = new_value

class Product:
    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price

    def get_ID(self):
        return self.ID
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    
    def display_info(self):
        print("print variable Productclass")
        print("ID:{}\tname:{}\tprice:{}\n".format(self.ID, self.name, self.price))
    
class ApartmentUnit(Product):
    def __init__(self, ID, name, price, capacity):
        super().__init__(ID, name, price)
        self.capacity = capacity
    def get_ID():
        return super().get_ID()
    def get_name():
        return super().get_name()
    def get_price():
        return super().get_price()
    def get_capacity(self):
        return self.capacity
    def display_info(self):
        print("ID:{}\tname:{}\tRate per Night:{}\ncapacity:{}".format(self.ID, self.name, self.price, self.capacity))

class SupplementaryItem(Product):
    def __init__(self, ID, name, price, supplementaryItem):
        super().__init__(ID, name, price)
        self.supplementaryItem = supplementaryItem
    
    def get_ID():
        return super().get_ID()
    def get_name():
        return super().get_name()
    def get_price():
        return super().get_price()
    def get_supplementaryItem(self):
        return self.supplementaryItem
    def display_info(self):
        return super().display_info()
    
# Order class store guest's purchase    
class Order:
    def __init__(self,ID, name, product, price_per_unit, quantity):
        self.ID = ID
        self.name = name
        self.product = product
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        
    def compute_cost(self):
        # return the original total cost (cost before discount)
        original_total_cost = self.price_per_unit * self.quantity
        return original_total_cost
        # the disccount
        # the final total cost (the cost after the discount)
        # the reward

# the central data repository of program.
class Records:
    # list of exising guest what should to store guestID, name, reward
    guest_list = []
    # list of exising product productID, price 
    product_list = []

    def read_guests(self, filename):
        file = open(filename,"r")
        line = file.readline()
        while line:
            line_field = line.strip().split()
            new_guest = Guest()
            #format: guest_ID, guestname, reward rate,reward, and redeem rate. 
            new_guest(line_field[0], line_field[1], line_field[2], line_field[3], line_field[4])
            self.guest_list.append(new_guest)
            line = file.readline()
        file.close()

    def read_product(self, filename):
        file = open(filename, "r")
        line = file.readline()
        while line:
            line_field = line.strip().split()
            if line_field[0].startswith("U"):
                new_product = ApartmentUnit(line_field[0], line_field[1], line_field[2], line_field[3])
            elif line_field[0] == "SI":
                new_product = SupplementaryItem(line_field[0], line_field[1], line_field[2])
            self.product_list.append(new_product)
            line = file.readline()
        file.close()
        
    def find_guest(self, search_value):
        for i in range(len(self.guest_list)):
            if search_value == self.guest_list[i].name or search_value == self.guest_list[i].ID:
                return self.guest_list[i]
            if i == len(self.guest_list) - 1:
                return None
            
    def find_product(self, search_value):
        for i in range(len(self.product_list)):
            if search_value == self.product_list[i].name or search_value == self.product_list[i].ID:
                return self.product_list[i]
            if i == len(self.product_list) - 1:
                return None
            
    def list_guest(self):
        for guest in self.guest_list:
            guest.display_info()

    def list_product(self, product_type):
        if product_type.lower() == "apartment":
            for apartment in self.product_list:
                apartment.display_info()
        else:
            for product in self.product_list:
                product.display_info()
# the main class of program
class Operations:
    record = Records()
    record.read_guests("guest.csv")
    record.read_product("product.csv")
    
    def make_a_booking():
        
        print()
    def display_existing_guest():
        print()

    def display_existing_apartment():
        print()
    def display_existing_supplementary_items():
        print()

    def exit():
        print()






