import unittest

from src import doomsday


class TestDoomsday(unittest.TestCase):
    
    def test_valid_input(self):
        year = 2024
        month = 11
        day = 29
        weekday = doomsday.get_week_day(year, month, day)
        self.assertEqual('Friday', weekday)

    def test_literal_year(self):
        weekday = doomsday.get_week_day('a', 10, 24)
        self.assertEqual(None, weekday)
    
    def test_literal_month(self):
        weekday = doomsday.get_week_day(2023, 'a', 24)
        self.assertEqual(None, weekday)
    
    def test_literal_day(self):
        weekday = doomsday.get_week_day(2023, 10, 'a')
        self.assertEqual(None, weekday)

    def test_invalid_year(self):
        with self.assertRaises(AssertionError) as context:
            doomsday(-2023, 10, 24)
        self.assertEqual(str(context.exception), "year should be POSITIVE")

    #def test_invalid_month(self)
    #def test_invalid_day(self)

if __name__ == "__main__":
    unittest.main()