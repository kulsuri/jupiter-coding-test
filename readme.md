### esg-web-scraper
https://esg-web-scraper.herokuapp.com/

Is there a correlation between the ESG rating and the stock price for a company?

### What Does This App Do?
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

### Pre-requisites
- Python 3
- Pip
- Git

### Installation Instructions
The app is hosted online at: https://esg-web-scraper.herokuapp.com/

... but for those wanting to run locally:

1. Open command prompt (windows) or terminal (mac/linux)
2. Navigate to a path for which to host project files e.g
```
cd C:\project
```
3. Clone repo (note: this clones the **run-app-locally branch**, as master is configured slightly differently for CI and cloud deployment)
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
6. Run the app
```
python app.py
```
7. Open the web browser and open http://localhost:5000/
```
http://localhost:5000/
```

# Technologies
- python
- selenium
- flask
- yfinance
- matplotlib
- pandas
- regex

### File Structure

- get_stock_price.py # get stock price data
- get_esg_scores.py # get ESG scores for stock price from MSCI
- transform_the_data.py # transform data and create data frame
- create_sql_lite_db.py # create the sql lite database
- insert_data_to_sql_db.py # insert the scraped data into the sql lite database
- app.py # run the flask app / control routes / call python modules

# Running the App
1. Run the command: 
```
python app.py
```
2. Use an application like Postman to make GET/POST requests
- Note: if you want a new empty database, please delete the urls.db and re-run app.py in step 1 

# Shorten URL Example - POST Request
- Request type:
```
POST
```
- URL: 
```
localhost:5000/shorten_url
```
- Headers: 
```
{'Content-Type': 'application/json'}
```
- Body: 
```
{'url': 'www.babylonhealth.com'}
``` 
- Response: 
```
{"shortened_url": "http://localhost:5000/25t52"}
```

# Redirect Example - GET Request
- Request type:
```
GET
```
- URL: 
```
localhost:5000/25t52
```
- Response: redirected to the the original URL (http://babylonhealth.com) / returned the contents of the original URL

# View SQLite Database - GET Request
- Request type:
```
GET
```
- URL: 
```
localhost:5000
```
- Response:
```
[
  [
    1, 
    "http://w3.com", 
    "867nv"
  ], 
  [
    2, 
    "http://babylonhealth.com", 
    "25t52"
  ], 
  [
    3, 
    "http://google.com", 
    "ghpzy"
  ], 
  [
    4, 
    "http://theverge.com", 
    "6vyv6"
  ], 
  [
    5, 
    "http://hotukdeals.com", 
    "pbq8b"
  ], 
  [
    6, 
    "http://youtube.com", 
    "4xct4"
  ]
]
```
# Scaling
The solution allows for scaling due to:
- suitable error handling
- url validation reducing computational expense
- url normalization/formatting to prevent replication in the database
- built with functional programming in mind
- shortened urls are stored in a sqlite database, separate to the code, for fast retrieval 

How I would scale the app:
- run the application on a proper web server such as Apache or Nginx that supports execution of python
- these will easily handle many simultaneous connections