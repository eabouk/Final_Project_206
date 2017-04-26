FINAL PROJECT SI 206 
Emma Aboukasm 

PROJECT 1: NATIONAL PARK SERVICE WEBSITE SCRAPER 

DESCRIPTION: 
	This project takes data from the National Parks Service website, saves information into a database and computes states that gain
	the highest revenue from their national parks. It runs off of python and creates a json cached data file, and a database file in
	the process of being run. It requires no user input and is completely self contained. 


HOW TO RUN THIS FILE/DEPENDENCIES: 
	You will need to have Python 3 installed on your computer in order to run this file. Open your terminal window and go to the directory in which you have saved the file. Type in "sh run206Project.sh" in order to run the file. 

	This file runs using the default parser with Python 3, so no additional moduals need to be installed. 


FILES INCLUDED:

	- 206_final_project.py
	- national_park_cache.json
	- national_park_data.db
	- 206_final_project.txt
	- run206Project.sh
	- README_final_project_206.txt (this file)


FUNCTIONS:
	- get_national_park_data():
		This function will scrape the NPS website for all the HTML pages associated with each state and then cache each page into the CACHE_DICTION, which contains a lot of the html data for this project. 

	- get_frontpage_articles():
		This function simply takes the front page of the National Parks Service website and puts it in the CACHE_DICTION so it can be accessed later for parsing.

	- find_temp_data():
		This function uses the requests.get() module (like the other 2 functions above) and finds the average temperature for every state. It takes no inputs and returns a dictionary with each state and its respective average temeperature. 

	-get_state_table_info(): 
		This function checks first to see if the string "STATE_TABLE_TUPS" is in the CACHE_DICTION and if it's not, it will go through every single state's HTML page and make an instance of NationalPark in order to accumulate lists of parks and revenue for each state. It also zips other lists of information such as the state abbreviation for each state and the temperature value for each state found by the find_temp_data() function. It then compiles the list of tuples into a list and adds it to the CACHE_DICTION. If the list of state tups is already in the CACHE, it will simply return that list of state information. 



CLASSES:
	- NationalPark:
		The constructor for this class takes in an HTML page that represents one state's national parks. The constructor will make a list of a state's parks, locations of parks, park types, and park descriptions. 

		Each instance of the NationalPark class can represent either a very specific park based on a given state, or an entire state's parks, locations, and types, etc. That is why there are 8 instance variables for the constructor of the class.

		NationalPark Methods:
			num_parks():
				This class method within the NationalPark class will return the number of parks in each state. It uses HTML parsing that was set in the class constructor. It changes no data and uses only the information in the constructor, no additional inputs needed. 

			total_revenue():
				This method will return the amount of revenue that each state recieves from their national parks. It uses HTML parsing that was set in the class constructor. It changes no data and uses only the information in the constructor, no additional inputs needed. 

			visitor score():
				This method will return the total number of vistiors to national parks for a given state. It uses HTML parsing that was set in the class constructor. It changes no data and uses only the information in the constructor, no additional inputs needed. 


	- Article:
		The constructor for this class will take in the front page of the NPS website that was found using the get_frontpage_articles() function and will make a Beautiful Soup object to gather the titles and short descriptions of each article on the front page of the NPS website. 

		One instance of this class represents an article on the front page of the NPS website. 

		Article Methods:
			list_of_titles():
				This will use the constructor's beautiful soup object to find all the titles of articles on the front page of the NPS website and append them to a list, returning a list of titles. It changes no data and uses only the information in the constructor, no additional inputs needed. 

			list_of_descriptions():
				This method will use the constructor's beautiful soup object to find and append to a list, all the short descriptions of every article on the NPS front page. It changes no data and uses only the information in the constructor, no additional inputs needed. 


DATABASE TABLES:
	-parks:
		The parks table has 3 values:
			-park_name
			-park_location
			-park_type 

		The values for this table have been accumulated by the NationalPark class. 

		Each row in the table represents a National Park, and it's attributes are the name of the par, the location of the park and the type of park (national monument, national park, historic trail, etc.). 

	-states: 
		The states table has 4 values:
			-state_abrv: Abbreviation for the state
			-num_parks: Number of parks in each state
			-revenue: Amount of money brought in yearly due to national park attendence
			-avg_temp: Average yearly temperature for the state

		The values for this table have been accumulated through the function get_state_table_info(), which uses the NationalPark class and the function find_temp_data(). 

		Each row in the table represents a state and its attritubes are the 4 values, state_abrv, num_parks, revenue, and avg_temp.

		
	-articles:
		The articles table has 2 values:
			-headline: The headline of the article
			-description: The subheader of the article 

		The values for this table were accumulated by the Articles class. 

		Each row of the articles table represents an article on the front page of the NPS front page. 

WHY THIS PROJECT MATTERS TO ME:

	I chose this project because I like the idea of scraping websites for data to make inferences and calculations that will further help people understand things. The world is full of information and it can be overwhelming. But it is important to be able to gather very specific data in order to come up with a better understanding of what may be a complicated issue. This project may be a stepping stone for further data scraping projects in the future. 


FOR SI 206

	Line(s) on which each of your data gathering functions begin(s):
		-get_national_park_data():line 43
		-get_frontpage_articles(): line 81

	Line(s) on which your class definition(s) begin(s):
		-class NationalPark: line 111
		-class Article: line 214

	Line(s) where your database is created in the program:
		-line 394

	Line(s) of code that load data into your database:
		-lines 404 - 410
		-lines 422 - 428
		-lines 439 - 446

	Line(s) of code (approx) where your data processing code occurs — where in the file can we see all the processing techniques you used?
		-starts on line 456 downward... all my queries 
		-The file where the query results are contained is called 206_final_project.txt

	Line(s) of code that generate the output.
		-test cases at the bottom of the file: line 487 and downward 











