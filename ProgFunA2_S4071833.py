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
        print("guestID: {}\n\tname: {}\n\tthe reward_rate: {}\n\tthe reward: {}\n\tthe redeem_rate: {}\n".format(self.ID, self.name, self.reward_rate, self.reward, self.redeem_rate))
    
    @staticmethod
    def set_reward_rate(new_value):
        Guest.reward_rate = new_value
    
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
        print("ID:{}\t\nname:{}\t\nprice:{}\n".format(self.ID, self.name, self.price))
    
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
        print("ID:{}\t\nname:{}\t\nRate per Night:{}\t\ncapacity:{}\n".format(self.ID, self.name, self.price, self.capacity))

class SupplementaryItem(Product):
    def __init__(self, ID, name, price):
        super().__init__(ID, name, price)
        #self.supplementaryItem = supplementaryItem
    
    def get_ID():
        return super().get_ID()
    def get_name():
        return super().get_name()
    def get_price():
        return super().get_price()

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
        try:
            file = open(filename,"r")
            line = file.readline()
            while line:
                line_field = line.strip().split(",")
                #format: guest_ID, guestname, reward rate,reward, and redeem rate. 
                new_guest = Guest(line_field[0], line_field[1], line_field[2], line_field[3], line_field[4])
                self.guest_list.append(new_guest)
                line = file.readline()
            file.close()
            return True
        except FileNotFoundError:
            return False

    def read_product(self, filename):
        try:
            file = open(filename, "r")
            line = file.readline()
            while line:
                line_field = line.strip().split(",")
                if line_field[0].startswith("U"):
                    new_product = ApartmentUnit(line_field[0], line_field[1], float(line_field[2]), int(line_field[3]))
                    self.product_list.append(new_product)
                elif line_field[0].startswith("SI"):
                    new_product = SupplementaryItem(line_field[0], line_field[1], float(line_field[2]))
                    self.product_list.append(new_product)
                line = file.readline()
            file.close()
            return True
        except FileNotFoundError:
            return False
        
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
                if isinstance(apartment, ApartmentUnit):
                    apartment.display_info()
        else:
            for si in self.product_list:
                if isinstance(si, SupplementaryItem):
                    si.display_info()

# the main class of program
class Operations:

    def __init__(self, records):
        self.records = records

    def display_menu(self):
        print("1. Make a booking")
        print("2. Display existing guests")
        print("3. Display existing apartment units")
        print("4. Display existing supplementary items")
        print("5. Exit")
        menu = input("Select an menu: \n")
        self.select_menu(menu)

    def select_menu(self, menu):
        if menu == '1':
            self.make_booking()
        elif menu == '2':
            self.display_guests()
        elif menu == '3':
            self.display_apartments()
        elif menu == '4':
            self.display_supplementary_items()
        elif menu == '5':
            exit()
        else:
            print("Invalid menu, please try again.")
            self.display_menu()
    
    def make_booking():
        
        print()
    def display_guests(self):
        return self.records.list_guest()

    def display_apartments(self):
        return self.records.list_product("apartment")
    
    def display_supplementary_items(self):
        return self.records.list_product("SI")
    
    def exit():
        print()


        


records = Records()
guest_file = records.read_guests("guests.csv")
product_file = records.read_product("products.csv")

if not guest_file and not product_file:
    print("Error both: guests.csv and products.csv are missing!!!")
    exit()
elif not guest_file:
    print("Error guests.csv is missing!!!")
elif not product_file:
    print("Error products.csv is missing!!!")
else:
    print("Loaded both files successfully!!!!")
    operations = Operations(records)
    operations.display_menu()

