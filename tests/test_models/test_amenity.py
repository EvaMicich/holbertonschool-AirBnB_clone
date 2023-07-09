#!/usr/bin/python3
"""
Unittest for Amenity

"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.a = Amenity()

    def test_name_is_a_empty_string(self):
        self.assertEqual(self.a.name, "")
