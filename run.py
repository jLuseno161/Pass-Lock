#!/usr/bin/env python3.8
from user import User
from credential import Credential
import random
import string
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
    credential.save_account()


def find_account(account_name):
    '''
    Function that finds a account by account_name and returns the account
    '''
    return Credential.findby_account_name(account_name)


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


def display_account():
    '''
    Function that returns all the saved accounts
    '''
    return Credential.display_account()

    # MAIN FUNCTION


# def get_account():


def response_none(question):
    """Users response on whether to generate password or not"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def main():
    print(f"Welcome to Pass Lock,helping you save and remember your passwords is our priority.")
    print("Please create Account:")
    print('\n')

    print("Enter your new username")
    username = input()
    print("Enter your new password")
    password = input()
    save_user(create_user(username, password))
    print('\n')

    refresh()

    print(f"Hello {username}, Thank you for creating an account with us.")

    print("Proceed to Login")
    print('\n')

    print("Enter your username:")
    user_name = input()

    print("Enter your password:")
    pass_word = input()
    print('\n')

    if check_existing_user(user_name, pass_word):
        fetch_user = find_user(user_name, pass_word)
        # print(f"{fetch_user.username} {fetch_user.password}")

        while True:
            print("Use these short codes :log ca - create a new account credential, da - display account, fa -find an account,dl - delete account, ex -exit the account list ")
            # if username == username:
            #     print("")

            short_code = input().lower()

            if short_code == 'ca':
                print("New Credential Account")
                print("-"*10)

                print("Account Name ....")
                account_name = input()

                print("Username ...")
                username = input()

                """Determine if generate or not"""
                generate = response_none(
                    "Would you like us to generate a password for you? (y/n): ")
                if generate == "y":
                    value = 16
                    lower = string.ascii_lowercase
                    upper = string.ascii_uppercase
                    num = string.digits
                    all = lower + upper + num
                    temp = random.sample(all, value)
                    password = "".join(temp)

                else:

                    print("Password ...")
                    password = input()

                # create and save new credential.
                save_account(create_account(account_name, username, password))
                print('\n')
                print(
                    f"New account: {account_name}  with user name : {username} created :{password}")
                print('\n')

            elif short_code == 'da':
                if display_account():
                    print("Here is a list of all your accounts")
                    print('\n')

                    for credential in display_account():
                        print(
                            f"{credential.account_name} |   {credential.username} |   {credential.password}")

                else:
                    print('\n')
                    print("You dont seem to have any accounts saved yet")
                print('\n')

            elif short_code == 'fa':
                print("Enter the account name you want to search for")

                search_account = input()
                if check_existing_account(search_account):
                    check_account = find_account(search_account)
                    print(f"{check_account.account_name}")
                    print('-' * 20)

                    print(f"Account Name.......{check_account.account_name}")
                    print(f"Username.......{check_account.username}")
                else:
                    print("That account does not exist")
                print('\n')

            elif short_code == 'dl':
                print("Enter name of account to delete")
                search_account = input()
                if check_existing_account(search_account):
                    print("Please wait ...")
                    check_account = find_account(search_account)
                    delete_account(check_account)
                    print(
                        f"Account {check_account.account_name}deleted successfully")
                else:
                    print('\n')
                    print("You dont seem to have any accounts saved yet")

            elif short_code == "ex":
                print("Bye .......")
                break
            else:
                print("I really didn't get that. Please use the short codes")
    else:
        print("That account does not exist. Please create one")
        print('\n')

        main()

    print('\n')


if __name__ == '__main__':

    main()
