from oop.Infrastructure.Database import Database


class Repository(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            print("리포지토리 객체가 만들어 졌다!")
        return cls.__instance

    def __init__(self):
        print("")
        self.__db = Database()

    def get_user(self, email):
        user_rows = self.__db.read_from_file("users.csv")
        for user_row in user_rows:
            if user_row[0] == email:
                return user_row
        return None
