import unittest
from classtest.pessoa_juridica import PessoaJuridica


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.func = PessoaJuridica('11.222.333/0001-99', 'name', 1)

    def test_attributes(self):
        self.assertTrue(('cnpj' in self.func.__dict__) &
                        ('nome' in self.func.__dict__) &
                        ('idade' in self.func.__dict__))

    def test_get_cnpj(self):
        self.assertEqual(self.func.get_cnpj(), '11.222.333/0001-99')

    def test_set_cnpj(self):
        new_cnpj = '44.555.666/0002-88'
        old_cnpj = self.func.get_cnpj()
        self.func.set_cnpj(new_cnpj)

        if self.func.get_cnpj() == new_cnpj:
            self.func.set_cnpj(old_cnpj)
            self.assertTrue(True)

        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
