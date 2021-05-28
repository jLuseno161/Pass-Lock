
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
        self.new_user.save_user()  # add user to list
        self.assertEqual(len(User.user_list), 1)  # check length of list

#test 3 - if object actually exists
    def test_user_exits(self):
        self.new_user.save_user()
        check_user = User("jLuseno161","joy161")
        check_user.save_user()
        user_exists = User.user_exist("jLuseno161","joy161")
        self.assertTrue(user_exists)

if __name__ == '__main__':
    unittest.main()
