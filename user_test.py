
import unittest
from user import User


class LoginTest(unittest.TestCase):
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
        self.new_user = User("jLuseno161", "joy161")

    def test_init(self):
        """
            test to check for correct instantion of objects
        """
        self.assertEqual(self.new_user.username, "jLuseno161")
        self.assertEqual(self.new_user.password, "joy161")

# Test 2 - save created account's credentials

    def test_save_user(self):
        """
            test if new user has been saved to the new user_list
        """
        self.new_user.save_user()
        self.assertEqual(User.user_list, 1)

if __name__ == '__main__':
    unittest.main()
