from get_esg_score import bot
from get_stock_price import historicalPrices
from transform import transformESGData
from create_pandas_df import createDF
from visualisation_engine import visualisationEngine
from flask import Flask, render_template, request

app = Flask(__name__)
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