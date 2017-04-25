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
 
state_abrv = {}
state_abrv = {"Alabama": "al", "Alaska": "ak", "Arizona": "az", "Arkansas": "ar","California": "ca", "Colorado": "co", "Connecticut": "ct",
"Delaware": "de", "Florida": "fl", "Georgia": "ga", "Hawaii": "hi", "Idaho": "id", "Illinois": "il", "Indiana": "in", "Iowa": "ia", 
"Kansas": "ks", "Kentucky": "ky", "Louisiana": "la", "Maine": "me", "Maryland": "md", "Massachusetts": "ma", "Michigan": "mi",
"Minnesota": "mn", "Mississippi": "ms", "Missouri": "mo", "Montana": "mt", "Nebraska": "ne", "Nevada": "nv", "New Hampshire": "nh", 
"New Jersey": "nj", "New Mexico": "nm", "New York": "ny", "North Carolina": "nc", "North Dakota": "nd", "Ohio": "oh", "Oklahoma": "ok", 
"Oregon": "or", "Pennsylvania": "pa", "Rhode Island": "ri", "South Carolina": "sc", "South Dakota": "sd", "Tennessee": "tn", "Texas": "tx",
"Utah": "ut", "Vermont": "vt", "Virginia": "va", "Washington": "wa", "West Virginia": "wv", "Wisconsin": "wi", "Wyoming": "wy"}

#state_abrv holds all the states and their respective abbreviation so that it can loop through HTML pages in the function below
final_html = []
def get_national_park_data():
	
	for state in state_abrv.keys():
	
		if state not in CACHE_DICTION:
	
			base_url = "https://www.nps.gov/state/" + state_abrv.get(state) + "/index.htm"
			response = requests.get(base_url)
			html_doc = response.text

			soup = BeautifulSoup(html_doc, "html.parser")
			page_info = soup.find_all("div",{"class":"ContentHeader"})
			
			
			for p in page_info:
				state_title = p.find("h1",{"class": "page-title"})

			CACHE_DICTION[state_title.text] = html_doc
			f = open(CACHE_FILE, 'w')
			f.write(json.dumps(CACHE_DICTION))
			f.close()

			final_html.append(html_doc)
			

		else: 
			final_html.append(CACHE_DICTION[state])


	return final_html
	

all_html_pages = get_national_park_data()
print('printing number of pages', len(all_html_pages))


## STEP 3: Define a function that gathers HTML data representing all the front page articles on the NPS website. Do some searching
## on the page to figure out how to get all the headlines, store them in a list, and cache it using the key "NPS_front_articles"
# The link for this is: https://www.nps.gov/index.htm
def get_frontpage_articles():
	nps_front_page = []

	if "NPS_front_articles" not in CACHE_DICTION:
		base_url = "https://www.nps.gov/index.htm"
		response = requests.get(base_url)
		html_doc = response.text

		CACHE_DICTION["NPS_front_articles"] = html_doc
		f = open(CACHE_FILE, 'w')
		f.write(json.dumps(CACHE_DICTION))
		f.close()

		return CACHE_DICTION["NPS_front_articles"]

	else:
		nps_front_page = CACHE_DICTION["NPS_front_articles"]

	return nps_front_page

all_front_articles = get_frontpage_articles()


############### PART TWO ############### 
## Class 1 ##

## STEP 1: Define a class NationalPark that accepts HTML formatted string as input and uses BeautifulSoup data parsing to create
## instance variables for every instance of the National Park within the constructor. 


class NationalPark(object):

## STEP 2: Define class instance variables within the constructor. 
## Your class will have 8 instance variables:
## 		-park_name: the name of a single park
## 		-park_location: a string containing the state(s)/city of the park
## 		-park_description:  a string containing a description about the park
##		-park_type: the type of the park (battle ground, national park, historical landmark etc.)
##		NOTE: park_names, park_locations, park_descriptions and park_types are all lists of all the instance variables for each 
##			HTML page
	def __init__(self, html_doc):
		self.soup = BeautifulSoup(html_doc, "html.parser")
		self.page_info = self.soup.find_all("div",{"class": "col-md-9 col-sm-9 col-xs-12 table-cell list_left"})
		#park names
		self.park_names = []
		for p in self.page_info:
			park_n = p.find_all("h3")
			#print(park_n)
			for q in park_n:
				self.park_name = q.text
				self.park_names.append(q.text)
				#print(q.text)

		#park_location
		self.park_locations  = []
		for l in self.page_info:
			park_l = l.find_all("h4")
			for m in park_l:
				self.park_location = m.text
				self.park_locations.append(m.text)
				#print(m.text)

		#park_description
		self.park_descriptions = []
		for t in self.page_info:
			park_desc = t.find_all("p")
			for w in park_desc:
				self.park_description = w.text
				self.park_descriptions.append(w.text.rstrip('\n'))
				#print(w.text)

		#park_type
		self.park_types = []
		for b in self.page_info:
			park_t = b.find_all("h2")
			for p in park_t:
				self.park_type = p.text
				self.park_types.append(p.text)

## STEP 3: Define a method of your class called num_parks that finds and returns the number of parks in each state. It will take in 
## HTML data representing each state's park page and returns the number of parks in that state.

	def num_parks(self):
		# soup = BeautifulSoup(self, "html.parser")
		# page_info = soup.find_all("div", {"id": "list_numbers"})

		for p in self.page_info:
			numbers = self.soup.find_all("ul", {"class":"state_numbers"})
			for n in numbers:
				num_parks = self.soup.find_all("li")
				for x in num_parks:
					#print(x.text)
					num_parks = self.soup.find_all("strong")
					number_parks = num_parks[0].text
		return number_parks

## STEP 4: Define a method of your class called total_revenue that takes HTML data and finds how much revenue each state will get 
## every year from their state parks.
	
	def total_revenue(self):
		for p in self.page_info:
			for p in self.page_info:
				numbers = self.soup.find_all("ul", {"class":"state_numbers"})
			for n in numbers:
				revenue = self.soup.find_all("li")
				for x in revenue:
					#print(x.text)
					revenue = self.soup.find_all("strong")
					revenue_num = revenue[2].text
		return revenue_num

## STEP 5: Define a method of your class called visitor_score that takes HTML data representing each state's park page and returns 
## the number of visitors that visit national parks annually. This will not affect any data, simply it finds the number of annual
## visitors and returns it. You will use this number later for data processing later in this file.

	def visitor_score(self):
	
		for p in self.page_info:
			numbers = self.soup.find_all("ul", {"class":"state_numbers"})
			for n in numbers:
				num_visitors = self.soup.find_all("li")
				for x in num_visitors:
			
					num_visitors = self.soup.find_all("strong")
					num_visitors = num_visitors[1].text
					
		return num_visitors


one_park = NationalPark(all_html_pages[0])


############### PART THREE ############### 
## Class 2 ##

## STEP 1: Define a class Article that accepts an HTML formatted string representing one single article page. 
class Article(object):

	def __init__(self, html_doc):

		self.soup = BeautifulSoup(html_doc, "html.parser")
		self.page_info = self.soup.find_all("div", {"class":"FeatureGrid-item col-xs-12"})

## STEP 2: Define 2 instance variables for this class:
## 		- Title: the title of the article
## 		- Text: the SUBHEADER of the article

		for p in self.page_info:
			article_title = p.find_all("h3",{"class":"Feature-title carrot-end"})
			for r in article_title:
				self.title = r.text
			
		for p in self.page_info:
			description = p.find_all("p", {"class": "Feature-description"})
			for f in description:
				self.description = f.text

## STEP 3: Define a method of this class called list_of_titles that will gather a list of titles for all the front page articles

	def list_of_titles(self):
		self.list_of_titles = []

		for p in self.page_info:
			article_title = p.find_all("h3",{"class":"Feature-title carrot-end"})
			for r in article_title:
				self.list_of_titles.append(r.text)
		
		return self.list_of_titles

## STEP 4: Define a method of this class called list_of_descriptions that will gather a list of subheaders for all the front page 
## articles

	def list_of_descriptions(self):
		self.list_of_descriptions = []

		for p in self.page_info:
			description = p.find_all("div", {"class": "Component Feature -small"})
			#print(len(description))
			for f in description:
				description = f.find_all("p")
				for q in description:
					self.list_of_descriptions.append(q.text)
				# print(f.text)
		return self.list_of_descriptions


article_thing = Article(all_front_articles)
#print(article_thing.list_of_descriptions())
#print (article_thing.list_of_titles())

############### PART FOUR ############### 
## Creating lists from Classes ## 

## STEP 1: Create a list of instances of the NationalPark class. This will require you to use both your first function and your
## NationalPark class to gather all of the class instances into one group. Use comprehension if you're feeling up to the challenege.
states_parks = {}
for x in state_abrv:
	states_parks[x] = CACHE_DICTION[x]

#states_parks is a dictionary that contains a state name and the respective html for that state. It's just easier to create a new
#dictionary out of the CACHE_DICTION so that we can easily make lists of things. 
all_nat_park_info = []
for x in states_parks:
	one_state = NationalPark(states_parks[x])
	one_tup = zip(one_state.park_names, one_state.park_locations, one_state.park_types)
	all_nat_park_info.append(one_tup)

iterated_nat_park = []
for tup in all_nat_park_info:
	for item in tup:
		iterated_nat_park.append(item)

## STEP 2: Create a list of instances of the Article class using the second function you wrote to gather all the articles listed
## on the front page. You will have to invoke each article as a class instance first and then save them all into a list. 

article_thing = Article(all_front_articles)
article_titles = article_thing.list_of_titles()
article_descriptions = article_thing.list_of_descriptions()
article_tup = zip(article_titles, article_descriptions)
iterated_articles = []
for tup in article_tup:
	iterated_articles.append(tup)

## STEP 3: Write a function that makes a new dictionary "STATE_TEMP" that saves every state as a key band its average temparature as 
##values. (for example, Michigan's would be "MICHIGAN_TEMP": 45). Feel free to use requests and cache the data, using this website:
## https://www.currentresults.com/Weather/US/average-annual-state-temperatures.php
def find_temp_data():
	STATE_TEMP = {}

	if "STATE_TEMP" not in CACHE_DICTION: 
		base_url = "https://www.currentresults.com/Weather/US/average-annual-state-temperatures.php"
		response = requests.get(base_url)
		html_doc = response.text

		list_of_temps = []
		list_state_names = []
		soup = BeautifulSoup(html_doc, 'html.parser')

		find_temps = soup.find_all("table", {"class": "articletable tablecol-1-left"})

		for f in find_temps:
			state_find = f.find_all('tbody')

			for t in state_find:
				narrow = t.find_all('tr')
		 	
				for s in narrow:
					state_info = s.find_all("td")
					state_name = state_info[0].text
					state_ave_temp = state_info[1].text
			
					STATE_TEMP[state_name] = state_ave_temp

		
		CACHE_DICTION["STATE_TEMP"] = STATE_TEMP
		f = open(CACHE_FILE, 'w')
		f.write(json.dumps(CACHE_DICTION))
		f.close()

		return CACHE_DICTION["STATE_TEMP"]

	else:
		return CACHE_DICTION["STATE_TEMP"]

#print (find_temp_data())
temp_data = find_temp_data()
# print(type(temp_data))
new_temp_data = sorted(temp_data.items(), key = lambda x: x[0])
# print(type(new_temp_data))
# #print(new_temp_data)
states, temp_values = zip(*new_temp_data)
print("printing states and temp values", states, temp_values)
#print("PRINTING NEW TEMP DATA", new_temp_data.values())
#print (len(CACHE_DICTION["STATE_TEMP"]))
#print(sorted(CACHE_DICTION["STATE_TEMP"]))
#state_temps = sorted(CACHE_DICTION['STATE_TEMP'].values())

## STEP 4: Write code to make lists of all the data that will be inputted into the state's table in your database. You will need 
## a list of state_abrv, number of parks, revenue for each state, and avg_temp for each state. 
all_state_abrv = state_abrv.values()


def get_state_table_info():
	state_table_tups = []
	iterated_list_states = []
	if "STATE_TABLE_TUPS" not in CACHE_DICTION:

		number_all_states_parks = []
		num_revenue_all_states = []
		for state in sorted(states_parks):
			#print(states_parks[state])
			one_state = NationalPark(states_parks[state])
			#before this said sorted(states_parks.keys()) and then states_parks[state] for the NationalPark(state)...
			revenue = one_state.total_revenue()
			#print("PRINTING REVENUE", revenue)
			# num_revenue_all_states.append(revenue)


			# print("caching...", state)
			number_parks = one_state.num_parks()
			# print("num parks...", number_parks)
			# print("num revenue", revenue)
			# #print("num revenue...", num_revenue_all_states)
			# number_all_states_parks.append(number_parks)
			
			# one_tup = 

			state_table_tups.append(zip(state_abrv[state], number_parks, revenue, CACHE_DICTION['STATE_TEMP'][state]))

		for tup in state_table_tups:
			iterated_list_states.append(tup)
			print(tup)
				
		# state_table_zip = itertools.zip_longest(state_abrv.values(), number_all_states_parks, num_revenue_all_states, temp_values)


		# for item in state_table_zip:
		# 	state_table_tups.append(item)
		# 	print("PRINTING STATE TUP", item)

		CACHE_DICTION["STATE_TABLE_TUPS"] = iterated_list_states

		f = open(CACHE_FILE, 'w')
		f.write(json.dumps(CACHE_DICTION))
		f.close()

		return CACHE_DICTION["STATE_TABLE_TUPS"]

	else: 
		return CACHE_DICTION["STATE_TABLE_TUPS"]

all_state_table = get_state_table_info()
print (sorted(all_state_table))
print(len(all_state_table))

new_state_list = []
for tup in all_state_table:
	new_state_list.append(tup)
print(new_state_list)

## THINGS TO FIX:
	#- data is in states table but its off... not sure how much off but its not right
	#-check the articles table... see if its accurate. 
############### PART FIVE ############### 
## Database Work ##

## Set up your database connection and cursor below...
conn = sqlite3.connect('national_park_data.db')
cur = conn.cursor()

## STEP 1: Create a table for national parks and load data from lists into tups into the tables.
statement = "DROP TABLE IF EXISTS parks"
cur.execute(statement)
## For the parks table:
	# -park_name: text primary key
	# -park_location: text 
	# -park_type: (type of park) text
statement = "CREATE TABLE IF NOT EXISTS parks (park_name TEXT primary key, park_location TEXT, park_type TEXT)"
cur.execute(statement)

statement = "INSERT OR IGNORE INTO parks VALUES(?, ?, ?)"
for tup in iterated_nat_park:
 	cur.execute(statement, tup)
conn.commit()



## STEP 2: Create a table for states information. 
statement = "DROP TABLE IF EXISTS states"
cur.execute(statement)
## For the states table:
	# -state_abrv: text primary key (2 letter abbreviation)
	# -num_parks: integer 
	# -revenue: text
	# -avg_temp: Real (float)
statement = "CREATE TABLE IF NOT EXISTS states (state_abrv TEXT primary key, num_parks INTEGER, revenue TEXT, avg_temp REAL)"
cur.execute(statement)
#load data below...
statement = 'INSERT OR IGNORE INTO states VALUES(?, ?, ?, ?)'
for tup in new_state_list:
	cur.execute(statement, tup)
conn.commit()
#Will finish loading this in when I gather average temp data 



## STEP 3: Create a table for article data. 
statement = "DROP TABLE IF EXISTS articles"
cur.execute(statement)
## For the articles table: 
	# -headline: text primary key (from the "News Releases" website)
	# -date_released: date type or var char (numbers and dashes)
	# -related_park: text (park associated with article)
statement = "CREATE TABLE IF NOT EXISTS articles (headline TEXT primary key, description VARCHAR)"
cur.execute(statement)

#load data below...
statement = 'INSERT OR IGNORE INTO articles VALUES(?, ?)'
for tup in iterated_articles:
	cur.execute(statement, tup)
conn.commit()

conn.close()


############### PART SIX ############### 
## Queries ##

## STEP 1: Write a query to join on the states table the abrv column with the park_location on the parks table
query = "SELECT states.state_abrv, park.park_location FROM parks INNER JOIN states on state.state_abrv = park.park_location"
cur.execute(query)
joined_result = cur.fetchall()

## STEP 2: Write a query to find the states with num_parks greater than 10. Save that into a variable titled most_parks. 
query = "SELECT num_parks FROM states WHERE states.num_parks > 10"
cur.execute(query)
most_parks = cur.fetchall()

## STEP 3: Write a query to find the states with the hottest temperature. Save that into a variable titled hottest_temp.
query = "SELECT avg_temp FROM states WHERE states.avg_temp > 60"


############### PART SEVEN ############### 
## Data manipulation ## 

## STEP 1: Use a zip function to create a list of tuples of the top 5 states with the highest revenue AND their respective revenue.

## More data manipulation to come? 
## Wondering how to create the database files before writing the classes... will finish this later? 



############### TEST CASES ############### 
class TEST_PART_ONE(unittest.TestCase):
	def test_caching(self):
		self.assertEqual(type(CACHE_DICTION), type({}))
	def test_get_national_park_func(self):
		self.assertEqual(type(get_national_park_data()), type([]))
	def test_get_frontpage_aritcles_func(self):
		self.assertEqual(type(get_frontpage_articles()), type('s'))

class TEST_PART_TWO(unittest.TestCase):	
	def test_constructor_1(self):
		one_park = NationalPark(all_html_pages[0])
		self.assertEqual(type(one_park.park_names), type([]))
	def test_constructor_2(self):
		one_park = NationalPark(all_html_pages[1])
		self.assertEqual(type(one_park.park_locations), type([]))
	def test_constructor_3(self):
		one_park = NationalPark(all_html_pages[2])
		self.assertEqual(type(one_park.park_locations[0]), type('hello'))
		#testing that the first item in the lsit of parks is a string
	def test_constructor_4(self):
		one_park = NationalPark(all_html_pages[3])
		self.assertEqual(type(one_park.park_descriptions), type([]))

	def test_constructor_5(self):
		one_park = NationalPark(all_html_pages[4])
		self.assertEqual(type(one_park.park_types), type([]))	
	def test_method_1(self):
		one_park = NationalPark(all_html_pages[5])
		self.assertEqual(type(one_park.num_parks()), type('s'))
	def test_method_2(self):
		one_park = NationalPark(all_html_pages[6])
		self.assertEqual(type(one_park.visitor_score()), type('s'))
	def test_method_3(self):
		one_park = NationalPark(all_html_pages[0])
		self.assertEqual(type(one_park.total_revenue()), type('s'))

class TEST_PART_3(unittest.TestCase):
	def test_constructor_1(self):
		article = Article(all_front_articles)
		self.assertEqual(type(article.title), type('s'))
	def test_constructor_2(self):
		article = Article(all_front_articles)
		self.assertEqual(type(article.description), type('s'))
	def test_lists(self):
		article = Article(all_front_articles)
		self.assertEqual(type(article.list_of_titles()), type([]))
		self.assertEqual(type(article.list_of_descriptions()), type([]))

class TEST_PART_4(unittest.TestCase): 
	def test_new_dict(self):
		self.assertEqual(len(states_parks), 50)
	def test_temp_dict(self):
	 	self.assertEqual(len(CACHE_DICTION["STATE_TEMP"]), 50)
	def test_get_state_info(self):
		self.assertEqual(type(get_state_table_info()), type([]))
	def test_get_state_info_2(self):
		self.assertEqual(len(get_state_table_info()), 50)
	def test_get_state_info_3(self):
		self.assertEqual(type(all_state_table[0]), type((3, 4)))
# #will write more test cases when more code is written....
# #will solidify the test case ideas when more code is written...
# ## Remember to invoke all your tests...
if __name__ == "__main__":
	unittest.main(verbosity=2)