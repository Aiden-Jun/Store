from Repository.Repository import Repository


class ProductService(object):
    def __init__(self):
        self.__all_products = {}
        self.__repository = Repository()

    def get_products_list_of_user_id(self, user_id):
        return self.__all_products[user_id]

    def get_all_seller_and_products(self):
        return self.__all_products

    def get_product_object(self, seller_id, product_index):
        return self.__all_products[seller_id][product_index]

    def add_product(self, seller_id, product):
        self.__all_products[seller_id].append(product)

    def delete_product(self, seller_id, product_index):
        self.__all_products[seller_id].pop(product_index)
