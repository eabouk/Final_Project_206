## Your name: Emma Aboukasm
## The option you've chosen: Option 1

from bs4 import BeautifulSoup
import unittest
import requests 
import sqlite3 
import re
import json
import itertools








class pre_tests(unittest.TestCase):
	def test_constructor_1(self):
		#create class instance here
		#class_instance = NationalPark(park_name, park_state)
		self.assertEqual(type(class_instance.park_state), type("this is a string"))
		#testing that the state for each park is a string
	def test_visitor_score(self):
		#create class instance here
		#class_instance = NationalPark(park_name, park_state)
		self.assertEqual(type(class_instance.visitor_score), type(0))
		#testing that the visitor score for a given state
	def test_attendence_type(self):
		#create class instance here
		#class_instance = NationalPark(park_name, park_state)
		self.assertEqual(type(class_instance.highest_attendence), type([]))
		#testing that the method highest_attendence returns a list
	def test_attendence_len(self):
		self.assertEqual(len(class_instance.highest_attendence), 5)
		#testing that this method returns 5 items
	def test_highest_revenue(self):
		#create class instance here
		#class_instance = NationalPark(park_name, park_state)
		self.assertEqual(type(class_instance.highest_revenue), type([]))
	def test_highest_rev_len(self):
		self.assertEqual(len(class_instance.highest_revenue), 5)
		#testing that this method returns 5 things
	def test_most_parks(self):
		self.assertEqual(type(most_parks), type(tuple))
		#testing that this zip computation thing returns a tuple
	def test_most_parks_len(self):
		self.assertEqual(len(most_parks), 5)

## Remember to invoke all your tests...
if __name__ == "__main__":
	unittest.main(verbosity=2)