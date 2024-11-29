import unittest

from src import reverse

class TestReverseMethod(unittest.TestCase):
    """"""
    #ct01(733, 337)
    def test_numero_valido(self):
        entrada = 733
        saida = 337
        saida_obtida = reverse.reverse2(entrada)
        self.assertEqual(saida, saida_obtida)

    #ct02(-374, None)
    def test_numero_negativo(self):
        self.assertEqual(None, reverse.reverse2(-374))
    #ct03(abc, None)
    def test_string(self):
        self.assertEqual(None, reverse.reverse2('abc'))
    #ct04("", None)
    def test_vazio(self):
        self.assertEqual(None, reverse.reverse2(''))
if __name__ == '__main__':
    unittest.main()

