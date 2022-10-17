import sys, yaml
from pathlib import Path
sys.path.insert(0, str(Path.home()) + '/git/url_watcher/library')
import url

inputFile = str(Path.home()) + '/git/url_watcher/sites.yaml'
myClass = url.getURL('')

#myClass.lookup()

#print(myClass.myData)



# import libraries
#import urllib.request
#from bs4 import BeautifulSoup
#from selenium import webdriver
#import time
#import pandas as pd# specify the url
#urlpage = 'https://groceries.asda.com/search/yogurt'
#print(urlpage)
# run firefox webdriver from executable path of your choice
#driver = webdriver.Firefox(executable_path = 'your/directory/of/choice')

with open(inputFile, "r") as stream:
    try:
        my_yaml = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

for i in my_yaml['sites']:
    myClass.url = i
    myClass.lookup()
    print(myClass.myData)
