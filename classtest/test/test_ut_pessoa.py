import unittest
from classtest.pessoa import Pessoa


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.func = Pessoa('name', 1)

    def test_attributes(self):
        self.assertTrue(('nome' in self.func.__dict__) &
                         ('idade' in self.func.__dict__))

    def test_get_nome(self):
        self.assertEqual(self.func.get_nome(), 'name')

    def test_get_idade(self):
        self.assertEqual(self.func.get_idade(), 1)

    def test_set_nome(self):
        new_name = 'another'
        old_name = self.func.get_nome()
        self.func.set_nome(new_name)

        if self.func.get_nome() == new_name:
            self.func.set_nome(old_name)
            self.assertTrue(True)

        self.assertFalse(False)

    def test_set_idade(self):
        new_age = 10
        old_age = self.func.get_idade()
        self.func.set_idade(new_age)

        if self.func.get_idade() == new_age:
            self.func.set_idade(old_age)
            self.assertTrue(True)

        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
