#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:49:24 2021

@author: angel
"""

from scraper import Scraper

output_file = "../csv/dataset.csv"

scraper = Scraper();
scraper.execute_scraper();
scraper.data2csv(output_file);
