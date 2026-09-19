# Michael Benko
# 2026-09-19
# CSD325-302E Advanced Python (2267-DD)
# Module 7.2 Assignment

import unittest
from city_functions import get_city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        result = get_city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")

if __name__ == '__main__':
    unittest.main()