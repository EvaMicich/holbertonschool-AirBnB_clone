import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.obj1_id = '123'
        self.obj2_id = '456'
        self.obj1 = BaseModel(
            id=self.obj1_id,
            name='test1',
            my_number=42,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        self.obj2 = BaseModel(
            id=self.obj2_id,
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
        with open(self.storage._FileStorage__file_path, 'w') as file:
            file.write("")

    def test_all_objects_present_when_objects_added(self):
        expected_keys = [f"BaseModel.{self.obj1_id}", f"BaseModel.{self.obj2_id}"]
        for key in expected_keys:
            self.assertIn(key, self.objects)

    def test_new_adds_objects_to_storage(self):
        self.assertIn(f"BaseModel.{self.obj1_id}", self.objects)
        self.assertIn(f"BaseModel.{self.obj2_id}", self.objects)

    def test_save_serializes_objects_to_file(self):
        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
        self.assertIn(f"BaseModel.{self.obj1_id}", data)
        self.assertIn(f"BaseModel.{self.obj2_id}", data)

    def test_reload_deserializes_file_to_objects(self):
        reloaded_storage = FileStorage()
        reloaded_storage.reload()
        reloaded_objects = reloaded_storage.all()
        self.assertEqual(reloaded_objects, self.objects)

    def test_reload_obj1_dict_matches_original(self):
        obj1_dict = self.objects[f"BaseModel.{self.obj1_id}"]
        obj1 = BaseModel(**obj1_dict.to_dict())
        self.assertEqual(obj1.to_dict(), obj1_dict.to_dict())

    def test_reload_obj2_dict_matches_original(self):
        obj2_dict = self.objects[f"BaseModel.{self.obj2_id}"]
        obj2 = BaseModel(**obj2_dict.to_dict())
        self.assertEqual(obj2.to_dict(), obj2_dict.to_dict())

    def test_save_updates_updated_at(self):
        old_updated_at = self.obj1.updated_at
        self.obj1.save()
        new_updated_at = self.obj1.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == '__main__':
    unittest.main()
