from Database import Database


class Auth(object):
    def __init__(self):
        self.choice = None
        self.__db = Database()

    def find_user(self, email, password):
        user = self.__db.get_user('users.csv', email)
        if user != None:
            if user[1] == password:
                return user
        return None

    def add_user(self, email, password, name, type):
        self.__db.add_user_row(email, password, name, type)

    def does_this_email_exist(self, email):
        self.__db.check_email_existence(email)