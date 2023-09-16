class Product(object):
    def __init__(self, product_id, product_name, description, product_price, is_selling, seller_id, buyer_id):
        self._product_id = int(product_id)
        self._product_name = product_name
        self._description = description
        self._product_price = int(product_price)
        self._selling_status = bool(is_selling)
        self._seller_id = seller_id
        self._buyer_id = buyer_id

    def get_product_id(self):
        return self._product_id

    def get_product_name(self):
        return self._product_name

    def get_product_description(self):
        return self._description

    def get_product_price(self):
        return self._product_price

    def get_product_seller_id(self):
        return self._seller_id

    def is_product_selling(self):
        if self._selling_status:
            return True
        else:
            return False

    def get_buyer_id(self):
        return self._buyer_id

    def sold(self, buyer_id):
        self._selling_status = True
        self._buyer_id = buyer_id

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
