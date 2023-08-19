from User import Seller, Buyer
from Card import Card
from Manager import Manager
from Product import Product
from Auth import Auth

from pwinput import pwinput

class Store:
    def __init__(self):
        self.manager = Manager()
        self.auth = Auth()
        self.start_screen()
    
    def start_screen(self):
        print('Sign In (login)')
        print('Sign Up (create)')
        choice = input('>').lower()
        
        if choice == 'login':
            self.sign_in()
            pass
        else:
            self.sign_up()
    
    def sign_up(self):
        print('\nSign Up')

        print('What kind of user are you? (buyer/seller)')
        userType = input('>').lower()

        if userType == 'buyer' or userType == 'seller':
            pass
        else:
            print('Try Again!')
            self.sign_up()


        print('Email')
        entEmail = input('>')
        
        if self.auth.does_this_email_exist(entEmail):
            print('Email provided already exists, try again')
            self.sign_up()

        print('\nPassword')
        entPassword = pwinput('>')

        print('\nRe-Enter Password')
        reEntPassword = pwinput('>')

        if entPassword != reEntPassword:
            print('No your passwords does not match')
            print('Try again')
            self.sign_up()

        print('\nName')
        entName = input('>')

        self.auth.add_user(entEmail, entPassword, entName, userType)
        print('Done, now sign in')

        self.sign_in()


    def sign_in(self):
        print('\nSign In')
        
        print('Email')
        entEmail = input('>')
        
        print('\nPassword')
        entPassword = pwinput('>')

        try:
            if self.auth.find_user(entEmail, entPassword) != None:
                user_data = self.auth.find_user(entEmail, entPassword)
                print(f'Welcome back {user_data[2]}!')
                self.main_screen()
        except:
            print('Email or password is incorrect')
            print('Please try again')
            self.sign_in()


    def main_screen(self):
        
        print('This is main screen (Not done YET)')


# This runs when Main.py is not imported
if __name__ == '__main__':
    store = Store()