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
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_account.save_account()
        test_contact = Credential(
            "Instagram", "jLuseno161", "joy161")  # new contact
        test_contact.save_account()
        self.assertEqual(len(Credential.credential_list), 2)


if __name__ == '__main__':
    unittest.main()
