from Database import Database


class Auth(object):
    def __init__(self):
        self.choice = None
        self.__email = None
        self.__password = None
        self.__name = None
        self.__user = None
        self.__db = Database()

    def show_prompt(self):
        self.choice = int(input("로그인(0) vs 회원가입(1): "))
        if self.choice == 0:
            self.show_login_prompt()
        else:
            self.show_sign_up_prompt()

    def show_login_prompt(self):
        self.__email = input("이메일을 입력하세요: ")
        self.__password = input("비밀번호를 입력하세요: ")
        user = self.find_user(self.__email, self.__password)
        if user == None:
            print("이메일 혹은 비밀번호가 일치하지 않습니다")
            self.show_prompt()
        else:
            self.__user = user
            print(self.__user)

    def show_sign_up_prompt(self):
        self.__email = input("이메일을 입력하세요: ")
        self.__password = input("비밀번호를 입력하세요: ")
        self.__name = input("이름을 입력하세요: ")
        self.__name = input("셀러 vs 바이어 선택하세요: ")

    def find_user(self, email, password):
        user = self.__db.get_user('users.csv', email)
        if user and user[1] == password:
            return user
        return None
