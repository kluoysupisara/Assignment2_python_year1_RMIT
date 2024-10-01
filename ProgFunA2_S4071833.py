from datetime import datetime
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
    def __init__(self,ID, product, unit_price, qty):
        self.ID = ID
        self.product = product
        self.unit_price = unit_price
        self.quantity = qty
        
    def compute_cost(self):
        # return the original total cost (cost before discount)
        #original_total_cost = self.price_per_unit * self.quantity
        #return original_total_cost
        # the disccount
        # the final total cost (the cost after the discount)
        # the reward
        print()

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
            if search_value == self.guest_list[i].name.strip() or search_value == self.guest_list[i].ID.strip():
                return self.guest_list[i]
            if i == len(self.guest_list) - 1:
                return None

    def find_product(self, search_value):
        for i in range(len(self.product_list)):
            if search_value == self.product_list[i].name.strip() or search_value == self.product_list[i].ID.strip():
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
    
    def make_booking(self):
        try:
            # self.guest_name = self.is_alpha() 
            # self.number_guest = self.is_positive_guest() 
            # self.apartment = self.check_apartmentID()
            # self.apartment_id = self.apartment.ID
            # self.apartment_rate = self.apartment.price
            # print(f"[AUTO] The selected unit rate is ${self.apartment_rate:.2f}\n")
            # self.checkin_date = self.get_checkin_date()
            # self.checkout_date = self.get_checkout_date()
            # self.lenght_stay = self.calculate_night_stay(self.checkin_date, self.checkout_date)
            # self.booking_date = self.get_current_date()

            self.add_supplementary()

            #self.display_receipt()
        except ValueError as e:
            print("Error! make booking: {e}")
        
        
#====================================== PART1 =================================
    @staticmethod
    def is_alpha():
        while True:
            str = input("Enter the name of the main guest (e.g. Alyssa):\n")
            if str.isalpha(): #check input string only alphabet
                return str
            else:
                print("names contain only alphabet characters")
        # function check number of guest mus be positive integer.
    @staticmethod    
    def is_positive_guest():
        while True:
            try:
                number = int(input("How many people will stay?:\n"))
                if number > 0: # check number varieable must be greater than 0 to check the positive int.
                    return number
                else:
                    print("Please enter a valid positive number.\n")
            except:
                print("Please enter a valid positive number.\n")

    # function check apartment_id must be in list apartment_id
    @staticmethod
    def check_apartmentID():
        while True:
            apartment_id = input("Enter apartment unit ID to book:\n")
            if records.find_product(apartment_id):
                return records.find_product(apartment_id)
            else:
                print("This is not valid apartment ID. Please enter the valid ID.")
    @staticmethod            
    def get_checkin_date():
        while True:
            checkin_date = input("\nWhen will the guest is expected to check in (dd/mm/yyyy):\n")
            if Operations.validate_date(checkin_date):
                return checkin_date
            else:
                print("Input Date. Enter valid date.")
    @staticmethod            
    def get_checkout_date():
        while True:
            checkout_date = input("\nWhen will the guest is expected to check out (dd/mm/yyyy):\n")
            if Operations.validate_date(checkout_date):
                return checkout_date
            else:
                print("Invalid Date. Enter valid date.")

    @staticmethod            
    def validate_date(date):
        try:
            valid_date = datetime.strptime(date, "%d/%m/%Y")
            return valid_date
        except:
            print("Invalid date format. Enter in format dd/mm/yyyy")

    @staticmethod
    def calculate_night_stay(check_in, check_out):
        night = datetime.strptime(check_out, "%d/%m/%Y") - datetime.strptime(check_in, "%d/%m/%Y")
        if night.days > 0:
            return night.days
        else:
            print("Invalid input date> Check out date must be after Check in date!!!!!")

    @staticmethod
    def get_current_date():
        current_date = datetime.now()
        format_date = current_date.strftime("%d/%m/%Y %H:%M")
        return format_date


    @staticmethod            
    def isNotNull(value):
        if value is None:
            return False
        elif value.strip():
            return False
        elif len(value) == 0:
            return False
        else:
            return True
        
    @staticmethod
    def add_supplementary():
        q1 = Operations.validate_asking_supplementary_1()
        if q1:
            while True:
                si = Operations.get_supplementary()
                if si:
                    si_qty = Operations.get_quantity()
                    if si_qty:
                        confirm = Operations.confirm_order()
                        if confirm:
                            print("ADD to order class !!!!!!!")
                            print("supplementary_id:", si.ID)
                            print("supplementary_id_Name:", si.name)
                            print("supplementary_id_qty:",si_qty)
                            print("supplementary_id_Unit:", si.price)
                        if not Operations.validate_asking_supplementary_2():
                            break

    @staticmethod
    def validate_asking_supplementary_1():
        while True:
            answer = input("Do you want to order a supplementary item? (y/n)\n")
            if answer.lower() in ['y', 'n']:
                return answer.lower() == 'y'
            print("Invalid answer. Please answer 'y' or 'n' only\n")
    @staticmethod
    def validate_asking_supplementary_2():
        while True:
            answer = input("Do you want to order another supplementary item? (y/n):\n")
            if answer.lower() in ['y', 'n']:
                return answer.lower() == 'y'
            print("Invalid answer. Please answer 'y' or 'n' only\n")
    @staticmethod
    def get_supplementary():
        while True:
            supplementary_id = input(
                "Enter the supplementary item ID (e.g., car_park, breakfast, toothpaste, extra_bed):\n"
            )
            si = records.find_product(supplementary_id)
            if si != None:
                return si
            print("Invalid answer. There are non this supplementary_id\n")
    @staticmethod
    def get_quantity():
        while True:
            try:
                quantity = int(input("Enter the desired quantity: "))
                if quantity > 0:
                    return quantity
                print("Quantity must be an integer greater than 0.")
            except ValueError:
                print("Invalid input. Quantity must be an integer greater than 0.")
    @staticmethod
    def confirm_order():
        while True:
            confirm = input("Confirm the order: (y/n)\n")
            if confirm.lower() in ['y', 'n']:
                    return confirm.lower() == 'y'
            print("Invalid answer. Please answer 'y' or 'n' only\n")



    # disply total receipt after making a book apartment from menu 1
    def display_receipt(self):
        print("="*70)
        print(f"{'Pythonia Service Apartment - Booking Receipt':^70}")
        print("="*70)
        print(f"{'Guest name:':<20} {self.guest_name}")
        print(f"{'Number of guests:':<20} {self.number_guest}")
        print(f"{'Apartment name:':<20} {self.apartment.name}(auto-complete based on id)")
        print(f"{'Apartment_rate:$':<20} {self.apartment_rate:.2f}(AUD) (auto-complete based on id)")
        print(f"{'Check-in date:':<20} {self.checkin_date}")
        print(f"{'Check-out date:':<20} {self.checkout_date}")
        print(f"{'Length of stay:':<20} {self.lenght_stay}(night)")
        print(f"{'Booking date:':<20} {self.booking_date}")
        # print("---------------------------------------------------------------- ")
        # print(f"Total cost: ${receipt['cost']:.2f}  (AUD)")
        # print(f"Earned rewards: {receipt['point']} (points)\n")
        # print("Thank you for your booking! We hope you will have an enjoyable stay.")
        # print("====================================================================== ")
#====================================== [END] PART1 =================================
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

