class Credential:
    """
        Class generates new instance of credentials
    """

    credential_list = []

    def __init__(self, account_name, username, password):
        """Constructor for objects credential"""
        self.account_name = account_name
        self.username = username
        self.password = password

    def save_account(self):
        """Method to append new account the list"""
        Credential.credential_list.append(self)

    @classmethod
    def account_exist(cls, account_name):
        '''
         Method that checks if a account exists from the credentials list.
        Args:
            string: account name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.credential_list:
            if account.account_name == account_name:
                return True

        return False

    @classmethod
    def findby_account_name(cls, account_name):
        """
        method to search account by account name
        """
        for account in cls.credential_list:
            if account.account_name == account_name:
                return account

    def delete_account(self):
        '''
        delete_account method deletes a saved account credentials from the credential_list
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def display_account(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credential_list
