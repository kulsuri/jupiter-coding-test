import re

class transformESGData:
    def __init__(self, raw_html_str_data):
        self.raw_html_str_data = raw_html_str_data

    def find_search_points_in_html_string(self, html_string):
        search_points_esg_in_html_string = []
        for i in re.finditer('style="font-size:14px;;font-weight:bold;color:#FFFFFF', html_string):
        #print('text found', i.start(), i.end())
            search_points_esg_in_html_string.append(i.end())

        search_points_esg_in_html_string.append( search_points_esg_in_html_string[-1] + 50 )
        return search_points_esg_in_html_string

    def filter_esg_scores_from_search_points(self, html_string, search_points_esg):
        esg_scores = []
        for index, value in enumerate(search_points_esg):
            if value == search_points_esg[-1]:
                break
            else:
                result = re.search('">(.*)</text>', html_string[ search_points_esg[index]: search_points_esg[index+1] ])
                esg_scores.append(result.group(1))
        return esg_scores

    def filter_esg_dates_from_html_string(self, html_string):
        dates = re.findall(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\-\d{2}', html_string)
        return dates

    def initializeESGTranformProcess(self):
        search_points_esg = self.find_search_points_in_html_string(self.raw_html_str_data)
        esg_scores = self.filter_esg_scores_from_search_points(self.raw_html_str_data, search_points_esg)
        dates = self.filter_esg_dates_from_html_string(self.raw_html_str_data)
        data = [esg_scores, dates]
        return data