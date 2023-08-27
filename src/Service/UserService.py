from OOP.Repository.Repository import Repository


class UserService(object):
    def __init__(self):
        self.__all_users = []
        self.__repository = Repository()

    def register_user(self, user):
        self.__all_users.append(user)

        # Registering a seller

    def register_seller(self, seller_id):
        self.__all_products[seller_id] = []

    def get_all_seller_and_products(self):
        return self.__all_products

    def get_all_users(self):
        return self.__all_users

    def pay_seller(self, seller_id, amount):
        seller_obj = self.__all_users[seller_id - 1]
        seller_obj.pay_seller(amount)