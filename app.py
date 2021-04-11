from get_esg_score import bot
from get_stock_price import historicalPrices
from transform import transformESGData
from create_pandas_df import createDF
from visualisation_engine import visualisationEngine
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST', "GET"])
def my_form_post():
    ticker = request.form['text']
    if ticker != "":
        df = web_scraper(ticker)
        return display_data(df)
    else:
        return render_template("index.html")

# No caching at all for API endpoints.
# @app.after_request
# def add_header(response):
#     # response.cache_control.no_store = True
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '-1'
#     return response

def display_data(df):
    return render_template("data.html", tables=[df.to_html(classes='data')], titles=df.columns.values, user_image = 'static/my_plot.png')

def web_scraper(ticker_symbol):
    data1 = bot(ticker_symbol).initializeScrapeProcess()
    data2 = transformESGData(data1).initializeESGTranformProcess()
    data3 = createDF(ticker_symbol, data2).initializeDF()
    visualisationEngine(data3).initializePlot()
    return data3

if __name__ == '__main__':
    app.run(threaded=True, port=5000)