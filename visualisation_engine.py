import matplotlib.pyplot as plt

class visualisationEngine:
    def __init__(self, esg_price_df):
        self.esg_price_df = esg_price_df

    def assign_num_val_to_esg_scores(self):
        esg_score_to_num_map = {
            'AAA' : 9,
            'AA' : 8,
            'A' : 7,
            'BBB' : 6,
            'BB' : 5,
            'B' : 4,
            'CCC' : 3,
            'CC' : 2,
            'C' : 1
        }

        plotable_df = self.esg_price_df
        plotable_df['ESG Value'] = plotable_df['ESG Score'].map(esg_score_to_num_map)
        return plotable_df

    def plot_df(self, plotable_df):
        plotable_df.plot(y='Adj Close')
        bx = plotable_df['ESG Value'].plot(secondary_y=True, color='k', marker='o')
        return bx #plt.show()

    def initializePlot(self):
        df = self.assign_num_val_to_esg_scores()
        viz = self.plot_df(df)
        plot_img = viz.figure.savefig('static/my_plot.png')
        return plot_img