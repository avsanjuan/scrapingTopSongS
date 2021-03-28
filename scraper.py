# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

#import urllib3
import requests
#import re
#import time
from bs4 import BeautifulSoup
#from dateutil import parser
from requests.exceptions import HTTPError 

#from reason_classifier import ReasonClassifier
class Scraper():

    def __init__(self):
        self.url ="https://www.elportaldemusica.es/lists/top-100-canciones/2020"
        self.subdomain = "/database.htm"
        self.find_arg = [
                        ['p','class','single-list-entry-rank-position'],
                        ['div', 'class','name'],
                        ['div', 'class','related'],
                        ['div', 'class','list_week'],
                        ['span', 'class','number'],
                        ]
        self.data = []
        
    def requestPage(self):  
        try:
            raw_html = requests.get(self.url, verify=False)
            try:
                html = BeautifulSoup(raw_html.text, features='html.parser')
                return html
            except:
                print('Error parsing HTML code')
                return None
        except HTTPError as e:
            print(e.reason)
            return None

    def __download_html(self, url):
        html = self.requestPage()
        return html
    
    def extract_data(self, html, arg1, arg2, arg3):
        result = html.find_all(arg1, {arg2: arg3})
        return result
    
    def execute_scraper(self):
        html = self.__download_html(self.url)
        if html is not None:
            j=0;
            for fa in self.find_arg:
                result = self.extract_data(html, fa[0], fa[1], fa[2])
                i=0;
                for rs in result:
                    if j == 0:
                        self.data.append(1)
                        self.data[i]=rs.string.strip()
                    else:
                        self.data[i]=str(self.data[i]) + ';' + str(rs.string.strip())
                    i=i+1
                j=j+1
           
                
    def data2csv(self, filename):
        #file = open("../csv/" + filename, "w+")
        file = open(filename, "w+")
        for dt in self.data:
                file.write(dt + "\n");
		
            
     
            