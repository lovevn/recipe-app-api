from django.test import TestCase

from .calc import add, subtract


class CaclTest(TestCase):
    def test_add_numbers(self):
        """
        Test two number are added together
        :return:
        """
        self.assertEqual(add(3, 4), 7)

    def test_subtract_numbers(self):
        """
        Test subtract two numbers
        :return:
        """
        self.assertEqual(subtract(3, 10), 7)
