from datetime import datetime
class Guest:

    reward_rate = 100
    redeem_rate = 1
    #format: guest_ID, guestname, reward rate,reward, and redeem rate.
    def __init__(self, ID, name, reward=0, reward_rate=None, redeem_rate=None):
        self.ID = ID
        self.name = name.strip()
        self.reward = float(reward)
        self.reward_rate = float(reward_rate) if reward_rate is not None else Guest.reward_rate
        self.redeem_rate = float(redeem_rate) if redeem_rate is not None else Guest.redeem_rate

    def get_reward(self,total_cost):
        cal_reward = round(total_cost * (self.reward_rate/100))
        return cal_reward
    
    def update_reward(self, new_reward):
        self.reward += new_reward
        print(f"Success Update reward!!! {self.name} has total reward = {self.reward}")

    def update_reward_from_order(self, new_reward):
        self.reward = new_reward
        print(f"Success Update reward!!! {self.name} has total reward = {self.reward} from order file.")
    
    
    def display_info(self):
        print(f"{self.ID:<10} {self.name:<20} {self.reward_rate:>10.2f} {self.reward:>10.2f} {self.redeem_rate:>15.2f}")
    @staticmethod
    def set_reward_rate(new_value):


        Guest.reward_rate = new_value
        print(f"Successfully set the new reward rate for all guests to {Guest.reward_rate:.2f}%.\n")
    @staticmethod
    def set_redeem_rate(new_value):
        Guest.redeem_rate = new_value
        print(f"Successfully set the new reward rate for all guests to {Guest.redeem_rate:.2f}%.\n")

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
        print(f"{self.ID:<5} {self.name:<30} {self.price:<20.2f}")

    
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
        print(f"{self.ID:<15} {self.name:<30} {self.price:<20.2f} {self.capacity:<10}")

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
    
class Bundle(Product):
    def __init__(self, ID, name, price, component=[]):
        super().__init__(ID, name, price)
        self.component = component
        self.component_dict = {}

    def count_component(self):
        component_dict = {}
        for item in self.component:
            if item in component_dict:
                component_dict[item] += 1
            else:
                component_dict[item] = 1
        self.component_dict = component_dict

    def display_info(self):
        #display here
        self.count_component()
        # Create a formatted string for components with quantities
        component_str = ', '.join([f"{qty} x {comp}" if qty >= 1 else comp for comp, qty in self.component_dict.items()])
        print(f"{self.ID:<5} {self.name:<45} {component_str:<60} {self.price:<10.2f}")

    
# Order class store guest's purchase    
class Order:
    def __init__(self,guest_name, products, total_cost, earn_reward, order_date):
        self.guest_name = guest_name
        self.products = products
        self.total_cost = total_cost
        self.earn_reward = earn_reward
        self.order_date = order_date
    # sprint formatted order information
    def display_info(self):
        # Create the product string in the format 'quantity x product_id'
        products_str = ', '.join([f"{item['quantity']} x {item['product_id']}" for item in self.products])
        print(f"{self.guest_name:<20}{products_str:<45}{self.total_cost:<15.2f}{self.earn_reward:<15}{self.order_date:<20}")

    def display_history(self, index):
        # Create the product string in the format 'quantity x product_id'
        products_str = ', '.join([f"{item['quantity']} x {item['product_id']}" for item in self.products])
        print(f"Order{index:<10} {products_str:<50} {self.total_cost:<15.2f} {self.earn_reward:<15}")


    
    # =============== Backup Orderclass before HD Level=================
    # def __init__(self,guest, product=[], qty=[]):
    #     self.guest = guest
    #     self.product = product
    #     self.quantity = qty
    #     self.cost_dict = {}
        
    # def compute_cost(self, ans):

    #     # cost before the discount
    #     original_total_cost = sum(product.price * qty for product, qty in zip(self.product, self.quantity))
    #     discount = 0
    #     redeem_point = 0
    #     print("original_total_cost:", original_total_cost)
    #     if ans:
    #         discount = self.guest.reward * (self.guest.redeem_rate/100)
    #         # point is used to reedeem
    #         redeem_point = self.guest.reward
            
    #     # the final_total_cost:
    #     final_total_cost = original_total_cost - discount
    #     # earn_reward
    #     earn_reward = self.guest.get_reward(final_total_cost)

    #     self.cost_dict['original_total_cost'] = original_total_cost
    #     self.cost_dict['redeem_point'] = redeem_point
    #     self.cost_dict['discount'] = discount
    #     self.cost_dict['final_total_cost'] = final_total_cost
    #     self.cost_dict['reward'] = earn_reward

    #     #get_reward
    #     new_reward = self.guest.get_reward(final_total_cost)
    #     #update reward
    #     if discount > 0:
    #         self.guest.update_reward(redeem_point*-1)
    #         self.guest.update_reward(new_reward)
    #     else:
    #         self.guest.update_reward(new_reward)

    #     return self.cost_dict
    # =============== Backup Orderclass before HD Level=================


# the central data repository of program.
class Records:
    # list of exising guest what should to store guestID, name, reward
    guest_list = []
    # list of exising product productID, price 
    product_list = []
    # list of order
    order_list = []

    def read_guests(self, filename):
        try:
            file = open(filename,"r")
            line = file.readline()
            while line:
                line_field = line.strip().split(",")
                #format: guest_ID, guestname, reward rate,reward, and redeem rate. 
                new_guest = Guest(line_field[0], line_field[1], line_field[3], line_field[2], line_field[4])
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
                    new_product = ApartmentUnit(line_field[0], line_field[1].strip(), float(line_field[2]), int(line_field[3]))
                    self.product_list.append(new_product)
                elif line_field[0].startswith("SI"):
                    new_product = SupplementaryItem(line_field[0], line_field[1].strip(), float(line_field[2]))
                    self.product_list.append(new_product)
                elif line_field[0].startswith("B"):
                        bundle_id = line_field[0].strip()
                        bundle_name = line_field[1].strip()
                        bundle_price = float(line_field[-1])
                        bundle_components = line_field[2:-1]
                        new_product = Bundle(bundle_id, bundle_name, bundle_price, bundle_components)
                        self.product_list.append(new_product)
                line = file.readline()
            file.close()
            return True
        except FileNotFoundError:
            return False
    # read order.csv file and at to list
    def read_orders(self, filename):
        try:
            file = open(filename,"r")
            line = file.readline()

            # create guest look up dictionary: get guest object from guest_list to loopup_guests after loading order.csv
            # key (guestname) : value (object guest)
            guest_lookup = {guest.name: guest for guest in self.guest_list}
            #create reward_update dict to update reward base on order.file
            # key (guestname) : value (earn_reward)
            reward_updates = {}

            while line:
                line_field = line.strip().split(",")
                guest_name = line_field[0].strip()
                raw_products = line_field[1:-3]  # ['2 x U12swan', '4 x SI2' ]
                products = []
                
                for item in raw_products:
                    # Match format like '2 x U12swan' or '4 x SI2'
                    parts = item.strip().split(" x ")
                    if len(parts) == 2:
                        quantity = int(parts[0].strip())
                        product_id = parts[1].strip()
                        products.append({
                            'product_id': product_id,
                            'quantity': quantity
                        })
                # Extract and convert the total cost and earned rewards fields
                total_cost = float(line_field[-3].strip())
                earn_reward = int(line_field[-2].strip())
                
                # Extract the order date
                order_date = line_field[-1].strip()
                
                # Create a new Order object and add it to the order list
                new_order = Order(guest_name, products, total_cost, earn_reward, order_date)
                self.order_list.append(new_order)

                # Update the reward points in the reward_updates dictionary
                if guest_name in reward_updates:
                    reward_updates[guest_name] += earn_reward
                else:
                    reward_updates[guest_name] = earn_reward
                # Read next line
                line = file.readline()
            file.close()

            # Update the guests' reward points based on reward_updates dictionary
            for guest_name, total_reward in reward_updates.items():
                if guest_name in guest_lookup:
                    guest_lookup[guest_name].update_reward_from_order(total_reward)

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
    def find_order(self, search_value):
        matching_orders = []
        for i in range(len(self.order_list)):
            if search_value == self.order_list[i].guest_name.strip():
                matching_orders.append(self.order_list[i])
        if not matching_orders:
            return None
        return matching_orders
            
    def list_guest(self):
        text = " Display existing guests "
        total_width = 100
        padding = "-" * ((total_width - len(text)) // 2)
        # Print the scaled display
        print(f"\n{padding}{text}{padding}\n")

        print(f"{'ID':<10} {'Name':<20} {'Reward_rate':>10} {'Reward':>10} {'Redeem_rate':>15}")
        for guest in self.guest_list:
            guest.display_info()

    def list_product(self, product_type):
        if product_type.lower() == "apartment":
            text = " Display existing apartment units "
            total_width = 100
            padding = "-" * ((total_width - len(text)) // 2)
            # Print the scaled display
            print(f"\n{padding}{text}{padding}\n")
            print(f"{'ID':<15} {'Name':<30} {'Rate per Night':<20} {'Capacity':<10}")
     
            for apartment in self.product_list:
                if isinstance(apartment, ApartmentUnit):
                    apartment.display_info()
        elif product_type.lower() == 'si':
            text = " Display existing supplementary items "
            total_width = 100
            padding = "-" * ((total_width - len(text)) // 2)
            # Print the scaled display
            print(f"\n{padding}{text}{padding}\n")
            print(f"{'ID':<5} {'Name':<30} {'Price':<20}")
           
            for si in self.product_list:
                if isinstance(si, SupplementaryItem):
                    si.display_info()
        elif product_type.lower() == 'bundle':
            text = " Display existing  bundle items "
            total_width = 100
            padding = "-" * ((total_width - len(text)) // 2)
            # Print the scaled display
            print(f"\n{padding}{text}{padding}\n")
            print(f"{'ID':<5} {'Name':<45} {'Components':<60} {'Price':<10}")
          
            for bundle in self.product_list:
                if isinstance(bundle, Bundle):
                    bundle.display_info()

    # Display all order
    def list_order(self):
        print(f"{'Guests name':<20}{'Product':<45}{'Total Cost':<15}{'Earn Rewards':<15}{'Order Date':<20}")
  
        for order in self.order_list:
            if isinstance(order, Order):
                order.display_info()
    
    # display a guest order history
    def order_history(self, guest_name, orders):
        print(f"\nThis is the booking and order history for {guest_name}.")
        print("{:<15} {:<50} {:<15} {:<15}".format("order ID","Product Ordered", "Total Cost", "Earned Rewards"))
        index = 1
        for order in orders:
            if isinstance(order, Order):
                order.display_history(index)
                index += 1
    def add_update_apartment(self):
        """
        Add or update information of apartment units.
        The user can add a new apartment unit or update an existing one.
        """
        user_input = input("Enter apartment information (e.g., apartment_id apartment_name rate capacity):\n").strip().split()
        if len(user_input) < 4:
                print("Invalid input format. Please enter in the format 'apartment_id apartment_name rate capacity'. Returning to main menu...")
                return  # Return to main menu on invalid input
        try:
            #apartment_id, apartment_name, rate, capacity = user_input[0], user_input[1], user_input[2], user_input[3]
            # Validate input length (must have exactly 2 parts: item_id and price)
            # Extract the first three parts: apartment_id, rate, and capacity, and join the rest as the apartment_name
            apartment_id = user_input[0]
            rate = user_input[-2]  # Second-to-last element
            capacity = user_input[-1]  # Last element
            apartment_name = " ".join(user_input[1:-2])  # Join all elements in between as apartment_name
    
        
            if not self.validate_apartment_id(apartment_id): # check invalidate apartment_id
                print("Error name is not validated")
                return
            # if pass validate apartment_id can add to new apartment_id
            try:
                # Convert rate to float and capacity to integer
                apartment_name = apartment_name.strip()
                rate = float(rate)
                capacity = int(capacity)
            except ValueError:
                print("Invalid rate or capacity. Rate must be a number (e.g., 200.00) and capacity must be an integer (e.g., 3).")
                return  # Return to main menu on invalid input
            
            # Check if the apartment unit already exists in the product list
            existing_apartment = self.find_product(apartment_id)
            if existing_apartment:
                print(f"Apartment unit with ID '{apartment_id}' already exists.")
                print("Updating the existing apartment unit information...")
                # Update the existing apartment unit information
                existing_apartment.name = apartment_name # Name is set to the ID (e.g., U12swan)
                existing_apartment.price = rate
                existing_apartment.capacity = capacity
                print(f"Updated apartment unit '{apartment_id}' successfully!")
            else:
                # Create a new apartment unit and add it to the product list
                new_apartment = ApartmentUnit(apartment_id, apartment_name, rate, capacity)
                self.product_list.append(new_apartment)
                print(f"Added new apartment unit '{apartment_id}' successfully!")

            # Display the updated list of apartment
            print("\nUpdated List of ApartmentUnits:")
            self.list_product("apartment")
            
        except:
            print("invalid format.\n")

    def validate_apartment_id(apartment_id):
        if not apartment_id.startswith('U'): # check apartmentid must start with U
            return False
        i = 1
        for i in range(1,len(apartment_id)) :
            if not apartment_id[i].isdigit():
                #print("final digit of number:",i)
                break
            i += 1
        if not apartment_id[i:].isalpha() : # check after number is not alphabet
            return False
        return True
    
    def validate_item_id(item_id):
        if not item_id.startswith('SI'): # check apartmentid must start with U
            return False
        return True
    
    # New method to add/update supplementary item information with input validation
    def add_update_supplementary_item(self):
        print("\n--- Add/Update Information of Supplementary Items ---")

        while True:
            # Prompt the user to enter supplementary item information in the required format
            user_input = input("Enter supplementary item information in the format 'item_id item_name price, item_id item_name price, ...' (e.g., IS5 toothpaste 5.2, IS6 toothbrush 3.0):\n").strip().split(',')

            valid_input = True  # Flag to check if all entries are valid

            # Process each item separately
            for item in user_input:
                item = item.strip().split()  # Split each item by whitespace to get item_id, item_name, and price

                # Ensure that each item has at least 3 components: item_id, item_name, price
                if len(item) < 3:
                    print(f"Invalid input format for '{' '.join(item)}'. Please enter in the format 'item_id item_name price'.")
                    valid_input = False  # Set the flag to False if there's any invalid entry
                    break  # Exit the for loop and prompt the user to enter again

                # Extract item_id, item_name, and price
                item_id = item[0]
                price = item[-1]  # Last element is the price
                item_name = " ".join(item[1:-1])  # Join the remaining elements as item_name
                if not self.validate_item_id(item_id):
                    print("Error ID is not validated Id must dtart with SI")
                    return
                try:
                    # Convert price to float and validate it's positive
                    price = float(price)
                    if price <= 0:
                        print(f"Price for item '{item_id}' must be a positive number.")
                        valid_input = False  # Set the flag to False if price is invalid
                        break  # Exit the for loop and prompt the user to enter again
                except ValueError:
                    print(f"Invalid price format for item '{item_id}'. Please enter a numeric value.")
                    valid_input = False  # Set the flag to False if there's any invalid entry
                    break  # Exit the for loop and prompt the user to enter again

            # If all entries are valid, break out of the while loop
            if valid_input:
                break
            else:
                print("Please re-enter the supplementary item information correctly.\n")

        # Process the valid input and add/update items
        for item in user_input:
            item = item.strip().split()
            item_id = item[0]
            price = float(item[-1])  # Last element is the price
            item_name = " ".join(item[1:-1])  # Join the remaining elements as item_name

            # Check if the supplementary item already exists in the product list
            existing_supplementary = self.find_product(item_id)

            if existing_supplementary:
                print(f"Supplementary item with ID '{item_id}' already exists.")
                print("Updating the existing supplementary item information...")
                # Update the existing supplementary item information
                existing_supplementary.name = item_name
                existing_supplementary.price = price
                print(f"Updated supplementary item '{item_id}' successfully with new price: {price:.2f}!")
            else:
                # Create a new supplementary item and add it to the product list
                new_supplementary = SupplementaryItem(item_id, item_name, price)
                self.product_list.append(new_supplementary)
                print(f"Added new supplementary item '{item_id}' successfully with price: {price:.2f}!")

        # Display the updated list of supplementary items
        print("\nUpdated List of Supplementary Items:")
        self.list_product("si")

    # New method to add/update bundle information with input validation
    def add_update_bundle(self):
        """
        Add or update information of a bundle product based on user input.
        The input must follow the format: bundle_id bundle_name price component1, component2, ...
        Example: B1 Bed and Breakfast 220.48 U12swan, SI2, SI2, SI1
        """
        print("\n--- Add/Update Information of Bundles ---")

        # Prompt the user to enter bundle information in the required format
        user_input = input("Enter bundle information in the format 'bundle_id bundle_name price components' (e.g., B1 Bed and Breakfast 220.48 U12swan, SI2, SI2, SI1):\n").strip().split(',')

        # Validate input length (must have at least 4 parts: bundle_id, bundle_name, price, and components)
        if len(user_input) < 4:
            print("Invalid input format. Please enter in the format 'bundle_id bundle_name price components'. Returning to main menu...")
            return  # Return to main menu on invalid input

        # Extract and validate each component
        bundle_id = user_input[0]
        bundle_name = user_input[1]  # Join the name parts (everything between ID and price)
        price = user_input[-2]  # Second last part is the price
        components_input = user_input[2:-2]  # Last part is the components string

        if not bundle_id.startswith('B'): # check bundleid must start with B
            print("Invalid bundle ID format. It must start with 'B'. Returning to main menu...")
            return  # Return to main menu on invalid input
        if not bundle_id[1:].isdigit():
            print(f"Invalid bundle ID format '{bundle_id}'. It must start with 'B', followed by a number (e.g., B1).")
            return  # Return to main menu on invalid input

        try:
            # Convert price to float and validate it's positive
            price = float(price)
            if price <= 0:
                print("Price must be a positive number. Returning to main menu...")
                return  # Return to main menu on invalid input
        except ValueError:
            print("Invalid price format. Please enter a numeric value. Returning to main menu...")
            return  # Return to main menu on invalid input

        # Validate and process the component IDs
        component_ids = [component.strip() for component in components_input.split(",")]
        for component in component_ids:
            if not self.find_product(component):
                print(f"Component ID '{component}' does not exist in the product list. Returning to main menu...")
                return  # Return to main menu if any component is invalid

        # Check if the bundle already exists in the product list
        existing_bundle = self.find_product(bundle_id)

        if existing_bundle:
            print(f"Bundle with ID '{bundle_id}' already exists.")
            print("Updating the existing bundle information...")
            # Update the existing bundle information
            existing_bundle.name = bundle_name
            existing_bundle.price = price
            existing_bundle.components = component_ids
            print(f"Updated bundle '{bundle_id}' successfully with new name '{bundle_name}', price: {price:.2f}, and components: {', '.join(component_ids)}!")
        else:
            # Create a new bundle and add it to the product list
            new_bundle = Bundle(bundle_id, bundle_name, price, component_ids)
            self.product_list.append(new_bundle)
            print(f"Added new bundle '{bundle_id}' with name '{bundle_name}', price: {price:.2f}, and components: {', '.join(component_ids)}!")

        # Display the updated list of bundles
        print("\nUpdated List of Bundles:")
        self.list_product("bundle")



# the main class of program
class Operations:

    def __init__(self, records):
        self.records = records

    def display_menu(self):
        print("")
        print("--- Main Menu ---")
        print("1) Make a booking")
        print("2) Display existing guests")
        print("3) Display existing apartment units")
        print("4) Display existing supplementary items")
        print("5) Display existing bundle items")
        print("6) Add/update information of an apartment unit")
        print("7) Add/update information of a supplement item")
        print("8) Add/update information of a bundle item")
        print("9) Adjust the reward rate of all guests")
        print("10) Adjust the redeem rate of all guests")
        print("11) Display all orders")
        print("12) Generate key statistics")
        print("13) Display a guest history")
        print("0) Exit")
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
            self.display_bundle()
        elif menu == '6':
            records.add_update_apartment()
        elif menu == '7':
            records.add_update_supplementary_item()
        elif menu == '8':
            records.add_update_bundle()
        elif menu == '9':
            self.set_reward_rate()
        elif menu == '10':
            self.set_redeem_rate()
        elif menu == '11':
            text = " Display all orders "
            total_width = 100
            padding = "-" * ((total_width - len(text)) // 2)
            # Print the scaled display
            print(f"\n{padding}{text}{padding}\n")
            records.list_order()
        elif menu == '12':
            stat = Statistics(self.records.order_list)
            stat.generate_key_stat()
        elif menu == '13':
            text = " Display a guest order history "
            total_width = 100
            padding = "-" * ((total_width - len(text)) // 2)
            # Print the scaled display
            print(f"\n{padding}{text}{padding}\n")
            self.display_order_history()
        elif menu == '0':
            exit()
        else:
            print("Invalid menu, please try again.")
            self.display_menu()
    
    def make_booking(self):
        try:
            self.guest_name = self.is_alpha() 
            self.number_guest = self.is_positive_guest() 
            self.apartment = self.check_apartmentID()
            self.apartment_id = self.apartment.ID
            self.apartment_name = self.apartment.name.strip()
            self.apartment_rate = self.apartment.price
            print(f"[AUTO] The selected unit rate is ${self.apartment_rate:.2f}")
            self.booking_date = self.get_current_date()
            self.checkin_date = self.get_checkin_date()
            self.checkout_date = self.get_checkout_date()
            
            # Pass validate_date
            self.length_stay = self.calculate_night_stay(self.checkin_date, self.checkout_date)
            #Calculate apartment_sub_total
            self.apartment_sub_total = self.apartment_rate * self.length_stay

            # Check if extra beds are needed based on the number of guests and length of stay
            extra_beds_needed = self.validate_guest_capacity(self.number_guest, self.apartment.capacity, self.length_stay)
            if extra_beds_needed is None:
                # Exceeds maximum capacity even after adding extra beds, booking cannot proceed
                print("Booking cannot proceed as the number of guests exceeds the maximum capacity even with extra beds.\n")
                return
            
            # add supplementary
            self.supplementary_list = self.add_supplementary(extra_beds_needed, self.length_stay)
            

            # a guest finishes making an order

            #check exist guest
            if not self.check_exist_guest():
                number_guest = len(self.records.guest_list)
                new_id = number_guest + 1
                guest = Guest(new_id, self.guest_name)
                #add new_guest to guest_list
                self.records.guest_list.append(guest)

            # Existing guest    
            else:
                #print message showing reward point poceed the purchese
                guest = self.records.find_guest(self.guest_name)
                print(f"{'You have rewards point':<30} {guest.reward}")
            
            # making order part
            list_product_order = []
            list_qty_order = []
            # order for apartment_unit
            list_product_order.append(self.apartment)
            list_qty_order.append(self.length_stay)

            # order supplementary_items
            if self.supplementary_list:
                self.supplementary_item_sub_total = self.get_si_sub_total()
                for si, qty in self.supplementary_list:
                    list_product_order.append(si)
                    list_qty_order.append(qty)

            # create order
            self.order = Order(guest, list_product_order, list_qty_order)
            # add to records
            self.records.add_order(self.order)

            #=============== claim for discount================
            # case guest can claim reward
            could_redeem = guest.reward * guest.redeem_rate
            if could_redeem > 0:
                answer_claim_reward = Operations.confirm_claim_discount()
            else:
                # cannot claim disount reward because donot have enough reward point.
                answer_claim_reward = 'n'
            
            self.cost_result = self.order.compute_cost(answer_claim_reward)
            print("cost_result_total:", self.cost_result)


            self.display_receipt()
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
    #@staticmethod            
    def get_checkin_date(self):
        while True:
            checkin_date = input("\nWhen will the guest is expected to check in (dd/mm/yyyy):\n")
            validate_date = Operations.format_date(checkin_date)
            if validate_date:
                if Operations.validate_dates_checkin(validate_date, self.booking_date):
                    return validate_date
            else:
                print("Input Date. Enter valid date.")    
    @staticmethod
    def validate_dates_checkin(checkin_date, booking_date):
        # Validate the date logic for check-in and check-out.
        if checkin_date < booking_date:
            print("Check-in date is earlier than the booking date")
            return False
        return True      
    def get_checkout_date(self):
        while True:
            checkout_date = input("\nWhen will the guest is expected to check out (dd/mm/yyyy):\n")
            validate_date = Operations.format_date(checkout_date)
            if validate_date:
                if Operations.validate_dates_checkcout(self.checkin_date, validate_date, self.booking_date):
                    return validate_date
            else:
                print("Invalid Date. Enter valid date.")
    @staticmethod
    def validate_dates_checkcout(checkin_date, checkout_date, booking_date):
        # Validate the date logic for check-in and check-out.
        if checkout_date < booking_date:
            print("Check-out date is earlier than the booking date")
            return False
        elif checkout_date < checkin_date:
            print("Check-out date is earlier than check-in date.")
            return False
        elif checkin_date == checkout_date:
            print("Check-in date is the same as the check-out date.")
            return False
        return True

    @staticmethod            
    def format_date(date):
        try:
            format_date = datetime.strptime(date, "%d/%m/%Y")
            return format_date
        except:
            print("Invalid date format. Enter in format dd/mm/yyyy")

    @staticmethod
    def calculate_night_stay(check_in, check_out):
        night = check_out - check_in
        if night.days > 0:
            return night.days
        else:
            print("Invalid input date> Check out date must be after Check in date!!!!!")

    @staticmethod
    def get_current_date():
        current_date = datetime.now()
        #format_date = current_date.strftime("%d/%m/%Y %H:%M")
        return current_date


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
    def add_supplementary(self, extra_beds_needed=0, length_stay=0):
        supplementary_list = []
        #total_car_park = 0
        total_extra_beds = 0  # Track the total number of extra beds added
        print("Length of stay:",length_stay)
        max_extra_beds = 2 * length_stay  # Maximum number of extra beds allowed per order
        #============ extra bed=================
        # Automatically add extra beds if needed
        if extra_beds_needed > 0:
            print(f"Adding {extra_beds_needed} extra bed(s) to the order.")
            extra_bed = records.find_product("SI6") # si6 = extra_bed supplementary
            supplementary_list.append((extra_bed, extra_beds_needed))
            total_extra_beds += extra_beds_needed

        # Allow user to add other supplementary items manually
        q1 = Operations.validate_asking_supplementary_1()
        if q1:
            while True:
                si = Operations.get_supplementary()
                if si.ID == 'SI6':
                    if total_extra_beds == max_extra_beds:
                        print(f"Error: The total extra bed quantity cannot exceed {max_extra_beds}.")
                        continue  # Skip to the next iteration if the input is invalid
                if si:
                    while True:
                        si_qty = Operations.get_quantity()
                        valid_input = True  # Assume input is valid initially
                        # Check if the item is a car park and validate its quantity
                        if si.ID == 'SI1':
                            if si_qty < length_stay:
                                print(f"Error: The total car park quantity cannot be less than the number of nights ({self.length_stay}).")
                                valid_input = False  # Invalid input, re-prompt for quantity
                        # check if item = extra_bed and validate its quantity but not exceed max_extra_bed
                        if si.ID == 'SI6':
                            if si_qty < length_stay: # validate at least minimum of stay nights
                                print(f"Error: The total extra bed quantity cannot be less than the number of nights ({self.lenght_stay}).")
                                valid_input = False  # Invalid input, re-prompt for quantity
                            if total_extra_beds + si_qty >  max_extra_beds:
                                print(f"Error: number of extra bed added is {total_extra_beds + si_qty} The total extra bed quantity cannot exceed {max_extra_beds}.")
                                print(f"You can add {max_extra_beds - total_extra_beds} extra bed(s) to the order.")
                                valid_input = False  # Invalid input, re-prompt for quantity
                        # If input is valid, break out of the quantity input loop
                        if valid_input:
                            if si.ID == 'SI6':
                                total_extra_beds += si_qty
                            break  # Exit the inner while loop
                    #if si_qty:
                    confirm = Operations.confirm_order()
                    if confirm:
                        print("Adding to order...")
                        print("supplementary_id:", si.ID)
                        print("supplementary_id_Name:", si.name)
                        print("supplementary_id_qty:",si_qty)
                        print("supplementary_id_Unit:", si.price)

                        # check if supplemetary item is already exist
                        found = False
                        for item in supplementary_list:
                            if item[0].ID == si.ID:  # Assuming `ID` uniquely identifies the item
                                # Update the quantity if the item already exists
                                item[1] += si_qty
                                found = True
                                print(f"Updated Quantity for {si.name}: New Quantity = {item[1]}")
                                break
                        
                        if not found:
                            # If item is not found, add it to the list as a new entry
                            supplementary_list.append((si, si_qty))
                            print(f"Item added to order! Supplementary ID: {si.ID}, Name: {si.name}, Quantity: {si_qty}, Unit Price: {si.price}")
                    if not Operations.validate_asking_supplementary_2():
                        break
            # return the final list of (si, qty)
            return supplementary_list

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
                "Enter the supplementary item ID (e.g., Car Park, Breakfast, Tooth paste, Shampoo):\n"
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

    def check_exist_guest(self):
        if self.records.find_guest(self.guest_name):
            return True
        else:
            return False
        
    def get_si_sub_total(self):
        sub_total = 0
        if self.supplementary_list:
            for item, qty in self.supplementary_list:
                cost = item.price * qty
                sub_total += cost
        return sub_total
    @staticmethod
    def confirm_claim_discount():
        while True:
            confirm = input("Do you want to use point to claim for discount?: (y/n)\n")
            if confirm.lower() in ['y', 'n']:
                    return confirm.lower() == 'y'
            print("Invalid answer. Please answer 'y' or 'n' only\n")
    
    
    
    
    def calculate_extra_beds(self, number_guest):
        # Calculate the number of extra beds required based on the number of guests.
        if number_guest > 2:
            return number_guest - 2  # Assuming 2 guests can fit without extra beds.
        return 0

    def calculate_car_park(self, length_stay):
        # Calculate the number of car park spaces required based on the length of stay.
        return length_stay  # Assuming 1 car park spot is needed for each night of stay.
    
    def validate_guest_capacity(self, number_guest, apartment_capacity, length_stay):
        """
        Validates the number of guests against the apartment capacity.
        If the number of guests exceeds the capacity, suggest extra beds.
        Each extra bed can accommodate 2 guests, and a maximum of 2 extra beds can be added.
        The number of extra beds ordered must be at least the same as the number of nights.
        """
        if number_guest <= apartment_capacity:
            # No extra beds needed
            return 0

        # Calculate extra guests that cannot be accommodated by the apartment's capacity
        extra_guests = number_guest - apartment_capacity

        # Determine the number of extra beds needed (each bed can accommodate 2 guests)
        extra_beds_needed = (extra_guests + 1) // 2  # Rounds up to cover all extra guests

        # Check if the total extra beds needed exceeds the maximum allowed (2 beds) / day
        if extra_beds_needed > 2: # per day
            print(f"Error: The number of extra beds needed exceeds the maximum of 2 beds. Booking cannot proceed.")
            return None  # Indicates booking cannot proceed

        # Adjust extra beds needed to match or exceed the number of nights
        #if extra_beds_needed < length_stay:
        #print(f"Note: The number of extra beds must be at least {length_stay} to match the number of nights.")
        #extra_beds_needed = length_stay * extra_beds_needed_per_day

        # Multiply the number of extra beds by the number of nights to reflect per-night pricing
        total_extra_beds = extra_beds_needed * length_stay

        # Display a message suggesting extra beds
        print(f"Warning: The number of guests exceeds the apartment capacity by {extra_guests} guests.")
        print(f"Please consider ordering {total_extra_beds} extra bed(s) to accommodate the extra guests for {length_stay} night(s).")

        # Prompt the user to confirm or cancel the addition of extra beds
        confirm_extra_beds = Operations.confirm_order()
        if not confirm_extra_beds:
            print("Booking cancelled as extra beds were not confirmed.")
            return None  # Indicates booking cannot proceed

        
        return total_extra_beds
    
    def set_reward_rate(self):
        while True:
            try:
                new_reward_rate = float(input("Enter new reward rate for all guests (positive number greater than 0): ").strip())
                # Validate that the input is a positive number greater than zero
                if new_reward_rate <= 0:
                    raise ValueError("Reward rate must be greater than 0.")
                # Update the reward rate
                Guest.set_reward_rate(new_reward_rate)
                break
            except ValueError as e:
                # Handle invalid input and re-prompt the user
                print(f"Invalid input: {e}. Please enter a valid positive number.")
    def set_redeem_rate(self):
        while True:
            try:
                new_redeem_rate = float(input("Enter new reward redeem rate for all guests (positive number greater than 0): ").strip())
                # Validate that the input is a positive number greater than zero
                if new_redeem_rate <= 0:
                    raise ValueError("Redeem rate must be greater than 0.")
                # Update the redeem rate
                Guest.set_redeem_rate(new_redeem_rate)
                break
            except ValueError as e:
                # Handle invalid input and re-prompt the user
                print(f"Invalid input: {e}. Please enter a valid positive number.")





    # disply total receipt after making a book apartment from menu 1
    def display_receipt(self):
        print("="*70)
        print(f"{'Pythonia Service Apartment - Booking Receipt':^70}")
        print("="*70)
        print(f"{'Guest name:':<20} {self.guest_name}")
        print(f"{'Number of guests:':<20} {self.number_guest}")
        print(f"{'Apartment name:':<20} {self.apartment_name}(auto-complete based on id)")
        print(f"{'Apartment_rate:$':<20} {self.apartment_rate:.2f}(AUD) (auto-complete based on id)")
        print(f"{'Check-in date:':<20} {self.checkin_date}")
        print(f"{'Check-out date:':<20} {self.checkout_date}")
        print(f"{'Length of stay:':<20} {self.length_stay}(night)")
        print(f"{'Booking date:':<20} {self.booking_date}\n")
        print(f"{'Sub-total:$':<20} {self.apartment_sub_total}(AUD)")
        # print part supplemetary items
        if self.supplementary_list:
            print("-"*70)
            print(f"{'Supplementary items':<20}")
            print(f"{'ID':<10} {'Name':<20} {'Quantity':<10} {'Unit Price $':<15} {'Cost $':<10}")

            for si, qty in self.supplementary_list:
                id = si.ID
                name = si.name
                qty = qty
                unit_price = si.price
                cost = si.price * qty

                print(f"{id:<10} {name:<20} {qty:<10} {unit_price:<15.2f} {cost:<10.2f}")

            print(f"{'Sub-total:$':<20} {self.supplementary_item_sub_total}(AUD)")
            print("-"*70)
        print(f"{'Total cost:$':<20} {self.cost_result['original_total_cost']}(AUD)")
        print(f"{'Reward points to redeem:':<20} {self.cost_result['redeem_point']}(points)")
        print(f"{'Discount based on points: $':<20} {self.cost_result['discount']}(AUD)")
        print(f"{'Final total cost: $':<20} {self.cost_result['final_total_cost']}(AUD)")
        print(f"{'Earned rewards: ':<20} {self.cost_result['reward']}(points)")
        print("")
        print(f"{'Thank you for your booking!':<20}")
        print(f"{'We hope you will have an enjoyable stay.':<20}")
        print("="*70)

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
    
    def display_bundle(self):
        return self.records.list_product("bundle")
    def display_order_history(self):
        try:
            name = input("Enter the name of the guest to show history booking:") # input name
            # check name in history
            if self.records.find_guest(name):
                orders = self.records.find_order(name)
                self.records.order_history(name, orders)
            else:
                # if not find print message
                print(f"Guest's name {name} not found. Please enter tha valid guest's name")   
        except ValueError as e:
            print("Error! order_history: {e}")
    def exit():
        
        print()

class Statistics:
    def __init__(self,orders):
        self.orders = orders
    
    def generate_key_stat(self):
        # top 3 top spender guest booking so far
        top3_guests = self.get_top3_guests()
        print("\n--- Top 3 Most Top Spender Guest ----")
        for guest, total in top3_guests:
            print(f"Guest: {guest}, Total Amout: ${total:.2f}")

        # top 3 Popular products show name and quantity
        top3_products = self.get_top3_products()
        print("\n--- Top 3 Most Pupular Products ---")
        for product, quantity in top3_products:
            print(f"Product: {product}, Quantity Sold: {quantity}")

        # save to file 'stats.txt'
        # Save the results to stats.txt
        self.save_to_file(top3_guests, top3_products)
    # Get top 3 Guest base on their total order amounts
    # Return List of tuples containing (guest_name, total_order_amount)
    def get_top3_guests(self):
        guest_totals= {}

        for order in self.orders:
            guest_name = order.guest_name
            total_amount = order.total_cost 

            if guest_name in guest_totals:
                guest_totals[guest_name] += total_amount
            else:
                guest_totals[guest_name] = total_amount

        # Sort guests by total order amount in descending order and get top 3
        top_guests = sorted(guest_totals.items(), key=lambda x: x[1], reverse=True)[:3]
        return top_guests
    def get_top3_products(self):
        """
        Calculate and return the top 3 most popular products based on sold quantity.
        :return: List of tuples containing (product_name, total_sold_quantity).
        """
        product_quantities = {}
        for order in self.orders:
            # Extract product names and their quantities from the order
            for item in order.products:
                product_id = item["product_id"]
                quantity = item["quantity"]

                if product_id in product_quantities:
                    product_quantities[product_id] += quantity
                else:
                    product_quantities[product_id] = quantity

        # Sort products by total quantity sold in descending order and get top 3
        top_products = sorted(product_quantities.items(), key=lambda x: x[1], reverse=True)[:3]
        return top_products
    
    def save_to_file(self, top_guests, top_products):
        """
        Save the key statistics to a file called stats.txt.
        :param top_guests: List of tuples containing top 3 most valuable guests.
        :param top_products: List of tuples containing top 3 most popular products.
        """
        with open("stats.txt", "w") as file:
            # Write Top 3 Most Valuable Guests
            file.write("--- Top 3 Most Valuable Guests ---\n")
            for guest, total in top_guests:
                file.write(f"Guest: {guest}, Total Order Amount: ${total:.2f}\n")

            # Write Top 3 Most Popular Products
            file.write("\n--- Top 3 Most Popular Products ---\n")
            for product, quantity in top_products:
                file.write(f"Product: {product}, Quantity Sold: {quantity}\n")

            print("\nKey statistics have been saved to stats.txt.")
    
    


records = Records()
guest_file = records.read_guests("guests.csv")
product_file = records.read_product("products.csv")
order_file = records.read_orders("orders.csv")

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
    while True:
        operations.display_menu()

