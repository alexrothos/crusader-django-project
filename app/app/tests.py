"""
Sample test file
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """"Test the calc module"""

    def test_add_numbers(self):
        res = calc.add(3, 2)

        self.assertEqual(res, 5)

    def test_subtract_numbers(self):
        """Test subtracting two numbers"""
        res = calc.subtract(10, 2)

        self.assertEqual(res, 8)