from oop.Service.AuthService import Auth
from oop.Service.Manager import Manager


class Store:
    def __init__(self):
        self.auth = Auth()
        self.manager = Manager()
        self.start_ui()

    def start_ui(self):
        print('Sign In (login)')
        print('Sign Up (create)')
        choice = input('>').lower()

        if choice == 'login':
            self.sign_in_ui()
        else:
            self.sign_up_ui()

    def sign_up_ui(self):
        print('\nSign Up')

        print('What kind of user are you? (buyer/seller)')
        userType = input('>').lower()

        if userType != 'buyer' and userType != 'seller':
            print('Try Again!')
            self.sign_up_ui()

        print('Email')
        entEmail = input('>')

        if self.auth.does_this_email_exist(entEmail):
            print('Email provided already exists, try again')
            self.start_ui()

        print('\nPassword')
        entPassword = input('>')

        print('\nRe-Enter Password')
        reEntPassword = input('>')

        if entPassword != reEntPassword:
            print('No your passwords does not match')
            print('Try again')
            self.sign_up_ui()

        print('\nName')
        entName = input('>')

        self.auth.add_user(entEmail, entPassword, entName, userType)
        print('Done, now sign in')

        self.start_ui()

    def sign_in_ui(self):
        print('\nSign In')

        print('Email')
        entEmail = input('>')

        print('\nPassword')
        entPassword = input('>')

        find_user = self.auth.find_user(entEmail, entPassword)
        if find_user is not None:
            print(f'Welcome back {find_user[2]}!')
            self.main_ui()
        else:
            print('Email or password is incorrect')
            print('Please try again')
            self.sign_in_ui()

    def main_ui(self):

        print('This is main screen (Not done YET)')


# This runs when Main.py is not imported
if __name__ == '__main__':
    store = Store()
