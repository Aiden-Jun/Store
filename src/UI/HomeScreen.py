from src.Service.Service import Service


class HomeScreen(object):
    def __init__(self):
        self.service = Service()
        self.me = None

    def home(self, me):
        """
        # 구매자의 이메일과 구매했던 상품 목록 아이디와 이름 리스트, 계좌의 잔액을 표시하세요
        # 판매되고 있는 모든 상품 목록 아이디와 이름 리스트를 표시하세요
        # 구매하고자 하는 상품 아이디를 입력받는 UI를 보여주세요
        # 상품 아이디를 입력하면 상품을 구매합니다
        :param me:
        :return:
        """
        print('This is main screen (Not done YET)')
        self.me = me
        if me['user_type'] == 'buyer':
            self.buyer_main_ui()

    def buyer_main_ui(self):
        print(f'buyer, 이메일: {self.me["email"]}, 잔액: {self.me["money"]}')
        bought_products = self.service.get_product_service().get_buy_products(self.me['user_id'])
        for bought_product in bought_products:
            print(f"{bought_product.get('product_id')},{bought_product.get['product_name']}")
        selling_products = self.service.get_product_service().get_selling_products()
        print("==============================================================")
        for bought_product in bought_products:
            print(f"판매중인 상품: {bought_product.get('product_id')},{bought_product.get['product_name']}")
        print("==============================================================")
        choice = input("구매할 상품의 아이디를 입력하세요: ")
