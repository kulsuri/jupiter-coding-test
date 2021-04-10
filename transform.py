import pandas as pd
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

    #def convert_to_df(self, esg_list, dates_list):


    def initializeESGTranformProcess(self):
        search_points_esg = self.find_search_points_in_html_string(self.raw_html_str_data)
        esg_scores = self.filter_esg_scores_from_search_points(self.raw_html_str_data, search_points_esg)
        dates = self.filter_esg_dates_from_html_string(self.raw_html_str_data)
        data = [esg_scores, dates]
        return data


# test_data = '''('<div id="highcharts-y3208n8-0" dir="ltr" class="highcharts-container " '
#  'style="position: relative; overflow: hidden; width: 321px; height: 250px; '
#  'text-align: left; line-height: normal; z-index: 0; '
#  '-webkit-tap-highlight-color: rgba(0, 0, 0, 0); color: rgb(0, 32, 54);"><svg '
#  'version="1.1" class="highcharts-root" style="font-family:\'Roboto Regular\', '
#  'sans-serif;;font-size:12px;;color:#002036;fill:#002036;" '
#  'xmlns="http://www.w3.org/2000/svg" width="321" height="250" viewBox="0 0 321 '
#  '250"><desc>Created with Highcharts 7.2.0</desc><defs><clipPath '
#  'id="highcharts-y3208n8-1-"><rect x="0" y="0" width="257" height="172" '
#  'fill="none"></rect></clipPath><clipPath id="highcharts-y3208n8-8-"><rect '
#  'x="0" y="0" width="331" height="200" fill="none"></rect></clipPath><clipPath '
#  'id="highcharts-y3208n8-21-"><rect x="0" y="0" width="271" height="172" '
#  'fill="none"></rect></clipPath><clipPath id="highcharts-y3208n8-22-"><rect '
#  'x="0" y="0" width="257" height="172" '
#  'fill="none"></rect></clipPath></defs><rect fill="#ffffff" '
#  'class="highcharts-background" x="0" y="0" width="321" height="250" rx="0" '
#  'ry="0"></rect><rect fill="none" class="highcharts-plot-background" x="54" '
#  'y="10" width="257" height="172"></rect><g class="highcharts-grid '
#  'highcharts-xaxis-grid" data-z-index="1"><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 104.5 10 L 104.5 182" '
#  'opacity="1"></path><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 156.5 10 L 156.5 182" '
#  'opacity="1"></path><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 207.5 10 L 207.5 182" '
#  'opacity="1"></path><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 259.5 10 L 259.5 182" '
#  'opacity="1"></path><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 310.5 10 L 310.5 182" '
#  'opacity="1"></path><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 53.5 10 L 53.5 182" '
#  'opacity="1"></path></g><g class="highcharts-grid highcharts-yaxis-grid" '
#  'data-z-index="1"><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 54 182.5 L 311 182.5" '
#  'opacity="1"></path><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 54 159.5 L 311 159.5" '
#  'opacity="1"></path><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 54 136.5 L 311 136.5" '
#  'opacity="1"></path><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 54 113.5 L 311 113.5" '
#  'opacity="1"></path><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 54 90.5 L 311 90.5" '
#  'opacity="1"></path><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 54 67.5 L 311 67.5" '
#  'opacity="1"></path><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 54 44.5 L 311 44.5" '
#  'opacity="1"></path><path fill="none" data-z-index="1" '
#  'class="highcharts-grid-line" d="M 54 21.5 L 311 21.5" '
#  'opacity="1"></path></g><rect fill="none" class="highcharts-plot-border" '
#  'data-z-index="1" x="54" y="10" width="257" height="172"></rect><g '
#  'class="highcharts-axis highcharts-xaxis" data-z-index="2"><path fill="none" '
#  'class="highcharts-axis-line" stroke="#002036" stroke-width="1" '
#  'data-z-index="7" d="M 54 182.5 L 311 182.5"></path></g><g '
#  'class="highcharts-axis highcharts-yaxis" data-z-index="2"><path fill="none" '
#  'class="highcharts-axis-line" stroke="#002036" stroke-width="1" '
#  'data-z-index="7" d="M 53.5 10 L 53.5 182"></path></g><g '
#  'class="highcharts-series-group" data-z-index="3"><g data-z-index="0.1" '
#  'class="highcharts-series highcharts-series-0 highcharts-line-series " '
#  'transform="translate(54,10) scale(1 1)" '
#  'clip-path="url(#highcharts-y3208n8-22-)"><path fill="none" d="M 25.7 '
#  '11.46666666666667 L 77.1 11.46666666666667 L 128.5 11.46666666666667 L 179.9 '
#  '11.46666666666667 L 231.3 11.46666666666667" class="highcharts-graph" '
#  'data-z-index="1" stroke="#002036" stroke-width="2" stroke-linejoin="round" '
#  'stroke-linecap="round"></path><path fill="none" d="M 15.7 11.46666666666667 '
#  'L 25.7 11.46666666666667 L 77.1 11.46666666666667 L 128.5 11.46666666666667 '
#  'L 179.9 11.46666666666667 L 231.3 11.46666666666667 L 241.3 '
#  '11.46666666666667" visibility="visible" data-z-index="2" '
#  'class="highcharts-tracker-line" stroke-linejoin="round" '
#  'stroke="rgba(192,192,192,0.0001)" stroke-width="22"></path></g><g '
#  'data-z-index="0.1" class="highcharts-markers highcharts-series-0 '
#  'highcharts-line-series  highcharts-tracker" transform="translate(54,10) '
#  'scale(1 1)" clip-path="none"><path fill="#007567" d="M 25 31 A 20 20 0 1 1 '
#  '25.01999999666668 30.999990000000835 Z" opacity="1" '
#  'class="highcharts-point"></path><path fill="#007567" d="M 77 31 A 20 20 0 1 '
#  '1 77.01999999666668 30.999990000000835 Z" opacity="1" '
#  'class="highcharts-point"></path><path fill="#007567" d="M 128 31 A 20 20 0 1 '
#  '1 128.01999999666668 30.999990000000835 Z" opacity="1" '
#  'class="highcharts-point"></path><path fill="#007567" d="M 179 31 A 20 20 0 1 '
#  '1 179.01999999666668 30.999990000000835 Z" opacity="1" '
#  'class="highcharts-point"></path><path fill="#007567" d="M 231 31 A 20 20 0 1 '
#  '1 231.01999999666668 30.999990000000835 Z" opacity="1" '
#  'class="highcharts-point"></path></g></g><text x="10" '
#  'class="highcharts-title" data-z-index="4" '
#  'style="color:#333333;font-size:18px;fill:#333333;" y="24"></text><text '
#  'x="161" text-anchor="middle" class="highcharts-subtitle" data-z-index="4" '
#  'style="color:#666666;fill:#666666;" y="24"></text><text x="10" '
#  'text-anchor="start" class="highcharts-caption" data-z-index="4" '
#  'style="color:#666666;fill:#666666;" y="247"></text><g data-z-index="6" '
#  'class="highcharts-data-labels highcharts-series-0 highcharts-line-series " '
#  'transform="translate(54,10) scale(1 1)" opacity="1"><g '
#  'class="highcharts-label highcharts-data-label '
#  'highcharts-data-label-color-undefined" data-z-index="1" '
#  'transform="translate(6,-2)"><text x="5" data-z-index="1" '
#  'style="font-size:14px;;font-weight:bold;color:#FFFFFF;fill:#FFFFFF;" '
#  'y="19">AAA</text></g><g class="highcharts-label highcharts-data-label '
#  'highcharts-data-label-color-undefined" data-z-index="1" '
#  'transform="translate(57,-2)"><text x="5" data-z-index="1" '
#  'style="font-size:14px;;font-weight:bold;color:#FFFFFF;fill:#FFFFFF;" '
#  'y="19">AAA</text></g><g class="highcharts-label highcharts-data-label '
#  'highcharts-data-label-color-undefined" data-z-index="1" '
#  'transform="translate(109,-2)"><text x="5" data-z-index="1" '
#  'style="font-size:14px;;font-weight:bold;color:#FFFFFF;fill:#FFFFFF;" '
#  'y="19">AAA</text></g><g class="highcharts-label highcharts-data-label '
#  'highcharts-data-label-color-undefined" data-z-index="1" '
#  'transform="translate(160,-2)"><text x="5" data-z-index="1" '
#  'style="font-size:14px;;font-weight:bold;color:#FFFFFF;fill:#FFFFFF;" '
#  'y="19">AAA</text></g><g class="highcharts-label highcharts-data-label '
#  'highcharts-data-label-color-undefined" data-z-index="1" '
#  'transform="translate(212,-2)"><text x="5" data-z-index="1" '
#  'style="font-size:14px;;font-weight:bold;color:#FFFFFF;fill:#FFFFFF;" '
#  'y="19">AAA</text></g></g><g class="highcharts-axis-labels '
#  'highcharts-xaxis-labels" data-z-index="7"><text x="82.99983164553723" '
#  'style="color:#002036;cursor:default;font-size:14px;;fill:#002036;" '
#  'text-anchor="end" transform="translate(0,0) rotate(-45 82.99983164553723 '
#  '200)" y="200" opacity="1">May-17</text><text x="134.39983164553723" '
#  'style="color:#002036;cursor:default;font-size:14px;;fill:#002036;" '
#  'text-anchor="end" transform="translate(0,0) rotate(-45 134.39983164553723 '
#  '200)" y="200" opacity="1">Jun-18</text><text x="185.7998316455372" '
#  'style="color:#002036;cursor:default;font-size:14px;;fill:#002036;" '
#  'text-anchor="end" transform="translate(0,0) rotate(-45 185.7998316455372 '
#  '200)" y="200" opacity="1">Mar-19</text><text x="237.19983164553724" '
#  'style="color:#002036;cursor:default;font-size:14px;;fill:#002036;" '
#  'text-anchor="end" transform="translate(0,0) rotate(-45 237.19983164553724 '
#  '200)" y="200" opacity="1">Feb-20</text><text x="288.5998316455372" '
#  'style="color:#002036;cursor:default;font-size:14px;;fill:#002036;" '
#  'text-anchor="end" transform="translate(0,0) rotate(-45 288.5998316455372 '
#  '200)" y="200" opacity="1">Mar-21</text></g><g class="highcharts-axis-labels '
#  'highcharts-yaxis-labels" data-z-index="7"><text x="0" '
#  'style="color:#002036;cursor:default;font-size:14px;;fill:#002036;" '
#  'text-anchor="end" transform="translate(0,0)" y="-9999">-1</text><text x="39" '
#  'style="color:#002036;cursor:default;font-size:14px;;fill:#002036;" '
#  'text-anchor="end" transform="translate(0,0)" y="165" '
#  'opacity="1">CCC</text><text x="39" '
#  'style="color:#002036;cursor:default;font-size:14px;;fill:#002036;" '
#  'text-anchor="end" transform="translate(0,0)" y="142" '
#  'opacity="1">B</text><text x="39" '
#  'style="color:#002036;cursor:default;font-size:14px;;fill:#002036;" '
#  'text-anchor="end" transform="translate(0,0)" y="119" '
#  'opacity="1">BB</text><text x="39" '
#  'style="color:#002036;cursor:default;font-size:14px;;fill:#002036;" '
#  'text-anchor="end" transform="translate(0,0)" y="96" '
#  'opacity="1">BBB</text><text x="39" '
#  'style="color:#002036;cursor:default;font-size:14px;;fill:#002036;" '
#  'text-anchor="end" transform="translate(0,0)" y="73" '
#  'opacity="1">A</text><text x="39" '
#  'style="color:#002036;cursor:default;font-size:14px;;fill:#002036;" '
#  'text-anchor="end" transform="translate(0,0)" y="50" '
#  'opacity="1">AA</text><text x="39" '
#  'style="color:#002036;cursor:default;font-size:14px;;fill:#002036;" '
#  'text-anchor="end" transform="translate(0,0)" y="27" '
#  'opacity="1">AAA</text></g><g class="highcharts-label highcharts-tooltip '
#  'highcharts-color-undefined" style="pointer-events:none;white-space:nowrap;" '
#  'data-z-index="8" transform="translate(385,-9999)" opacity="0" '
#  'visibility="visible"><path fill="none" class="highcharts-label-box '
#  'highcharts-tooltip-box highcharts-shadow" d="M 3.5 0.5 L 35.5 0.5 41.5 -5.5 '
#  '47.5 0.5 82 0.5 C 85.5 0.5 85.5 0.5 85.5 3.5 L 85.5 27.5 C 85.5 30.5 85.5 '
#  '30.5 82.5 30.5 L 3.5 30.5 C 0.5 30.5 0.5 30.5 0.5 27.5 L 0.5 3.5 C 0.5 0.5 '
#  '0.5 0.5 3.5 0.5" stroke="#000000" stroke-opacity="0.049999999999999996" '
#  'stroke-width="5" transform="translate(1, 1)"></path><path fill="none" '
#  'class="highcharts-label-box highcharts-tooltip-box highcharts-shadow" d="M '
#  '3.5 0.5 L 35.5 0.5 41.5 -5.5 47.5 0.5 82 0.5 C 85.5 0.5 85.5 0.5 85.5 3.5 L '
#  '85.5 27.5 C 85.5 30.5 85.5 30.5 82.5 30.5 L 3.5 30.5 C 0.5 30.5 0.5 30.5 0.5 '
#  '27.5 L 0.5 3.5 C 0.5 0.5 0.5 0.5 3.5 0.5" stroke="#000000" '
#  'stroke-opacity="0.09999999999999999" stroke-width="3" '
#  'transform="translate(1, 1)"></path><path fill="none" '
#  'class="highcharts-label-box highcharts-tooltip-box highcharts-shadow" d="M '
#  '3.5 0.5 L 35.5 0.5 41.5 -5.5 47.5 0.5 82 0.5 C 85.5 0.5 85.5 0.5 85.5 3.5 L '
#  '85.5 27.5 C 85.5 30.5 85.5 30.5 82.5 30.5 L 3.5 30.5 C 0.5 30.5 0.5 30.5 0.5 '
#  '27.5 L 0.5 3.5 C 0.5 0.5 0.5 0.5 3.5 0.5" stroke="#000000" '
#  'stroke-opacity="0.15" stroke-width="1" transform="translate(1, '
#  '1)"></path><path fill="rgba(247,247,247,0.85)" class="highcharts-label-box '
#  'highcharts-tooltip-box" d="M 3.5 0.5 L 35.5 0.5 41.5 -5.5 47.5 0.5 82 0.5 C '
#  '85.5 0.5 85.5 0.5 85.5 3.5 L 85.5 27.5 C 85.5 30.5 85.5 30.5 82.5 30.5 L 3.5 '
#  '30.5 C 0.5 30.5 0.5 30.5 0.5 27.5 L 0.5 3.5 C 0.5 0.5 0.5 0.5 3.5 0.5" '
#  'stroke="#007567" stroke-width="1"></path><text x="8" data-z-index="1" '
#  'style="font-size:12px;color:#333333;cursor:default;fill:#333333;" '
#  'y="20"><tspan style="font-weight:bold">Feb-20: '
#  'AAA</tspan></text></g></svg></div>')'''

# tf1 = transformESGData(test_data).initializeESGTranformProcess()
# print(tf1)