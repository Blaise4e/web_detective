# -*- coding: utf-8 -*-
from msedge.selenium_tools import Edge, EdgeOptions
options = EdgeOptions()
options.use_chromium = True
driver  = Edge(options = options)

driver.get('https://books.toscrape.com/')
want_some = driver.find_element_by_xpath(
    '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]/article/div[2]/p[1]')
print(want_some.text)
want_some2 = driver.find_element_by_xpath(
    '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[2]/article/div[2]/p[1]')
print(want_some2.text)
list_price = []
list_xpath = []
xpath1 = '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li['
xpath2 = ']/article/div[2]/p[1]'

# Get the Xpaths of all the prices for one page:
for i in range (20):
    xpath = xpath1 + str(i+1) + xpath2
    list_xpath.append(xpath)
    

# Get the URL of the 50 pages: 
list_pages = ['https://books.toscrape.com/catalogue/page-' + str(i)
              + '.html' for i in range(51)]
del list_pages[0]
list_pages[0] = "https://books.toscrape.com/"

for url in list_pages:
    # def scrap_datas(i)
    urlpage = url
    # request the url
    driver.get(urlpage)

    for xpath in list_xpath:
        temp_price = driver.find_element_by_xpath(xpath).text
        list_price.append(temp_price)

driver.quit()

"""
list_price, list_rating, list_disponibility, = [], [], []
list_title, list_picture = [],[]
"""
