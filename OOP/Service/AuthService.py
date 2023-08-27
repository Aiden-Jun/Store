from OOP.Repository.Repository import Repository


class AuthService(object):
    def __init__(self):
        self.__repository = Repository()

    def does_this_email_exist(self, email):
        user = self.__repository.find_user_by_email(email)
        if user:
            return True
        else:
            return False

    def add_user(self, email, password, name, user_type):
        self.__repository.add_user(email, password, name, user_type)

    def get_user(self, email, password):
        user = self.__repository.find_user_by_email_and_password(email, password)
        if user != None and user.get_password() == password:
            return user

        return None
