from selenium import webdriver
from bs4 import BeautifulSoup as BS

Browser = webdriver.Chrome(executable_path = r"C:\Users\EXCLUSIVE\Desktop\repositoriy\Test\chromedriver.exe")
Browser.get(url='https://web.telegram.org/')
a = input()
Browser.quit()