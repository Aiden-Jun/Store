import random

class Product(object):
    def __init__(self, title, content, price, seller):
        self.title = title
        self.content = content
        self.price = price
        self.seller = seller
        self.id = random.randint(0,1000000000000000000)

    def __str__(self):
        return self.title + str(self.id)
    




if __name__ == "__main__":
    pass
