# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import urllib3
import requests
import re
import time
from bs4 import BeautifulSoup
from dateutil import parser
from requests.exceptions import HTTPError 

#from reason_classifier import ReasonClassifier
class Scraper():

    def __init__(self):
        self.url ="https://www.elportaldemusica.es/lists/top-100-canciones/2020"
        self.subdomain = "/database.htm"
        self.data = []
        #self.geolocator = Yandex()
        #self.reason_classifier = (
        #ReasonClassifier("../train/summary_train_set.txt"))
        
        
    def requestPage(url):  
        try:
            raw_html = requests.get(url)
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
        #self.response = urllib3.request(url)
        #html = self.response.read()
        html = self.requestPage()
       # html = requestPage(url)
        return html
    
    
    def execute_scraper(self):
        html = self.__download_html(self.url)
        print('Hola mundo')
        print(html)
        

    #print('hola mundo')