class Card(object):
    def __init__(self, card_number, balance, card_pin):
        self.__card_number = card_number
        self.__balance = balance
        self.__card_pin = card_pin

    def get_card_balance(self):
        return self.__balance
    
    def set_balance(self, new_balance):
        self.__balance = new_balance

    def income(self, amount):
        self.__balance += amount

    def expense(self, amount):
        self.__balance -= amount