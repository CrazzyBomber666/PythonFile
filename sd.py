from selenium import webdriver
from bs4 import BeautifulSoup as BS

"""Browser = webdriver.Chrome(executable_path = r"C:\Users\EXCLUSIVE\Desktop\repositoriy\Test\chromedriver.exe")

Browser.get(url = 'https://elibrary.ru/')

Browser.find_element_by_xpath('//*[@id="win_goto"]/table[1]/tbody/tr[8]/td[2]/a').click()

Html = BS(Browser.page_source, "lxml")

temp = Html.find('table', {'width': '100%', 'cellspacing': '1', 'cellpadding': '3', 'id': 'restab'})
temp = temp.find_all('tr', {'align': 'center', 'valign': 'top'})

for i in temp:
    Tematika = i.find('td', {'align': 'left'})
    Tematika = Tematika.find('b').text.replace('\n', '')
    print(Tematika)"""
Browser = webdriver.Chrome(executable_path = r"C:\Users\EXCLUSIVE\Desktop\repositoriy\Test\chromedriver.exe")
Browser.get(url='https://web.telegram.org/')
a = input()
Browser.quit()