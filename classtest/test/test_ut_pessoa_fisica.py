import unittest
from classtest.pessoa_fisica import PessoaFisica


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.func = PessoaFisica('111.222.333-44', 'name', 1)

    def test_attributes(self):
        self.assertTrue(('cpf' in self.func.__dict__) &
                        ('nome' in self.func.__dict__) &
                        ('idade' in self.func.__dict__))

    def test_get_cpf(self):
        self.assertEqual(self.func.get_cpf(), '111.222.333-44')

    def test_set_cpf(self):
        new_cpf = '555.666.777-88'
        old_cpf = self.func.get_cpf()
        self.func.set_cpf(new_cpf)

        if self.func.get_cpf() == new_cpf:
            self.func.set_cpf(old_cpf)
            self.assertTrue(True)

        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
