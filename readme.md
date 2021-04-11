# esg-web-scraper
https://esg-web-scraper.herokuapp.com/

Is there a correlation between the ESG rating and the stock price for a company?

![screengrab](https://media.giphy.com/media/yRx7YJn3sn3lSexn19/giphy.gif)

# What Does This App Do?
1. Scrapes ESG data from the [MSCI ESG Ratings Corporate Search Tool](https://www.msci.com/our-solutions/esg-investing/esg-ratings/esg-ratings-corporate-search-tool/issuer/)
- Using selenium in headless mode with the website being dynamic and the data stored in a SVG
2. Performs transformations on the ESG data to retrieve company ESG scores as well as the corresponding dates those score were given
- Using regex to filter raw html
3. Grabs historical stock price data for the company
- Using the yfinance API
4. Merges the two data sources into a single dataframe
- Using pandas data manipulation methods
5. Plots ESG scores against stock price
- Using the matplotlib module
6. Delivered to the user via a nice(ish), interactable website
- Using flask to render the html and control GET and POST requests

# Pre-requisites
- Python 3
- Pip
- Git

# Installation Instructions
The app is hosted online at: https://esg-web-scraper.herokuapp.com/

... but for those wanting to run locally:

1. Open command prompt (windows) or terminal (mac/linux)
2. Navigate to a path for which to host project files e.g
```
cd C:\project
```
3. Clone repo (note: this clones the **run-app-locally** branch)
```
git clone -b run-app-locally https://github.com/kulsuri/jupiter-coding-test
```
4. Navigate to the project folder e.g.
```
cd C:\project\jupiter-coding-test
```
5. Install required modules
```
pip install -r requirements.txt 
```

# Running the App
1. Navigate to the project folder and run the command:
```
python app.py
```
2. In the web browser, open:
```
http://localhost:5000/
```

# Technologies
- python 3
- selenium
- flask
- yfinance
- matplotlib
- pandas
- regex

# How Does It Work?

- get_stock_price.py # get stock price data
- get_esg_scores.py # get ESG scores for stock price from MSCI
- transform_the_data.py # transform data and create data frame
- create_sql_lite_db.py # create the sql lite database
- insert_data_to_sql_db.py # insert the scraped data into the sql lite database
- app.py # run the flask app / control routes / call python modules

# Loadin Data to Relational DB
- Request type:

# Bugs and Issues

The solution allows for scaling due to:
- suitable error handling
- url validation reducing computational expense
- url normalization/formatting to prevent replication in the database
- built with functional programming in mind
- shortened urls are stored in a sqlite database, separate to the code, for fast retrieval 

How I would scale the app:
- run the application on a proper web server such as Apache or Nginx that supports execution of python
- these will easily handle many simultaneous connections