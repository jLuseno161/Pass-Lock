class Credential:
    """
        Class generates new instance of credential
    """

    credentia_list = []

    def __init__(self,account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password

        