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


def check_existing_contacts(string):
    '''
    Function that check if a user exists with username and password and returns a Boolean
    '''
    return User.user_exist(string)
