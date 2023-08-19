from oop.Infrastructure.Repository import Repository


class Manager(object):
    def __init__(self):
        self.__all_products = {}
        self.__all_users = []
        self.__repository = Repository()

    def register_user(self, user):
        self.__all_users.append(user)

    # Registering a seller
    def register_seller(self, seller_id):
        self.__all_products[seller_id] = []

    def get_products_list_of_user_id(self, user_id):
        return self.__all_products[user_id]
    
    def get_all_seller_and_products(self):
        return self.__all_products

    def get_all_users(self):
        return self.__all_users

    def get_product_object(self, seller_id, product_index):
        return self.__all_products[seller_id][product_index]

    def add_product(self, seller_id, product):
        self.__all_products[seller_id].append(product)

    def delete_product(self, seller_id, product_index):
        self.__all_products[seller_id].pop(product_index)

    def pay_seller(self, seller_id, amount):
        seller_obj = self.__all_users[seller_id-1]
        seller_obj.pay_seller(amount)