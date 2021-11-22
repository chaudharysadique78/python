from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time 
import random
import threading
import xlrd
import os
import xlwt
from datetime import datetime
from datetime import timedelta
from xlutils.copy   import copy

Search_item = input('Kindly enter search item : ')
browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
browser.implicitly_wait(6)
browser.get('https://www.google.com/')
browser.maximize_window()
a=browser.find_element_by_name('q')
a.send_keys(Search_item,Keys.ENTER)
browser.find-element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3').send_keys(Keys.ENTER)



