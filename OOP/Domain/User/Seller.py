# Class Seller (Child of User)
# It will later be child of Buyer
# It's because seller should also be able to buy
from OOP.Domain.User.User import User


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


if __name__ == "__main__":
    pass
