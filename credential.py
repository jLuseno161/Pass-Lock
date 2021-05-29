class Credential:
    """
        Class generates new instance of credentials
    """

    credential_list = []

    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password

    def save_account(self):
        Credential.credential_list.append(self)

    # def account_exist(cls, account_name,username, password):
    #     '''
    #     Method that checks if a account exists from the credentials list.
    #     Args:
    #         string: account name to search if it exists
    #     Returns :
    #         Boolean: True or false depending if the account exists
    #     '''
    #     # for user in cls.user_list:
    #     #     if user.username == username and user.password == password:
    #     #         return True
    #     for account in cls.credential_list:
    #         if account.account_name == account_name:
    #             return True

    #     return False

    @classmethod
    def findbyname(cls, account_name):
        for account in cls.credential_list:
            if account.account_name == account_name:
                return account
