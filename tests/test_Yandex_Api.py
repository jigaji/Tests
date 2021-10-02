import unittest
from unittest.mock import patch
from make_folder_on_yandex import create_folder

class test_Yandex_Api(unittest.TestCase):

    @patch ('builtins.input')
    def test_create_folder(self, mocked_input):
        mocked_input.return_value = 'new'
        self.assertEqual(create_folder(), 201)

    @patch ('builtins.input')
    def test_folder_existance(self, mocked_input):
        mocked_input.return_value = 'new'
        self.assertEqual(create_folder(), 409, 'Папка с таким именем уже существует')

    @patch ('builtins.input')
    def test_token(self, mocked_input):
        mocked_input.return_value = 'new'
        self.assertEqual(create_folder(), 401, 'Токен неверный')

if __name__ == '__main__':
    unittest.main()