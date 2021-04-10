from get_stock_price import historicalPrices
import pandas as pd

class createDF:
    def __init__(self, company_ticker, esg_data): #, price_data):
        self.company_ticker = company_ticker
        self.esg_list = esg_data[0]
        self.dates_list = esg_data[1]

    # convert output from tranform.py to df
    def convert_esg_data_to_df(self):
        esg_df = pd.DataFrame(list(zip(self.esg_list, self.dates_list)), columns = ['ESG Score', 'Date'])
        esg_df['Date'] = pd.to_datetime( esg_df['Date'], format='%b-%y')
        esg_df = esg_df.set_index('Date')
        return esg_df
    
    def get_price_data(self, esg_df):
        start_date = esg_df.index.min()
        end_date = esg_df.index.max() + pd.DateOffset(30)
        price_data_df = historicalPrices(self.company_ticker, start_date, end_date).get_ticker_price_data()
        return price_data_df

    def calculate_monthly_avg_price(self, price_data_df):
        price_data_df_monthly_avg = price_data_df.resample('M').mean()
        return price_data_df_monthly_avg

    def create_YYYYMM_cols_to_merge_dfs(self, price_data_df_monthly_avg, esg_df):
        price_data_df_monthly_avg['YYYY-MM Date'] = price_data_df_monthly_avg.index.get_level_values('Date').to_period('M')
        esg_df['YYYY-MM Date'] = esg_df.index.get_level_values('Date').to_period('M')
        esg_price_joined_df = pd.merge(esg_df, price_data_df_monthly_avg, on=['YYYY-MM Date'], how='inner')
        return esg_price_joined_df

    def drop_unnecessary_cols(self, esg_price_joined_df):
        esg_price_joined_df_simplified = esg_price_joined_df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis = 1)
        esg_price_joined_df_simplified = esg_price_joined_df_simplified.set_index('YYYY-MM Date')
        return esg_price_joined_df_simplified

    def initializeDF(self):
        esg_df = self.convert_esg_data_to_df()
        price_data_df = self.get_price_data(esg_df)
        price_data_df_monthly_avg = self.calculate_monthly_avg_price(price_data_df)
        esg_price_joined_df = self.create_YYYYMM_cols_to_merge_dfs(price_data_df_monthly_avg, esg_df)
        esg_price_joined_df_simplified = self.drop_unnecessary_cols(esg_price_joined_df)
        return esg_price_joined_df_simplified
