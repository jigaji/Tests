import unittest
from ya_authorization import authorization




class TestYandexAuth(unittest.TestCase):


    def test_auth(self):
        auth = authorization(input('Введите логин: '), input('Введите пароль: '))
        self.assertEqual(auth.status_code, 200)


if __name__ == '__main__':
    unittest.main()
