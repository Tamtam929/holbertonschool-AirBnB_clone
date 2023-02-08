#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''testing file storage'''

    def test_all(self):
        """check if returns dic<class>.<id> : {obj instance}"""
        storage = FileStorage()
        all_objs = storage.all()
        self.assertIsNotNone(all_objs)
        self.assertEqual(dict, type(all_objs))
        self.assertIs(all_objs, storage._FileStorage__objects)

    def test_new(self):
        """check if it has created new object"""
        storage = FileStorage()
        all_objs = storage.all()
        jacqueline = User()
        jacqueline.id = 00000
        jacqueline.first_name = "Jacqueline"
        jacqueline.last_name = "lu"
        storage.new(jacqueline)
        key = jacqueline.__class__.__name__ + "." + str(jacqueline.id)
        self.assertIsNotNone(all_objs[key])

    def test_save(self):
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """
        Testing reload.
        """
        FileStorage.clear()
        storage.reload()
        self.assertTrue(len(storage.all()) > 0)

    def test_create(self):
        """ happy pass instance creation """
        all_objs = FileStorage()
        self.assertTrue(type(all_objs) == FileStorage)
        self.assertTrue(isinstance(all_objs, FileStorage))

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)


if __name__ == "__main__":
    unittest.main()
