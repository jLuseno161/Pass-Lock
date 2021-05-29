#!/usr/bin/env python3.8
from user import User
from credential import Credential
import os
os.system("clear")

# USER CLASS FUNCTIONS


def create_user(username, password):
    '''
    Function to create a new account
    '''
    new_user = User(username, password)
    return new_user


def save_user(user):
    '''
    Function to save new user
    '''
    user.save_user()


def find_user(username, password):
    '''
    Function that finds a account by number and returns the account
    '''
    return User.findbyname(username, password)


def check_existing_user(username, password):
    '''
    Function that check if a user exists with username and password and returns a Boolean
    '''
    return User.user_exist(username, password)


def refresh():
    os.system("clear")


# CREDENTIALS CLASS FUNCTIONS
def create_account(account_name, username, password):
    '''
    Function to create a new account
    '''
    new_account = Credential(account_name, username, password)
    return new_account


def save_account(credential):
    '''
    Function to save new user
    '''
    credential.save_user()


def find_account(account_name):
    '''
    Function that finds a account by account_name and returns the account
    '''
    return User.findbyname(account_name)


def check_existing_account(account_name):
    '''
    Function that check if an account exists with the account_name and returns a Boolean
    '''
    return Credential.account_exist(account_name)

def delete_account(credential):
    '''
    Function to delete a account
    '''
    credential.delete_account()

    # MAIN FUNCTION


def main():
    print(f"Welcome to Pass Lock,helping you save and remember your passwords is our priority.")
    print('\n')
    print("Please create Account:")
    print('\n')
    print("Enter your new username")
    username = input()
    print('\n')
    print("Enter your new password")
    password = input()

    # if username == "" or password == "":
    #     refresh()
    #     print("please Enter correct ")
    #     username = input()
    # else:
    save_user(create_user(username, password))
    print('\n')

    refresh()

    print(f"Hello {username}, Thank you for creating an account with us.")
    print('\n')
    print("Proceed to Login")
    print('\n')

    print("Enter your username:")
    user_name = input()
    print('\n')

    print("Enter your password:")
    pass_word = input()
    print('\n')

    if check_existing_user(user_name, pass_word):
        fetch_user = find_user(user_name, pass_word)
        print(f"{fetch_user.username} {fetch_user.password}")

    else:
        print("That contact does not exist")


if __name__ == '__main__':

    main()
