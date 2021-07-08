# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib.request
import csv
import numpy as np


main_url = "https://books.toscrape.com/"
result = requests.get(main_url)
soup = BeautifulSoup(result.text, 'html.parser')



#find all the price of the page
price = soup.find_all("p",{"class" : "price_color"} )
str_price_dirty = str(price)

rating = soup.find_all("p", {"class": "star-rating"})
str_rating_dirty= str(rating)

disp = soup.find_all("p", {"class": "instock availability"})
str_disp_dirty= str(disp)

#find title
title = soup.find_all("img",{"class": "thumbnail"} )
str_title_dirty= str(title)



#print(str_price_dirty[0])

# Cleaning price
str_price_dirty = str_price_dirty.replace('<p class="price_color">Â£', "")
str_price_dirty = str_price_dirty.replace('</p>', "")
str_price_dirty = str_price_dirty.replace(' ', "")
str_price_dirty = str_price_dirty.replace('[', "")
str_price_dirty = str_price_dirty.replace(']', "")
str_price = str_price_dirty.split(",")
price = [float(i) for i in str_price]

#Cleaning disp
disp_dirty = disp_dirty.replace('\n', "")
disp_dirty = disp_dirty.replace('[', "")
disp_dirty = disp_dirty.replace(']', "")
disp_dirty = disp_dirty.split(",")
disp_dirty[0] = ' ' + disp_dirty[0]
is_disp = ' <p class="instock availability"><i class="icon-ok"></i>            In stock    </p>'
disp = [np.where(i == is_disp, 1 ,0 ) for i in disp_dirty]

#Cleaning rating
#test_trim = str_rating_dirty.strip(" ")
str_rating_dirty = str_rating_dirty('[', "")
str_rating_dirty = str_rating_dirty.replace(']', "")
str_rating_dirty = str_rating_dirty.replace(' ', "")
str_rating_dirty = str_rating_dirty.replace('\n', "")












