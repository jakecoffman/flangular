import unittest
import users


class UsersTest(unittest.TestCase):
    def setUp(self):
        self.users = users.UserAPI()

    def tearDown(self):
        pass

    def test_list(self):
        self.users.get()