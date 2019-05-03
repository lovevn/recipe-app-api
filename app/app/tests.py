from django.test import TestCase

from .calc import add


class CaclTest(TestCase):
    def test_add_numbers(self):
        """
        Test two number are added together
        :return:
        """
        self.assertEqual(add(3, 4), 7)
