#!/usr/bin/python3
"""
Unittest for Review([...])
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_text(self):
        self.assertEqual(self.review.text, "")

    def test_user_id(self):
        self.assertEqual(self.review.user_id, "")

    def test_place_id(self):
        self.assertEqual(self.review.place_id, "")
