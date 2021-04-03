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
        self.url ="https://www.elportaldemusica.es/lists/top-100-canciones/"
        self.subdomain = "/database.htm"
        self.find_arg = [
                        ["p","class","single-list-entry-rank-position"],
                        ["div", "class","name"],
                        ["div", "class","related"],
                        ["div", "class","list_week"],
                        ["span", "class","number"],
                        ]
        self.data = []
        self.years = [2009 , 2010 , 2011 , 2012 , 2013 , 2014 , 2015 , 2016 , 2017 , 2018 , 2019 , 2020]
        
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

    def __download_html(self):
        html = self.requestPage()
        return html
    
    def extract_data(self, html, arg1, arg2, arg3):
        #print(html)
        result = html.find_all(arg1, {arg2: arg3})
        return result
    
    def execute_scraper(self):
        url2 = self.url
        i=0
        j=0
        k=0
        for ya in self.years:
            self.url = url2 + str(ya)
            print(self.url)
            html = self.__download_html()
            if html is not None:
                j=0;
                for fa in self.find_arg:
                    result = self.extract_data(html, fa[0], fa[1], fa[2])
                    i=k;
                    for rs in result:
                        if j == 0:
                            self.data.append(1)
                            self.data[i]=str(ya) + ';' + str(rs.string.strip())
                            #self.data[i]=str(rs.string.strip())
                        else:
                            self.data[i]=str(self.data[i]) + ';' + str(rs.string.strip())
                        i=i+1
                    j=j+1
                k=i
               
                
    def data2csv(self, filename):
        #file = open("../csv/" + filename, "w+")
        file = open(filename, "w+")
        for dt in self.data:
                 file.write(str(dt) + "\n");
		
            
     
            