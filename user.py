class User:

    """
        Class that generates new instances of user
    """
    user_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        """ append new user to list"""
        User.user_list.append(self)

    @classmethod
    def user_exist(cls, username, password):
        '''
        Method that checks if a user exists from the user list.
        Args:
            string: username to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return True

        return False

    @classmethod
    def findbyname(cls,  username, password):
        """ Method to find user by searching their name"""
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return user
