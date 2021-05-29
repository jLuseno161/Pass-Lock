import unittest
from credential import Credential


class CredentialTest(unittest.TestCase):
    """
        Test subclass that inherits from the test case.
        Helps in creating tests
    """
# Test 1 - check for correct instantion of objects

    def setUp(self):
        """
            method that allows us to define instructions that will 
            be executed before each test method
        """
        self.new_account = Credential("Instagram", "jLuseno161", "joy161")

    def test_init(self):
        """
            test to check for correct instantion of objects
        """
        self.assertEqual(self.new_account.account_name, "Instagram")
        self.assertEqual(self.new_account.username, "jLuseno161")
        self.assertEqual(self.new_account.password, "joy161")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

# Test 2 - save created account's credentials

    def test_save_account(self):
        """
            test if new account credential has been saved to the new credential_list
        """
        self.new_account.save_account()  # add account to list
        self.assertEqual(len(Credential.credential_list),
                         1)  # check length of list
# Test 3 - save multiple accounts

    def test_save_multiple_account(self):
        '''
        test_save_multiple_accounts to check if we can save multiple account credential
        objects to our contact_list
        '''
        self.new_account.save_account()
        test_account = Credential(
            "Instagram", "jLuseno161", "joy161")  # new account
        test_account.save_account()
        self.assertEqual(len(Credential.credential_list), 2)

# Test 4 : fetch credentials
    def test_find_account_by_name(self):
        '''
        test to check if we can find a account by account name and display information
        '''
        self.new_account.save_account()
        test_account = Credential(
            "Instagram", "jLuseno161", "joy161")  # new account
        test_account.save_account()

        found_account = Credential.findby_account_name("Instagram")

        self.assertEqual(found_account.username, test_account.username)

# Test 5 : Delete account
    def test_delete_account(self):
        '''
        test_delete_account to test if we can remove an account from our contact list
        '''
        self.new_account.save_account()
        test_account = Credential(
            "Instagram", "jLuseno161", "joy161")  # new account
        test_account.save_account()

        self.new_account.delete_account()  # Deleting a account object
        self.assertEqual(len(Credential.credential_list), 1)

# Test 6: check if object actually exists
    def test_account_exits(self):
        self.new_account.save_account()
        check_account = Credential("Instagram", "jLuseno161", "joy161")
        check_account.save_account()
        account_exists = Credential.account_exist(
            "Instagram", "jLuseno161", "joy161")
        self.assertTrue(account_exists)

# Test 7: display account details


def test_display_all_accounts(self):
    '''
    method that returns a list of all accounts saved
    '''

    self.assertEqual(Credential.display_account(), Credential.credential_list)


if __name__ == '__main__':
    unittest.main()
