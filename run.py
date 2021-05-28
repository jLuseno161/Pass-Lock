#!/usr/bin/env python3.8

from user import User


def create_user(username, password):
    '''
    Function to create a new contact
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
    Function that finds a contact by number and returns the contact
    '''
    return User.findbyname(username, password)


def check_existing_user(username, password):
    '''
    Function that check if a user exists with username and password and returns a Boolean
    '''
    return User.user_exist(username, password)


def main():
    print(f"Welcome to Pass Lock, where helping you save and remember your passwords is our priority. \n Please create Account:")
    print("Enter your username")
    username = input()

    print("Enter your password")
    password = input()

    save_user(create_user(username, password))
    print('\n')
    print(f"Hello {username}, Thank you for creating an account with us.")
    print('\n')
    print("Please Login in to continue")

    print("Enter your username")
    user_name = input()

    print("Enter your username")
    pass_word = input()

    if check_existing_user(user_name, pass_word):
        fetch_user = find_user(user_name, pass_word)
        print(f"{fetch_user.username} {fetch_user.password}")

    else:
        print("That contact does not exist")


if __name__ == '__main__':

    main()
