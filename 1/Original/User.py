# 객체 지향 프로그래밍(Object Oriented Programming)
import random
from Product import Product
from Card import Card
from Manager import Manager

# 객체(Object, Instance)
class User(object):
    # 데이터: 인스턴스 변수
    # 데이터를 다루는 함수: 인스턴스 메소드
    # 매직 메소드: 특별한 상황이 되면 누가 시키지 않아도 자동으로 실행되는 함수

    # 매직 메소드: 생성자(constructor): 객체가 생성될 때 자동으로 호출되는 함수
    def __init__(self, name, email, password):
        # 인스턴스 변수
        # 접근 제어자: private, protected
        # _인스턴스변수: protected 변수: 다른 객체에서 이 변수를 직접 변경할 수 없도록 만든다. 단, 자식은 허용
        # __인스턴스변수: private 변수: 다른 객체에서 이 변수를 직접 변경할 수 없도록 만든다
        self._id = random.randint(0,1000000000000000000)
        self._name = name
        self.__email = email
        self.__password = password
        self.__card = None

    # 인스턴스 메소드
    def get_name(self):
        return self._name

    def get_email(self):
        return self.__email
    
    def get_id(self):
        return self._id

    def set_name(self, new_name):
        self.__name = new_name

    def set_email(self, new_email, password):
        if self.__password == password:
            self.__email = new_email

    def set_card(self, card):
        self.__card = card


class Seller(User):
    # 오버라이드: 부모 클래스에서 상속해 준 함수를 자식 클래스에서 재정의 하는 경우
    def __init__(self, name, email, password, phone_number, money, manager):
        self.manager = manager
        # 일단 부모님꺼는 다 그대~로 쓰고
        super().__init__(name, email, password)
        # 추가로 내가 할 일
        self.__phone_number = phone_number
        self.__money = money


        self.manager.register_seller(self.get_id())
        

    # 오버라이드: 부모 클래스에서 상속해 준 함수를 자식 클래스에서 재정의 하는 경우
    def get_name(self):
        return '셀러 ' + self._name + ' 입니다'
    
    def get_id(self):
        return self._id
    
    def add_product(self, product):
        self.manager.add_product(self._id, product)

    def access_product(self, product_index):
        return self.manager.view_product(product_index, self.get_id())
    
    def pay_seller(self, amount):
        self.__card.income(amount)
        


class Buyer(User):
    def __init__(self, name, email, password, manager):
        super().__init__(name, email, password)
        self.__card = None
        self.__cart = []
        self.__history = []
        self.manager = manager

    def get_name(self):
        return '바이어 ' + self._name + ' 입니다'
    
    def set_card(self, card):
        self.__card = card

    def add_to_cart(self, product_index, seller_id):
        self.__cart.append(self.manager.view_product(product_index, seller_id))

    def empty_cart(self):
        self.__cart = []

    def buy_cart(self):
        for item in self.__cart:
            self.__card.expense(item.price)
            item.seller.pay_seller(item.price)
            self.__history.append(item)
            


            


if __name__ == "__main__":
    pass