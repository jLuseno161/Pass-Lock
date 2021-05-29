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
