
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
            setUp() method allows us to define instructions that will 
            be executed before each test method
        """
        self.new_user = User("jLuseno161","joy161")
