from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from fake_useragent import UserAgent
#from datetime import date
import datetime
from time import sleep
import locale
import sys

def SleepPage():
    sleep(1)

def DisableWebDriver():
    option = webdriver.ChromeOptions()
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_argument("user-agent=" + str(UserAgent().random))
    option.add_argument("--headless")
    return option

def PathChromeDrivers():
    Path = "chromedriver.exe"
    return Path

def StartAndSettingsChrome():
    Browser = webdriver.Chrome(service = Service(executable_path = PathChromeDrivers()), options = DisableWebDriver())
    Browser.set_page_load_timeout(90)
    return Browser

def QuitBrowser(Browser):
    Browser.quit()

def CheckAuthorization(Browser):
    try:
        Browser.find_element(By.TAG_NAME, 'h4')
    except:
        print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Браузер закрыт')
        QuitBrowser(Browser)
        sys.exit()

def RussianLanguage(Browser):
    try:
        isflag = True
        while isflag:
            SleepPage()
            print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Переводим страницу на русский язык')
            Buttons = Browser.find_elements(By.CLASS_NAME, 'btn-primary.btn-secondary.btn-primary-transparent.primary.rp')
            for i in Buttons:
                if i.text == 'ПРОДОЛЖИТЬ НА РУССКОМ':
                    i.click()
                    isflag = False
                    break
    except:
        CheckAuthorization(Browser)
        print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Кнопка не прогрузилась, ожидаем')
        RussianLanguage(Browser)

def EnterButtonTelegramAccountNumber(Browser):
    SleepPage()
    Number = Browser.find_element(By.CSS_SELECTOR, 'div.input-field.input-field-phone')
    Number = Number.find_element(By.CSS_SELECTOR, 'div.input-field-input')
    #for i in Number:
    #    print(i.text)
    Number.click()
    print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Вводим номер телефона')
    SleepPage()
    Number.send_keys('9779943527')
    SleepPage()
    Browser.find_element(By.CSS_SELECTOR, 'button.btn-primary.btn-color-primary.rp').click()
    return Browser

def PutCode(Browser):
    try:
        SleepPage()
        Code = Browser.find_element(By.CSS_SELECTOR, 'input[type=tel]')
        Code.click()
        Code.clear()
        print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), end=' ')
        Code.send_keys(input('Введите код: '))
        SleepPage()
        Browser.find_element(By.NAME, 'notsearch_password')
    except:
        print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Введен неверный код')
        PutCode(Browser)
    return Browser

def EnterTelegramAccountNumber(Browser):
    try:
        SleepPage()
        isflag = True
        while isflag:
            Buttons = Browser.find_elements(By.CLASS_NAME, 'btn-primary.btn-secondary.btn-primary-transparent.primary.rp')
            for i in Buttons:
                if i.text == 'ВХОД ПО НОМЕРУ ТЕЛЕФОНА':
                    i.click()
                    isflag = False
                    break
        Browser = EnterButtonTelegramAccountNumber(Browser)
        Browser = PutCode(Browser)
        SleepPage()
        print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Вводим пароль от облачного хранилища')
        Password = Browser.find_element(By.NAME, 'notsearch_password')
        Password.clear()
        Password.send_keys('RepytwjdCD14031999')
        SleepPage()
        Button = Browser.find_elements(By.CSS_SELECTOR, 'button.btn-primary.btn-color-primary.rp')
        for i in Button:
            if i.text == 'ДАЛЕЕ':
                    i.click()
                    break
    except:
        CheckAuthorization(Browser)
        print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Error in Code')

def EnterTelegramAccount(Browser):
    try:
        SleepPage()
        Password = Browser.find_element(By.NAME, 'notsearch_password')
        Password.clear()
        Password.send_keys('RepytwjdCD14031999')
        SleepPage()
        Browser.find_element(By.CLASS_NAME, 'btn-primary.btn-color-primary.rp').click()
    except:
        CheckAuthorization(Browser)
        print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Ждем авторизации по QR-code')
        EnterTelegramAccount(Browser)

def SettingsFor(li, Channel, Start=0, End=0):
    isflag = False
    for i in li[Start:End:]:
        print(i.find_element(By.CSS_SELECTOR, 'span.peer-title').text)
        if i.find_element(By.CSS_SELECTOR, 'span.peer-title').text == Channel:
            print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Чат найден')
            i.click()
            isflag = True
            break
    return isflag

def SearchCannel(Browser, Channel):
    SleepPage()
    ul = Browser.find_element(By.CSS_SELECTOR, 'ul.chatlist')
    li, k = 0, 0
    while li <= len(ul.find_elements(By.TAG_NAME, 'li')):
        k += 1
        if k == 1:
            isflag = SettingsFor(ul.find_elements(By.TAG_NAME, 'li'), Channel, End=6)
        elif k == 2:
            isflag = SettingsFor(ul.find_elements(By.TAG_NAME, 'li'), Channel, End=len(ul.find_elements(By.TAG_NAME, 'li')))
        else:
            isflag = SettingsFor(ul.find_elements(By.TAG_NAME, 'li'), Channel, 20, len(ul.find_elements(By.TAG_NAME, 'li')))
        if isflag:
            break
        li = len(ul.find_elements(By.TAG_NAME, 'li'))
        ActionChains(Browser).scroll(0, 0, 0, 2500, origin=ul).perform()
        sleep(3)
    else:
        print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Запрашиваемый чат не найден')

'''def SearchCannel(Browser, Channel):
    SleepPage()
    ul = Browser.find_element(By.CSS_SELECTOR, 'ul.chatlist')
    li, FirstProxod = [1], True
    print(li[len(li) - 1])
    print(ul.find_elements(By.TAG_NAME, 'li')[len(ul.find_elements(By.TAG_NAME, 'li')) - 1])
    while li[len(li) - 1] != ul.find_elements(By.TAG_NAME, 'li')[len(ul.find_elements(By.TAG_NAME, 'li')) - 1]:
        li = ul.find_elements(By.TAG_NAME, 'li')
        if FirstProxod:
            isflag = SettingsFor(li, Channel)
        else:
            isflag = SettingsFor(li, Channel, 19)
        if isflag:
            break
        ActionChains(Browser).scroll(0, 0, 0, 2500, origin=ul).perform()
        sleep(1)
    else:
        print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Запрашиваемый чат не найден')'''

def CurrentDate(end_date):
    locale.setlocale(locale.LC_ALL, "")  
    if datetime.datetime.now().strftime('%d.%B.%Y') == end_date:
        end_date = 'Сегодня'
    return end_date

def SearchDatePost(start_date='20.03.2022', end_date='01.05.2022'):
    end_date = CurrentDate(end_date)
    

class Main:
    locale.setlocale(locale.LC_ALL, "")  
    Browser = StartAndSettingsChrome()
    Browser.set_window_size(1024, 768)
    Browser.get(url = "https://web.telegram.org/k/")
    RussianLanguage(Browser)
    EnterTelegramAccountNumber(Browser)
    #EnterTelegramAccount(Browser)
    Channel = 'XGTV'
    SearchCannel(Browser, Channel)
    #SearchDatePost()
    print(datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S'), 'Пока что всё!')
    sleep(30)
    QuitBrowser(Browser)