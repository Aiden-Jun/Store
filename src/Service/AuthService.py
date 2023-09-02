from src.Repository.Repository import Repository


class AuthService(object):
    def __init__(self):
        self.__repository = Repository()

    def does_this_email_exist(self, email):
        user_repository = self.__repository.get_user_repository()
        user = user_repository.find_user_by_email(email)
        if user:
            return True
        else:
            return False

    def add_user(self, email, password, name, user_type):
        user_repository = self.__repository.user_repository()
        user_repository.add_user(email, password, name, user_type)

    def get_user(self, email, password):
        user_repository = self.__repository.user_repository()
        user = user_repository.find_user_by_email_and_password(email, password)
        if user is not None and user.get_password() == password:
            return user.convert_domain_to_dto()
        return None

    def change_name(self, email, password, new_name):
        user_repository = self.__repository.get_user_repository()
        user = user_repository.find_user_by_email_and_password(email, password)
        if user is None:
            return {'message': "유저가 없습니다"}
        user.change_name(new_name)
        return {'message': "이름이 변경되었습니다"}
