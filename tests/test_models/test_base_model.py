#!/usr/bin/python3

"""
Unittest for BaseModel()
"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel(
            id='123',
            name='test',
            my_number=42,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        self.string_representation = str(self.model)
        self.initial_updated_at = self.model.updated_at
        self.model_dict = self.model.to_dict()

    def test_init_with_args(self):
        self.assertEqual(self.model.id, '123')

    def test_init_without_args(self):
        self.assertIsInstance(self.model.id, str)

    def test_init_created_at(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_init_updated_at(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_contains_class_name(self):
        self.assertIn('[BaseModel]', self.string_representation)

    def test_str_contains_id(self):
        self.assertIn(self.model.id, self.string_representation)

    def test_save_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(self.model_dict, dict)

    def test_to_dict_contains_class_name(self):
        self.assertEqual(self.model_dict['__class__'], 'BaseModel')

    def test_to_dict_contains_id(self):
        self.assertEqual(self.model_dict['id'], self.model.id)

    def test_to_dict_contains_created_at(self):
        self.assertEqual(self.model_dict['created_at'], self.model.created_at.isoformat())

    def test_to_dict_contains_updated_at(self):
        self.assertEqual(self.model_dict['updated_at'], self.model.updated_at.isoformat())

