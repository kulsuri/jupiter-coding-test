from get_esg_score import bot
from get_stock_price import historicalPrices
from transform import transformESGData
from create_pandas_df import createDF
import pprint

ticker_symbol = 'goog'

data1 = bot(ticker_symbol).initializeScrapeProcess()
data2 = transformESGData(data1).initializeESGTranformProcess()
data3 = createDF(ticker_symbol, data2).initializeDF()


print(data3)