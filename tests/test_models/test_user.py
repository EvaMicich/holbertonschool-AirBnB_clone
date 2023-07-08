#!/usr/bin/python3
"""
Unittest for User
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.u = User()

    def test_email(self):
        self.assertEqual(self.u.email, "")

    def test_password(self):
        self.assertEqual(self.u.password, "")

    def test_first_name(self):
        self.assertEqual(self.u.first_name, "")

    def test_last_name(self):
        self.assertEqual(self.u.last_name, "")
