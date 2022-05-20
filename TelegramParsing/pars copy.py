
from types import NoneType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from fake_useragent import UserAgent
import datetime
from time import sleep
import locale
import sys

def page_sleep():
    sleep(2)

def DisableWebDriver():
    option = webdriver.ChromeOptions()
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_argument("user-agent=" + str(UserAgent().random))
    option.add_argument("--headless")
    return option

def path():
    return r"C:\Users\EXCLUSIVE\Desktop\python файлы\TelegramParsing\chromedriver.exe"

def StartAndSettingsChrome():
    Browser = webdriver.Chrome(service = Service(executable_path = path()), options = DisableWebDriver())
    Browser.set_page_load_timeout(90)
    Browser.set_window_size(1024, 768)
    Browser.get(url = "https://web.telegram.org/k/")
    return Browser

def RussianLanguage(Browser):
    while Browser.find_elements(By.CLASS_NAME, 'btn-primary.btn-secondary.btn-primary-transparent.primary.rp') != NoneType and Browser.find_elements(By.CLASS_NAME, 'btn-primary.btn-secondary.btn-primary-transparent.primary.rp') == []:
        page_sleep()
        print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Переводим страницу на русский язык')
    else:
        page_sleep()
        for i in Browser.find_elements(By.CLASS_NAME, 'btn-primary.btn-secondary.btn-primary-transparent.primary.rp'):
            if i.text == 'ПРОДОЛЖИТЬ НА РУССКОМ':
                print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Страница переведена на русский язык')
                i.click()
                break
    a = input()
    print(a)
    Browser.quit()

class main:
    Browser = StartAndSettingsChrome()
    RussianLanguage(Browser)