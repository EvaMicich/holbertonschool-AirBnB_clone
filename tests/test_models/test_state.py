#!/usr/bin/python3
"""
Unittest for State
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.s = State()

    def test_if_name_is_empty_string(self):
        self.assertEqual(self.s.name, "")
