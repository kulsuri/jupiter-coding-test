from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import os

class bot:
    def __init__(self, company_ticker):
        self.company_ticker = company_ticker
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--headless")
        ####
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=self.chrome_options)
        ###
        
        #self.driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver_win32\chromedriver.exe'), options=self.chrome_options)
        self.driver.get('https://www.msci.com/our-solutions/esg-investing/esg-ratings/esg-ratings-corporate-search-tool/issuer/')

    def accept_cookies(self):
        cookie_accept_xpath = '//*[@id="portlet_mscicookiebar_WAR_mscicookiebar"]/div/div[2]/div/div/div[1]/div/button[1]'
        self.clickButton(cookie_accept_xpath)
        time.sleep(1)

    def search_for_company(self):
        company_search_field_xpath = '//*[@id="_esgratingsprofile_keywords"]'
        self.enterData(company_search_field_xpath, self.company_ticker)

    def select_company(self):
        company_search_dropdown = '//*[@id="ui-id-1"]' #/li'
        self.clickButton(company_search_dropdown)
        
    def get_esg_ratings(self):
        esg_ratings_xpath = '//*[@id="_esgratingsprofile_esg-rating-history"]'
        esg_data = self.grabData(esg_ratings_xpath)
        return esg_data

    def grabData(self, xpath):
        try:
            data = self.driver.find_element_by_xpath(xpath)
        except Exception:
            time.sleep(2)
            data = self.driver.find_element_by_xpath(xpath)
        return data

    def clickButton(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception:
            time.sleep(2)
            self.clickButton(xpath)

    def enterData(self, xpath, data):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(data)
            pass
        except Exception:
            time.sleep(1)
            self.enterData(field, data)

    def initializeScrapeProcess(self):
        self.accept_cookies()
        self.search_for_company()
        self.select_company()
        data = self.get_esg_ratings().get_attribute('innerHTML')
        self.driver.quit()
        return data