import Secretary
import unittest
from unittest.mock import patch

name = []
documents = []
for person in Secretary.documents:
    n = person['name']
    d = person['number']
    name.append(n)
    documents.append(d)
directories = {}
directories.update(Secretary.directories)

class TestSecretary(unittest.TestCase):

     def test_check_document_existance(self):
        self.assertTrue(Secretary.check_document_existance('10006'), 'Документ в наличии')


    @patch('Secretary.input')
    def test_get_doc_owner_name(self, mocked_input):
        mocked_input.return_value = "10006"
        self.assertEqual(Secretary.get_doc_owner_name(), "Аристарх Павлов")


    def test_get_all_doc_owners_names(self):
        self.assertEqual(Secretary.get_all_doc_owners_names(), set(name))

    def test_remove_doc_from_shelf(self):
        self.assertNotIn(Secretary.remove_doc_from_shelf('10006'), documents)

    @patch('Secretary.input')
    def test_add_new_shelf(self, mocked_input):
        mocked_input.return_value = '5'
        self.assertEqual(Secretary.add_new_shelf(), ('5', True))

    @patch('Secretary.input')
    def test_delete_doc(self, mocked_input):
        mocked_input.return_value = '11-2'
        self.assertEqual(Secretary.delete_doc(), ('11-2', True))

    @patch('Secretary.input')
    def test_get_doc_shelf(self, mocked_input):
        mocked_input.return_value = '10006'
        self.assertEqual(Secretary.get_doc_shelf(), '2')

    

if __name__ == '__main__':
    unittest.main()