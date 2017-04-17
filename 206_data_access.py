## Your name: Emma Aboukasm
## The option you've chosen: Option 1

from bs4 import BeautifulSoup
import unittest
import requests 
import sqlite3 
import re
import json
import itertools

############### PART ONE ############### 
## Gathering Data/Caching ##

## STEP 1: Start by creating a caching pattern and json file to cache HTML data. 
CACHE_FILE = "national_park_cache.json"

try: 
	f = open(CACHE_FILE, 'r')
	contents_of_CF = f.read()
	f.close()
	CACHE_DICTION = json.loads(contents_of_CF)
except: 
	CACHE_DICTION = {}

## STEP 2: Define a function to gather HTML data from each state's national park using this link https://www.nps.gov/index.html 
## Go through each state, find the park data data and cache it. 
## You should start by finding out the link to one state's listed parks and format a for loop to gather the data from each state, 
## and cache it into a cache file. Each state should have a simple HTML string that lists all the parks and data about each state. 

#First I need a dict of states and other zones that parks reside so that I can loop through in order to put the data in the cache 
# dictionary. 
state_abrv = {}
state_abrv = {"Alabama": "al", "Alaska": "ak", "Arizona": "az", "Arkansas": "ar","California": "ca", "Colorado": "co", "Connecticut": "ct",
"Delaware": "de", "Florida": "fl", "Georgia": "ga", "Hawaii": "hi", "Idaho": "id", "Illinois": "il", "Indiana": "in", "Iowa": "ia", 
"Kansas": "ks", "Kentucky": "ky", "Louisiana": "la", "Maine": "me", "Maryland": "md", "Massachusetts": "ma", "Michigan": "mi",
"Minnesota": "mn", "Mississippi": "ms", "Missouri": "mo", "Montana": "mt", "Nebraska": "ne", "Nevada": "nv", "New Hampshire": "nh", 
"New Jersey": "nj", "New Mexico": "nm", "New York": "ny", "North Carolina": "nc", "North Dakota": "nd", "Ohio": "oh", "Oklahoma": "ok", 
"Oregon": "or", "Pennsylvania": "pa", "Rhode Island": "ri", "South Carolina": "sc", "South Dakota": "sd", "Tennessee": "tn", "Texas": "tx",
"Utah": "ut", "Vermont": "vt", "Virginia": "va", "Washington": "wa", "West Virginia": "wv", "Wisconsin": "wi", "Wyoming": "wy", 
"Northern Mariana Islands": "mp", "Guam": "gu", "Puerto Rico": "pr", "Virgin Islands": "vi"}
#after writing the data_cache function, I will loop through the values of the dictionary above in order to put stuff in a cache file. 
final_list = []

def get_national_park_data():
	
	for state in state_abrv.keys():
		if state not in CACHE_DICTION:

	#lets put all keys and values in the dict
			#print("hello")
			# for abrv in state_abrv.values():
			base_url = "https://www.nps.gov/state/" + state_abrv.get(state) + "/index.htm"
			response = requests.get(base_url)
			html_doc = response.text

			soup = BeautifulSoup(html_doc, "html.parser")
			page_info = soup.find_all("div",{"class":"ContentHeader"})
			
			
			for p in page_info:
				state_title = p.find("h1",{"class": "page-title"})
				#print(state_title.text)

			json_html = json.dumps(html_doc)
			CACHE_DICTION[state_title.text] = json_html
			f = open(CACHE_FILE, 'w')
			f.write(json.dumps(CACHE_DICTION))
			f.close()

			state_tup = (state_title.text, html_doc)
			final_list.append(state_tup)
			#this portion will run if cache is empty

		else: 
			#this portion will run if cache diction has stuff in it already
			state_tup = (state, CACHE_DICTION[state])
			#if the state is already in the dictionary, make a tup and append to final list
			final_list.append(state_tup)

	return final_list

# print(get_national_park_data())

tups_of_all_pages = get_national_park_data()
print(len(tups_of_all_pages))

	


## STEP 3: Define a function that gathers HTML data representing all the front page articles on the NPS website. Do some searching
## on the page to figure out how to get all the headlines, store them in a list, and cache it using the key "NPS_front_articles"
# The link for this is: https://www.nps.gov/index.htm
def get_frontpage_articles():
	nps_front_page = []

	if "NPS_front_articles" not in CACHE_DICTION:
		base_url = "https://www.nps.gov/index.htm"
		response = requests.get(base_url)
		html_doc = response.text

		soup = BeautifulSoup(html_doc, "html.parser")
		page_info = soup.find_all("div", {"class":"Feature-imageContainer"})

		for p in page_info:
			article_title = p.find("h3",{"class":"Feature-title carrot-end"})
			nps_front_page.append(article_title.text)
			# print(article_title.text)

		CACHE_DICTION["NPS_front_articles"] = nps_front_page
		f = open(CACHE_FILE, 'w')
		f.write(json.dumps(CACHE_DICTION))
		f.close()

	else:
		nps_front_page = CACHE_DICTION["NPS_front_articles"]

	return nps_front_page

all_front_articles = get_frontpage_articles()
print(all_front_articles)

############### PART TWO ############### 
## Class 1 ##

## STEP 1: Define a class NationalPark that accepts HTML formatted string as input and uses BeautifulSoup data parsing to create
## instance variables for every instance of the National Park within the constructor. 

## STEP 2: Define class instance variables within the constructor. 
## Your class will have 3 instance variables:
## 		-park_state: the location/state of each park (a string containing the location)
## 		-park_info: a string containing a description about the park
##		-map_link: a link to the map for the park 

## STEP 3: Define a method of your class called visitor_score that takes HTML data representing each state's park page and returns 
## the number of visitors that visit national parks annually. This will not affect any data, simply it finds the number of annual
## visitors and returns it. You will use this number later for data processing later in this file.

## STEP 4: Define a method of your class called num_parks that finds and returns the number of parks in each state. It will take in 
## HTML data representing each state's park page and returns the number of parks in that state.

## STEP 5: Define a method of your class called annual_revenue that takes HTML data representing a state's park page and reuturns 
## the total annual revenue that is gained from state parks in that given state. 



############### PART THREE ############### 
## Class 2 ##

## STEP 1: Define a class Article that accepts an HTML formatted string representing one single article page. 

## STEP 2: Define 2 instance variables for this class:
## 		- Title: the title of the article
## 		- Text: the text of the article



############### PART FOUR ############### 
## Creating lists from Classes ## 

## STEP 1: Create a list of instances of the NationalPark class. This will require you to use both your first function and your
## NationalPark class to gather all of the class instances into one group. Use comprehension if you're feeling up to the challenege.

## STEP 2: Create a list of instances of the Article class using the second function you wrote to gather all the articles listed
## on the front page. You will have to invoke each article as a class instance first and then save them all into a list. 

## STEP 3: Create a new dictionary "STATE_TEMP" that saves every state as a key band its average temparature as values. 
## (for example, Michigan's would be "MICHIGAN_TEMP": 45). 


############### PART FIVE ############### 
## Database Work ##

############### PART SIX ############### 
## Data Manipulation


############### TEST CASES ############### 
# class pre_tests(unittest.TestCase):
# 	def test_constructor_1(self):
# 		#create class instance here
# 		#class_instance = NationalPark(park_name, park_state)
# 		self.assertEqual(type(class_instance.park_state), type("this is a string"))
# 		#testing that the state for each park is a string
# 	def test_visitor_score(self):
# 		#create class instance here
# 		#class_instance = NationalPark(park_name, park_state)
# 		self.assertEqual(type(class_instance.visitor_score), type(0))
# 		#testing that the visitor score for a given state
# 	def test_attendence_type(self):
# 		#create class instance here
# 		#class_instance = NationalPark(park_name, park_state)
# 		self.assertEqual(type(class_instance.highest_attendence), type([]))
# 		#testing that the method highest_attendence returns a list
# 	def test_attendence_len(self):
# 		self.assertEqual(len(class_instance.highest_attendence), 5)
# 		#testing that this method returns 5 items
# 	def test_highest_revenue(self):
# 		#create class instance here
# 		#class_instance = NationalPark(park_name, park_state)
# 		self.assertEqual(type(class_instance.highest_revenue), type([]))
# 	def test_highest_rev_len(self):
# 		self.assertEqual(len(class_instance.highest_revenue), 5)
# 		#testing that this method returns 5 things
# 	def test_most_parks(self):
# 		self.assertEqual(type(most_parks), type(tuple))
# 		#testing that this zip computation thing returns a tuple
# 	def test_most_parks_len(self):
# 		self.assertEqual(len(most_parks), 5)

## Remember to invoke all your tests...
if __name__ == "__main__":
	unittest.main(verbosity=2)