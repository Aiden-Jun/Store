class Card(object):
    def __init__(self, card_number, balance, owner):
        self.__card_number = card_number
        self.__balance = balance
        self.__owner = owner

    def income(self, income_amount):
        self.__balance += income_amount
    
    def expense(self, expense_amount):
        self.__balance -= expense_amount