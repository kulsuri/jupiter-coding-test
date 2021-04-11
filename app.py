from get_esg_score import bot
from get_stock_price import historicalPrices
from transform import transformESGData
from create_pandas_df import createDF
from visualisation_engine import visualisationEngine

import matplotlib.pyplot as plt
import pprint

ticker_symbol = 'jpm'

data1 = bot(ticker_symbol).initializeScrapeProcess()
data2 = transformESGData(data1).initializeESGTranformProcess()
data3 = createDF(ticker_symbol, data2).initializeDF()
data4 = visualisationEngine(data3).initializePlot()

# data4
# plt.show()