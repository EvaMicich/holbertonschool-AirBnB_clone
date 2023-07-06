#!/usr/bin/python3
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.obj1 = BaseModel(
            id='123',
            name='test1',
            my_number=42,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        self.obj2 = BaseModel(
            id='456',
            name='test2',
            my_number=24,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        self.storage.new(self.obj1)
        self.storage.new(self.obj2)
        self.storage.save()
        self.storage.reload()
        self.objects = self.storage.all()

    def tearDown(self):
        # Clean up the file.json after each test
        with open(self.storage._FileStorage__file_path, 'w') as file:
            file.write("")

    def test_all_objects_present_when_objects_added(self):
        # Test if all objects are present when objects are added
        objects = self.objects
        expected_keys = [f"BaseModel.{self.obj1.id}", f"BaseModel.{self.obj2.id}"]
        for key in expected_keys:
            self.assertIn(key, objects)


    def test_new_adds_objects_to_storage(self):
        # Test new() method adds objects to storage
        objects = self.objects
        self.assertIn(f"BaseModel.{self.obj1.id}", objects)
        self.assertIn(f"BaseModel.{self.obj2.id}", objects)

    def test_save_serializes_objects_to_file(self):
        # Test save() method serializes objects to the JSON file
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
        objects = self.objects
        self.assertIn(f"BaseModel.{self.obj1.id}", data)
        self.assertIn(f"BaseModel.{self.obj2.id}", data)

    def test_reload_deserializes_file_to_objects(self):
        # Test reload() method deserializes file to objects
        self.storage.reload()
        objects = self.objects
        self.assertIn(f"BaseModel.{self.obj1.id}", objects)
        self.assertIn(f"BaseModel.{self.obj2.id}", objects)

    def test_reload_obj1_dict_matches_original(self):
        # Test reload() method obj1 dictionary matches original
        obj1_dict = self.objects.get(f"BaseModel.{self.obj1.id}")
        obj1 = BaseModel(**obj1_dict)
        self.assertEqual(obj1.to_dict(), obj1_dict)

    def test_reload_obj2_dict_matches_original(self):
        # Test reload() method obj2 dictionary matches original
        obj2_dict = self.objects.get(f"BaseModel.{self.obj2.id}")
        obj2 = BaseModel(**obj2_dict)
        self.assertEqual(obj2.to_dict(), obj2_dict)

