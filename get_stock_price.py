import yfinance as yf

class historicalPrices:
    def __init__(self, ticker_symbol, startDate, endDate):
        self.ticker_symbol = ticker_symbol
        self.start_date = startDate
        self.end_date = endDate
    
    def get_ticker_price_data(self):
        stock_price_data = yf.download(self.ticker_symbol, self.start_date, self.end_date)
        return stock_price_data