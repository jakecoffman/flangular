import unittest
import users


class UsersTest(unittest.TestCase):
    def setUp(self):
        self.users = users.UserAPI()

    def tearDown(self):
        pass

    def test_list(self):
        print self.users.get(None)

if __name__ == "__main__":
    unittest.main()
