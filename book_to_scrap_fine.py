# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
#import urllib.request
import csv
import pandas as pd
import sqlite3
import timeit

start_time = timeit.default_timer()

# specify the url
urlpage = "https://books.toscrape.com/"
# request the url
req = requests.get(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(req.text, 'html.parser')

list_pages = ['https://books.toscrape.com/catalogue/page-' + str(i)
              + '.html' for i in range(51)]
del list_pages[0]
list_pages[0] = "https://books.toscrape.com/"

list_price, list_rating, list_disponibility, = [], [], []
list_title, list_picture = [],[]

for i in list_pages:
    # def scrap_datas(i)
    urlpage = i
    # request the url
    req = requests.get(urlpage)
    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(req.text, 'html.parser')

    
    disponibility = soup.find_all("p", {"class" : "instock"})
    for i in range(20):
        list_disponibility.append(disponibility[i].text.replace("\n", ""))

    # find rating
    rating = soup.find_all("p", {"class" : "star-rating"})
    for i in range (20):
        list_rating.append(rating[i]['class'][1])
    
    # find title
    h3 = soup.find_all('h3')
    for i in range (20):
        list_title.append(h3[i].a['title'])

    # find  price 
    price = soup.find_all("p", {"class": "price_color"})
    for i in range(20):
        list_price.append(price[i].text)

    #find picture
    picture = soup.find_all("img", {"class" : "thumbnail"})
    for i in range(20):
        list_picture.append("https://books.toscrape.com/"+ picture[i]['src'])

elapsed_scraping = timeit.default_timer() - start_time

# Transforming One Two Three to 1 2 3
for i in range(len(list_rating)):
    if list_rating[i] == 'One':
        list_rating[i]=1
    elif list_rating[i] == 'Two':
        list_rating[i]=2
    elif list_rating[i] == 'Three':
        list_rating[i]=3
    elif list_rating[i] == 'Four':
        list_rating[i]=4
    elif list_rating[i] == 'Five':
        list_rating[i]=5

# Transforming In stock or Not in stock to 1 ,0
for i in range(len(list_disponibility)):
    if list_disponibility[i] == '            In stock    ':
        list_disponibility[i]=1
    else :
            list_disponibility[i]=0
            
for i in range(len(list_price)):
    list_price[i] = list_price[i].replace('Â£', "")
    
elapsed_cleaning = timeit.default_timer() - elapsed_scraping

#create database
conn = sqlite3.connect('detective.db')
#get a cursor object 
c = conn.cursor()
#create table
c.execute('''CREATE TABLE IF NOT EXISTS books
          ([Book_title] text, [Book_price] float, [Book_rating] integer,
           [Book_disponibility] integer,[Url_picture] text)''')
conn.commit() 

for i in range(len(list_price)):
    data_tuple = (list_title[i],list_price[i], list_rating[i], list_disponibility[i], list_picture[i])

    sqlite_insert_query = """INSERT INTO books
                              (Book_title, Book_price, Book_rating, Book_disponibility, Url_picture) 
                              VALUES (?, ?, ?, ?, ?);"""

    c.execute(sqlite_insert_query, data_tuple)
    conn.commit()

conn.close()

elapsed_write_database = timeit.default_timer() - elapsed_cleaning

df_book_to_scrap = pd.DataFrame(list(zip(list_title, list_price, list_rating, list_disponibility)),
                                columns =['Book_title', 'Book_price', 'Book_rating', 'Book_disponibility' ])
#convert in CSV
df_book_to_scrap.to_csv(r'book_to_scrap.csv', index=False)

elapsed_all_prog = timeit.default_timer() - start_time


print('elapsed_scraping',elapsed_scraping,
      '/n elapsed_cleaning',elapsed_cleaning,
      '/n elapsed_write_database',elapsed_write_database,
      '/n elapsed_all_program =',elapsed_all_prog)
