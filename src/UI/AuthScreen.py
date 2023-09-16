from src.Service.Service import Service


class AuthScreen(object):
    def __init__(self):
        self.service = Service()

    def show_option_prompt(self):
        print('Sign In (login)')
        print('Sign Up (create)')
        choice = input('>').lower()
        return choice

    def sign_in(self):
        print('\nSign In')

        print('Email')
        entEmail = input('>')

        print('\nPassword')
        entPassword = input('>')

        user = self.service.get_auth_service().get_user(entEmail, entPassword)
        if user is not None:
            print(f"Hello {user['name']}")
            return user
        return None

    def sign_up(self):
        print('\nSign Up')

        print('What kind of user are you? (buyer/seller)')
        userType = input('>').lower()

        if userType != 'buyer' and userType != 'seller':
            print('Try Again!')
            return False

        print('Email')
        entEmail = input('>')

        if self.service.get_auth_service().does_this_email_exist(entEmail):
            print('Email provided already exists, try again')
            return False

        print('\nPassword')
        entPassword = input('>')

        print('\nRe-Enter Password')
        reEntPassword = input('>')

        if entPassword != reEntPassword:
            print('No your passwords does not match')
            print('Try again')
            return False

        print('\nName')
        entName = input('>')

        self.service.get_auth_service().add_user(entEmail, entPassword, entName, userType)
        print('Done, now sign in')

        return True
