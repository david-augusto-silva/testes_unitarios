import unittest

from src import doomsday


class TestDoomsday(unittest.TestCase):
    
    def test_valid_data(self):
        entrada = [2024, 11, 29]
        saida_esperada = "Friday"
        saida_obtida = doomsday.get_week_day(entrada[0], entrada[1], entrada[2])
        self.assertEqual(saida_esperada, saida_obtida)

    #teste dia
    def test_day_1(self):
        obtido = doomsday.get_week_day(2024, 11, 1)
        esperado = "Friday"
        self.assertEqual(esperado, obtido)

    def test_day_2(self):
        obtido = doomsday.get_week_day(2024, 11, 2)
        esperado = "Saturday"
        self.assertEqual(esperado, obtido)
    
    def test_day_0(self):
        with self.assertRaises(AssertionError) as ctx:
            doomsday.get_week_day(2024, 11, 0)
        assert_error = ctx.exception
        self.assertEqual(assert_error.__str__(), 'day should be between 1 to 31')

    def test_day_30(self):
        obtido = doomsday.get_week_day(2024, 11, 2)
        esperado = ("Saturday")
        self.assertEqual(esperado, obtido)

    def test_day_32(self):
        with self.assertRaises(AssertionError) as ctx:
            doomsday.get_week_day(2024, 11, 32)
        assert_error = ctx.exception
        self.assertEqual(assert_error.__str__(), "day should be between 1 to 31")
    
    
    #def test_invalid_month(self)
    #def test_invalid_day(self)

if __name__ == "__main__":
    unittest.main()