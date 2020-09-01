import selenium
from selenium import webdriver

browser = webdriver.Chrome('./driver/chromedriver.exe')
browser.get('https://www.google.com')
