# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 10:35:01 2021

@author: Utilisateur
"""
import bs4
from bs4 import BeautifulSoup
import urllib.request
import csv
import requests
import re



#specify the url
urlpage= "https://books.toscrape.com/"
#request the url
req = requests.get(urlpage)
#parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(req.text, 'html.parser')

'''
#query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)


print(soup)

#find result within title
title = soup.find('title', attrs={'class': 'title' })
results = title.find_all('title')
print(results)
'''
#soup= BeautifulSoup(req.text, "lxml")

'''
#Find all h3
for title in soup.find_all('h3'):
    print(title)
'''
'''
#find all the price of the page
price = soup.find_all("p",{"class" : "price_color"} )
str_price_dirty = str(price)

#find all rating
rating = soup.find_all("p", {"class": "star-rating"})
str_rating_dirty= str(rating)

#Find disponibility
disp = soup.find_all("p", {"class" : "instock"})
str_disp_dirty = str(disp)

#find title
title = soup.find_all("img",{"class": "thumbnail"} )
str_title_dirty= str(title)

#cleanning price
str_price_dirty = str_price_dirty.replace('<p class="price_color">Â£', "")
str_price_dirty = str_price_dirty.replace('</p>', "")
str_price_dirty = str_price_dirty.replace(' ', "")
str_price_dirty = str_price_dirty.replace('[', "")
str_price_dirty = str_price_dirty.replace(']', "")
str_price = str_price_dirty.split(",")


#string to float price
price = [float(i) for i in str_price]
'''

'''
#find disponibility
disponibility = soup.find_all("p", {"class" : "instock"})
dispo = disponibility[0]
print(disponibility[0].text.replace("\n", ""))


list_disponibility = []
for i in range(20):
    list_disponibility.append(disponibility[i].text.replace("\n", ""))

print(list_disponibility)

'''

'''
#find price
pr = soup.find_all("p", {"class" : "price_color"})
p = pr[0]
print(pr[0].contents)
list_price = []
for i in range(20):
    list_price.append(pr[i].contents)
    
print(list_price)

'''

'''
#find rating
rating = soup.find_all("p", {"class" : "star-rating"})
print(rating[0]['class'][1])

list_rating = []
for i in range (20):
    list_rating.append(rating[i]['class'][1])

print(list_rating)


'''


'''
#find title
h3 = soup.find_all('h3')
h = h3[0]
print(h)
print(h.a['title'])
print(h3[0].a['title'])
list_title = []
for i in range (20):
    list_title.append(h3[i].a['title'])
    
print(list_title)
'''

#find picture
picture = soup.find_all("img", {"class" : "thumbnail"})
print(picture[0]['src'])

list_picture = []
for i in range(20):
    list_picture.append(picture[i]['src'])

print(list_picture)


