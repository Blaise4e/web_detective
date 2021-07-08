# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib.request
import csv
import numpy as np

""
#specify the url
urlpage= "https://books.toscrape.com/"
#request the url
req = requests.get(urlpage)
#parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(req.text, 'html.parser')

list_pages = ['https://books.toscrape.com/catalogue/page-' + str(i) + '.html' for i in range(51)]
del list_pages[0]
list_pages[0] = "https://books.toscrape.com/"

str_price_dirty_list, str_rating_dirty_list ,str_disp_dirty_list, str_title_dirty_list = [],[],[],[]
for i in list_pages:
#def scrap_datas(i)
    urlpage= i
#request the url
    req = requests.get(urlpage)
#parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(req.text, 'html.parser')
        
    #find all the price of the page
    price = soup.find_all("p",{"class" : "price_color"} )
    str_price_dirty = str(price)
    str_price_dirty_list.append(str_price_dirty)
    
    rating = soup.find_all("p", {"class": "star-rating"})
    str_rating_dirty= str(rating)
    str_rating_dirty_list.append(str_rating_dirty)

    disp = soup.find_all("p", {"class": "instock availability"})
    str_disp_dirty= str(disp)
    str_disp_dirty_list.append(str_disp_dirty)
    
    #find title
    title = soup.find_all("img",{"class": "thumbnail"} )
    str_title_dirty= str(title)
    str_title_dirty_list.append(str_title_dirty)
 
    #return str_price_dirty_list, str_rating_dirty_list ,str_disp_dirty, str_title_dirty_list




