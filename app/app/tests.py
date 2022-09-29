from django.test import SimpleTestCase
from app import calc


class Calctest(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.sub(10, 5)

        self.assertEqual(res,  5)
