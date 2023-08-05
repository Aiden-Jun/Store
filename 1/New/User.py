user_creation_number = 0

# Create User Class
class User(object):
    # Magic Method: Functions that runs automatically
    # Gets User Information
    def __init__(self, email, password, name, manager): # Manager class object is passed in
        # Setting User Information
        self._email = email
        self._password = password
        self._name = name

        self._manager = manager

        global user_creation_number
        user_creation_number += 1

        self._user_id = user_creation_number

        # Not assigned value when User object is created
        self._card = None

        # Add to Manager's database
        self._manager.register_user(self)

    def get_email(self):
        return self._email
    
    def get_name(self):
        return self._name
    
    def set_card(self, card):
        self._card = card
    
    def get_user_id(self):
        return self._user_id
    
    def get_balance(self):
        if self._card != None: # Preventing Error
            return self._card.get_card_balance()
    
    def change_balance(self, new_balance):
        if self._card != None: # Preventing Error
            self._card.set_balance(new_balance)
        

# Class Buyer (Child of User)
class Buyer(User):
    # Magic Method
    def __init__(self, email, password, name, manager):
        # Use parent class
        super().__init__(email, password, name, manager)

        # History
        self.__history = []
        self.__cart = []

    def add_to_cart(self, seller_id, product_index):
        self.__cart.append(str(seller_id)+':'+str(product_index))
    
    def empty_cart(self):
        self.__cart = []
    
    def get_cart(self):
        return self.__cart

    def remove_item_from_cart(self, item_index):
        self.__cart.pop(item_index)

    def get_history(self):
        return self.__history

    # sellerid:product_index
    def buy_cart(self):
        for item_code in self.__cart:
            seller_id = item_code[:item_code.find(':')]
            product_index = item_code[item_code.find(':')+1:]

            product_obj = self._manager.get_product_object(int(seller_id), int(product_index))
            price = product_obj.get_product_price()

            self._manager.pay_seller(int(seller_id), price)
            self._card.expense(price)

            # Add to History
            self.__history.append(product_obj)

            self._manager.delete_product(int(seller_id), int(product_index))


# Class Seller (Child of User)
# It will later be child of Buyer
# It's because seller should also be able to buy
class Seller(User):
    # Magic Method
    def __init__(self, email, password, name, phone_number, manager):
        # Calls parent
        super().__init__(email, password, name, manager)
        self.__phone_number = phone_number

        # Register Seller using id
        self._manager.register_seller(self._user_id)

    def get_phone_number(self):
        return self.__phone_number
    
    def add_product(self, product):
        self._manager.add_product(self._user_id, product)

    def pay_seller(self, amount):
        self._card.income(amount)