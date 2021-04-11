# esg-web-scraper
https://esg-web-scraper.herokuapp.com/

Is there a correlation between the ESG rating and the stock price for a company?

# Screenshot
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

# Run the App
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

File | Technology | What Does It Do
--- | --- | ---
`app.py` | flask | runs the app, handles routes, renders templates and calls objects from the other files
`get_esg_score.py` | selenium | scrapes data from the [MSCI ESG Ratings Corporate Search Tool](https://www.msci.com/our-solutions/esg-investing/esg-ratings/esg-ratings-corporate-search-tool/issuer/) website
`transform.py` | regex | performs transformations on the raw html to retrieve company ESG scores as well as the corresponding dates those score were given
`get_stock_price.py` | yfinance | gets historical stock price data for the company
`create_pandas_df.py` | pandas | merges the two data sources into a single dataframe
`visualisation_engine.py` | matplotlib | assigns a numerical mapping to the ESG scores and plots these against the stock price

- get_stock_price.py # get stock price data
- get_esg_scores.py # get ESG scores for stock price from MSCI
- transform_the_data.py # transform data and create data frame
- create_sql_lite_db.py # create the sql lite database
- insert_data_to_sql_db.py # insert the scraped data into the sql lite database
- app.py # run the flask app / control routes / call python modules

# Loading Data to Relational DB
1. Import SQLAlchemy and create a sqllite db
- This will be our (mini) data warehouse
1. Create/insert tables with the below schema using 3NF and snowflake principles
<a href="https://ibb.co/QfrhW6w"><img src="https://i.ibb.co/SPRHkKC/schema.png" alt="schema" border="0"></a><br /><a target='_blank' href='https://the-crosswordsolver.com/tag/presuppose'></a><br />
3. In the ETL process, create dataframes which match the schema of the sql database
4. Open a connection to the database
5. Use pandas to_sql() function to write records stored in the dataframe to the sql database
6. Close the connection to the database

# Bugs and Issues
:x: Sometimes graphs fail to render due to browser caching handling

:x: Response times are slower than desired due to data scraping method using selenium (despite optimizations)

# Feature Requests and Improvements
:black_square_button: More ESG data sources

:black_square_button: Apply non-numerical elements to the ESG scores on the graphs

:black_square_button:	Improve response times

:black_square_button:	Resolve caching issues preventing new graphs to be displayed

:black_square_button:	Add data validation and error handling

:black_square_button: Create unit tests and integration tests

:black_square_button:	Build CI/CD pipeline