# Create User Class


class User(object):
    __user_creation_number = 0

    @classmethod
    def add_user_id(cls):
        cls.__user_creation_number += 1

    # Magic Method: Functions that runs automatically
    # Gets User Information
    def __init__(self, user_id, email, password, name, user_type, money,
                 repository):  # Manager class object is passed in
        # Setting User Information
        self._user_id = user_id
        self._email = email
        self._password = password
        self._name = name
        self.repository = repository

        # self._manager = manager
        User.add_user_id()

        # Not assigned value when User object is created
        self.__balance = money
        # Add to Manager's database
        # self._manager.register_user(self)
        self.user_type = user_type

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_name(self):
        return self._name

    def get_user_type(self):
        return self.user_type

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

    def change_name(self, new_name):
        self._name = new_name
        self.repository.update_user_name(self._user_id, new_name)

    def convert_domain_to_dto(self):
        return {
            "user_id": self.get_user_id(),
            "email": self.get_email(),
            "nickname": self.get_name(),
            "money": self.get_balance(),
            "user_type": self.get_user_type(),
        }


if __name__ == "__main__":
    pass
