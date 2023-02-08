#!/usr/bin/python3
""" Unit tests for class Place """
import unittest
import models
from models.place import Place
from datetime import datetime
from time import sleep


class TestUser(unittest.TestCase):
    """ Unit tests for class Place """

    def test_instantiate(self):
        """ Happy pass instantiation """
        self.assertEqual(Place, type(Place()))

    def test_id(self):
        """ Happy pass public id string format """
        self.assertEqual(str, type(Place().id))

    def test_created_at(self):
        """ Happy pass created at datetime """
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at(self):
        """ Happy pass updated at datetime """
        self.assertEqual(datetime, type(Place().updated_at))

    def test_uid(self):
        """ UID created at each instantiation """
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_city_id(self):
        """ Happy pass city_id """
        place1 = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertTrue(hasattr(place1, "city_id"))

    def test_user_id(self):
        """ Happy pass user_id """
        place1 = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertTrue(hasattr(place1, "user_id"))

    def test_name(self):
        """ Happy pass name """
        place1 = Place()
        self.assertEqual(str, type(Place.name))
        self.assertTrue(hasattr(place1, "name"))

    def test_description(self):
        """ Happy pass description """
        place1 = Place()
        self.assertEqual(str, type(Place.description))
        self.assertTrue(hasattr(place1, "description"))

    def test_number_rooms(self):
        """ Happy pass rooms """
        place1 = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertTrue(hasattr(place1, "number_rooms"))

    def test_number_bathrooms(self):
        """ Happy pass bathrooms """
        place1 = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertTrue(hasattr(place1, "number_bathrooms"))

    def test_max_guest(self):
        """ Happy pass max guest """
        place1 = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertTrue(hasattr(place1, "max_guest"))

    def test_price_by_night(self):
        """ Happy pass price by night """
        place1 = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertTrue(hasattr(place1, "price_by_night"))
