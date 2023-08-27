# Create User Class
class User(object):
    __user_creation_number = 0

    @classmethod
    def add_user_id(cls):
        cls.__user_creation_number += 1

    # Magic Method: Functions that runs automatically
    # Gets User Information
    def __init__(self, email, password, name, balance):  # Manager class object is passed in
        # Setting User Information
        self._email = email
        self._password = password
        self._name = name

        # self._manager = manager
        User.add_user_id()
        self._user_id = User.__user_creation_number

        # Not assigned value when User object is created
        self.__balance = balance
        # Add to Manager's database
        # self._manager.register_user(self)

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_name(self):
        return self._name

    def set_card(self, card):
        self._card = card

    def get_user_id(self):
        return self._user_id

    def get_balance(self):
        if self._card != None:  # Preventing Error
            return self._card.get_card_balance()

    def change_balance(self, new_balance):
        if self._card != None:  # Preventing Error
            self._card.set_balance(new_balance)

    def get_card_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def income(self, amount):
        self.__balance += amount

    def expense(self, amount):
        self.__balance -= amount


if __name__ == "__main__":
    pass
