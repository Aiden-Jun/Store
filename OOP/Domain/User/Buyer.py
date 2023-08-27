# Class Buyer (Child of User)
from OOP.Domain.User.Seller import User


class Buyer(User):
    # Magic Method
    def __init__(self, email, password, name, manager):
        # Use parent class
        super().__init__(email, password, name, manager)

        # History
        self.__history = []
        self.__cart = []

    def add_to_cart(self, seller_id, product_index):
        self.__cart.append(str(seller_id) + ':' + str(product_index))

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
            product_index = item_code[item_code.find(':') + 1:]

            product_obj = self._manager.get_product_object(int(seller_id), int(product_index))
            price = product_obj.get_product_price()

            self._manager.pay_seller(int(seller_id), price)
            self._card.expense(price)

            # Add to History
            self.__history.append(product_obj)

            self._manager.delete_product(int(seller_id), int(product_index))


if __name__ == "__main__":
    pass
