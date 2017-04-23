FINAL PROJECT SI 206 
Emma Aboukasm 

PROJECT 1: NATIONAL PARK SERVICE WEBSITE SCRAPER 

DESCRIPTION: 
	This project takes data from the National Parks Service website, saves information into a database and computes states that gain
	the highest revenue from their national parks. It runs off of python and creates a json cached data file, and a database file in
	the process of being run. It requires no user input and is completely self contained. 


HOW TO RUN THIS FILE/DEPENDENCIES: 
	You will need to have Python 3 installed on your computer in order to run this file. Open your terminal window and go to the directory in which you have saved the file. Type in "python 206_final_project" in order to run the file. 

	This file runs using the default parser with Python 3, so no additional moduals need to be installed. 


FILES INCLUDED:

	- 206_final_project.py
	- national_park_cache.json
	- national_park_data.db
	- README_final_project_206.txt (this file)


FUNCTIONS:
	- get_national_park_data():
		This function will scrape the NPS website for all the HTML pages associated with each state and then cache each page into the CACHE_DICTION, which contains a lot of the html data for this project. 

	- get_frontpage_articles():
		This function simply takes the front page of the National Parks Service website and puts it in the CACHE_DICTION so it can be accessed later for parsing.

	- find_temp_data():
		This function uses the requests.get() module (like the other 2 functions above) and finds the average temperature for every state. It takes no inputs and returns a dictionary with each state and its respective average temeperature. 


CLASSES:
	- NationalPark:
		The constructor for this class takes in an HTML page that represents one state's national parks. The constructor will make a list of a state's parks, locations of parks, park types, and park descriptions. 

		NationalPark Methods:
			num_parks():
				This class method within the NationalPark class will return the number of parks in each state. It uses HTML parsing that was set in the class constructor. 

			total_revenue():
				This method will return the amount of revenue that each state recieves from their national parks. It uses HTML parsing that was set in the class constructor. 

			visitor score():
				This method will return the total number of vistiors to national parks for a given state. It uses HTML parsing that was set in the class constructor. 


	- Article:
		The constructor for this class will take in the front page of the NPS website that was found using the get_frontpage_articles() function and will make a Beautiful Soup object to gather the titles and short descriptions of each article on the front page of the NPS website. 

		Article Methods:
			list_of_titles():
				This will use the constructor's beautiful soup object to find all the titles of articles on the front page of the NPS website and append them to a list, returning a list of titles. 

			list_of_descriptions():
				This method will use the constructor's beautiful soup object to find and append to a list, all the short descriptions of every article on the NPS front page. 


DATABASE TABLES:
	-parks:
		


DATA MANIPULATION:


WHY THIS PROJECT MATTERS TO ME:

	I chose this project because I like the idea of scraping websites for data to make inferences and calculations that will further help people understand things. The world is full of information and it can be overwhelming. But it is important to be able to gather very specific data in order to come up with a better understanding of what may be a complicated issue. This project may be a stepping stone for further data scraping projects in the future. 








