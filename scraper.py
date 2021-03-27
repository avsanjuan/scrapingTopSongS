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
        #self.response = urllib3.request(url)
        #html = self.response.read()
        html = self.requestPage()
       # html = requestPage(url)
        return html
    
    
    def execute_scraper(self):
        print(self.url)
        print('paso 0')
        html = self.__download_html(self.url)
        print('paso 1')
        if html is not None:
            print('paso 2')
        # Search wallpapers URL
            ranking = html.find_all('p', {'class': 'single-list-entry-rank-position '})
            print(ranking)
            for rk in ranking:
                i = rk.find('p')
                print(i)
                #img = wp.find('img')
                #images.append(img.attrs['src'])
    
            # Search for next page URL
            #try:
            #    more_button = html.find('a', {'class':'more'})
            #    next_page = more_button.attrs['href']
            #except:
            #    pass
        #print('Hola mundo')
        #print(html)
        

    #print('hola mundo')