# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 11:35:54 2021

@author: Blaise

Selenium
"""

import csv
import configparser
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome



driver = Chrome()


#options = ChromeOptions()
#options.use_chromium = True
#driver = Chrome(options = options)

config = configparser.RawConfigParser()
config.read(filenames = 'selpass.txt')

driver.get('https://twitter.com/login')
username = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
username.send_keys('zzeubb@gmail.com')
#username.send_keys(config.get('selpass', 'username'))

my_password = getpass()
password = driver.find_element_by_xpath('\\input[@name="session[password]"]')
password.send_keys('Twitter71!')
password.send_keys(Keys.RETURN)





