class Product(object):
    __product_creation_number = 0

    @classmethod
    def add_user_id(cls):
        cls.__product_creation_number += 1

    def __init__(self, product_id, product_name, description, product_price, is_selling, seller_id, buyer_id):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__product_price = int(product_price)
        self.__seller_id = seller_id
        self.__selling_status = int(is_selling)
        self.__buyer_id = buyer_id

        self.add_user_id()
        self._user_id = self.__product_creation_number

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_product_description(self):
        return self.__description

    def get_product_price(self):
        return self.__product_price

    def get_product_seller_id(self):
        return self.__seller_id
    
    def is_product_selling(self):
        if self.__selling_status == 1:
            return True
        else:
            return False
    
    def get_buyer_id(self):
        return self.__buyer_id

    def convert_dto(self):
        return {
            'product_id': self.get_product_id(),
            'product_name': self.get_product_name(),
            'description': self.get_product_description(),
            'product_price': self.get_product_price(),
            'is_selling': self.get_product_id(),
            'seller_id': self.get_product_seller_id(),
            'buyer_id': self.get_product_id,
        }


if __name__ == "__main__":
    pass
