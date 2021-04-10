import yfinance as yf

class historicalPrices:
    def __init__(self, ticker_symbol, startDate, endDate):
        self.ticker_symbol = ticker_symbol
        self.start_date = startDate
        self.end_state = endDate
    
    def get_data(self):
        stock_price_data = yf.download(company_ticker, startDate, endDate)
        return stock_price_data