class Product(object):
    __product_creation_number = 0

    @classmethod
    def add_user_id(cls):
        cls.__product_creation_number += 1


    def __init__(self, product_name, description, product_price, seller_id):
        self.__product_name = product_name
        self.__description = description
        self.__product_price = product_price
        self.__seller_id = seller_id

        self.add_user_id()
        self._user_id = self.__product_creation_number

    def get_product_name(self):
        return self.__product_name
    
    def get_product_description(self):
        return self.__description

    def get_product_price(self):
        return self.__product_price
    
    def get_product_seller_id(self):
        return self.__seller_id