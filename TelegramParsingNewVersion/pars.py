from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
# from selenium.common.exceptions import NoSuchElementException
from fake_useragent import UserAgent
import datetime
from time import sleep
import locale
import sys
import os

def log_file(date, title):
    with open(r"C:\Users\EXCLUSIVE\Desktop\LogOutputAndError.txt", mode='a', encoding='utf-8') as file:
        file.write(date + ' ' + title + '\n')

def date_show():
    return datetime.datetime.now().strftime('%d %B %Y - %H:%M:%S')

def sleep_page():
    sleep(1)

def option_web_driver():
    option = webdriver.ChromeOptions()
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_argument("user-agent=" + "PARSING" + str(UserAgent().random)) #+ str(UserAgent().random))
    # option.add_argument("--headless")
    return option

def path_chrome_driver():
    Path = r"C:\Users\EXCLUSIVE\Desktop\repositoriy\Test\chromedriver.exe"
    return Path

def start_and_settings_chrome():
    Browser = webdriver.Chrome(service = Service(executable_path = path_chrome_driver()), options = option_web_driver())
    Browser.set_page_load_timeout(90)
    return Browser

def quit_browser(Browser):
    Browser.quit()

def check_browser_on_exit(Browser):
    try:
        Browser.find_element(By.TAG_NAME, 'h4')
    except:
        log_file(date=date_show(), title='Браузер закрыт\n')
        quit_browser(Browser)
        sys.exit()

def translate_on_russian_language(Browser):
    isflag =  True
    while isflag:
        sleep_page()
        log_file(date=date_show(), title='Переводим страницу на русский язык')
        Buttons = Browser.find_elements(By.CLASS_NAME, 'btn-primary.btn-secondary.btn-primary-transparent.primary.rp')
        for i in Buttons:
            if i.text == 'ПРОДОЛЖИТЬ НА РУССКОМ':
                i.click()
                isflag = False
                break
    else:
        log_file(date=date_show(), title='Страница переведена на русский язык')

def button_enter_telegram_account_Number(Browser):
    sleep_page()
    Number = Browser.find_element(By.CSS_SELECTOR, 'div.input-field.input-field-phone')
    Number = Number.find_element(By.CSS_SELECTOR, 'div.input-field-input')
    Number.click()
    log_file(date=date_show(), title='Входим по номеру телефона')
    sleep_page()
    while True:
        while 'number_phone.txt' not in os.listdir('.'):
            log_file(date=date_show(), title='Файл number_phone.txt еще не создан')
            sleep_page()
        with open(file='number_phone.txt', mode='r', encoding='utf-8') as file:
            log_file(date=date_show(), title='Читаем файл number_phone.txt')
            NumberPhone = file.read()
        if len(NumberPhone) != 10:
            log_file(date=date_show(), title=f'Содержит неверный номер телефона: +7-{NumberPhone}, длина: {len(NumberPhone)}, требуется длина: 10')
            os.remove('number_phone.txt')
        else:
            break
    os.remove('number_phone.txt')
    Number.send_keys(NumberPhone)
    log_file(date=date_show(), title=f'Вводим номер телефона +7-{NumberPhone}')
    sleep_page()
    Browser.find_element(By.CSS_SELECTOR, 'button.btn-primary.btn-color-primary.rp').click()
    return Browser

def put_code(Browser):
    while True:
        try:
            sleep_page()
            Code = Browser.find_element(By.CSS_SELECTOR, 'input[type=tel]')
            sleep_page()
            break
        except:
            log_file(date=date_show(), title='Поле для ввода кода не найденно')
    log_file(date=date_show(), title='Ожидаем поля ввода кода')
    Code.click()
    Code.clear()
    while True:
        while 'sms_code.txt' not in os.listdir('.'):
            log_file(date=date_show(), title='Файл sms_code.txt еще не создан')
            sleep_page()
        with open(file='sms_code.txt', mode='r', encoding='utf-8') as file:
            log_file(date=date_show(), title='Читаем файл sms_code.txt')
            sms_code = file.read()
            sleep_page()
            log_file(date=date_show(), title=f'Веденный код: {sms_code}, длина кода: {len(sms_code)}')
            Code.send_keys(sms_code)
        os.remove('sms_code.txt')
        if len(sms_code) != 5:
            log_file(date=date_show(), title='Введен неверный код')
            log_file(date=date_show(), title=f'Веденный код: {sms_code}, длина кода: {len(sms_code)} While 1')
        else:
            sleep_page()
            break
    # os.remove('sms_code.txt')
    while True:
        try:
            sleep_page()
            Browser.find_element(By.NAME, 'notsearch_password')
            break
        except:
            log_file(date=date_show(), title='Введен неверный код')
            Code.click()
            Code.clear()
            while True:
                while 'sms_code.txt' not in os.listdir('.'):
                    log_file(date=date_show(), title='Файл sms_code.txt еще не создан')
                    sleep_page()
                with open(file='sms_code.txt', mode='r', encoding='utf-8') as file:
                    log_file(date=date_show(), title='Читаем файл sms_code.txt')
                    sms_code = file.read()
                    sleep_page()
                    log_file(date=date_show(), title=f'Веденный код: {sms_code}, длина кода: {len(sms_code)}')
                    Code.send_keys(sms_code)
                os.remove('sms_code.txt')
                if len(sms_code) != 5:
                    log_file(date=date_show(), title=f'Введен неверный код {sms_code}, {len(sms_code)}')
                    log_file(date=date_show(), title=f'Веденный код: {sms_code}, длина кода: {len(sms_code)} While 2')
                else:
                    break
            # os.remove('sms_code.txt')
            sleep_page()
    return Browser

# def put_code(Browser):
#     try:
#         sleep_page()
#         Code = Browser.find_element(By.CSS_SELECTOR, 'input[type=tel]')
#         Code.click()
#         Code.clear()
#         print(date_show(), end=' ')
#         Code.send_keys(input('Введите код: '))
#         sleep_page()
#         Browser.find_element(By.NAME, 'notsearch_password')
#     except:
#         log_file(date=date_show(), title= 'Введен неверный код')
#         put_code(Browser)
#     return Browser

def act_enter_telegram_account(Browser):
    sleep_page()
    isflag = True
    while isflag:
        Buttons = Browser.find_elements(By.CLASS_NAME, 'btn-primary.btn-secondary.btn-primary-transparent.primary.rp')
        for i in Buttons:
            if i.text == 'ВХОД ПО НОМЕРУ ТЕЛЕФОНА':
                i.click()
                isflag = False
                break
    Browser = button_enter_telegram_account_Number(Browser)
    Browser = put_code(Browser)
    sleep_page()
    log_file(date=date_show(), title='Перешли на страницу ввода облачного пароля')
    Password = Browser.find_element(By.NAME, 'notsearch_password')
    Password.clear()
    
    # account_password = 'RepytwjdCD14031999'

    while True:
        while 'password.txt' not in os.listdir('.'):
            log_file(date=date_show(), title='Файл password.txt еще не создан')
            sleep_page()
        with open(file='password.txt', mode='r', encoding='utf-8') as file:
            log_file(date=date_show(), title='Читаем файл password.txt')
            file_content = file.read()
        os.remove('password.txt')
        break
    sleep_page()

    log_file(date=date_show(), title='Вводим пароль от облачного хранилища')
    Password.send_keys(file_content)
    sleep_page()
    isflag = True
    while isflag:
        Button = Browser.find_elements(By.CSS_SELECTOR, 'button.btn-primary.btn-color-primary.rp')
        for i in Button:
            if i.text == 'ДАЛЕЕ':
                    i.click()
                    isflag = False
                    break
            elif i.text == Button[len(Button) - 1]:
                log_file(date=date_show(), title='Кнопка не найдена')
    log_file(date=date_show(), title='Успешный вход в аккаунт')

def setting_for(li, Channel, Start=0, End=0):
    isflag = False
    for i in li[Start:End:]:
        log_file(date=date_show(), title=i.find_element(By.CSS_SELECTOR, 'span.peer-title').text)
        if i.find_element(By.CSS_SELECTOR, 'span.peer-title').text == Channel:
            log_file(date=date_show(), title='Чат найден')
            i.click()
            isflag = True
            break
    return isflag

def search_channel(Browser, Channel):
    sleep_page()
    ul = Browser.find_element(By.CSS_SELECTOR, 'ul.chatlist')
    li, k = 0, 0
    while li <= len(ul.find_elements(By.TAG_NAME, 'li')):
        k += 1
        if k == 1:
            isflag = setting_for(ul.find_elements(By.TAG_NAME, 'li'), Channel, End=6)
        elif k == 2:
            isflag = setting_for(ul.find_elements(By.TAG_NAME, 'li'), Channel, End=len(ul.find_elements(By.TAG_NAME, 'li')))
        else:
            isflag = setting_for(ul.find_elements(By.TAG_NAME, 'li'), Channel, 20, len(ul.find_elements(By.TAG_NAME, 'li')))
        if isflag:
            break
        li = len(ul.find_elements(By.TAG_NAME, 'li'))
        ActionChains(Browser).scroll(0, 0, 0, 2500, origin=ul).perform()
        sleep(3)
    else:
        log_file(date=date_show(), title='Запрашиваемый чат не найден')

def current_date(end_date):
    locale.setlocale(locale.LC_ALL, "")  
    if datetime.datetime.now().strftime('%d.%B.%Y') == end_date:
        end_date = 'Сегодня'
    return end_date

def search_date_post(start_date='20.03.2022', end_date='01.05.2022'):
    end_date = current_date(end_date)
    

class Main:
    locale.setlocale(locale.LC_ALL, "")  
    Browser = start_and_settings_chrome()
    Browser.set_window_size(1024, 768)
    Browser.get(url = "https://web.telegram.org/k/")
    translate_on_russian_language(Browser)
    act_enter_telegram_account(Browser)
    while 'name_channel.txt' not in os.listdir('.'):
        log_file(date=date_show(), title='Файл name_channel.txt еще не создан')
        sleep_page()
    with open(file='name_channel.txt', mode='r', encoding='utf-8') as file:
        Channel = file.read()
    os.remove('name_channel.txt')
    search_channel(Browser, Channel)
    log_file(date=date_show(), title='Пока что всё!')
    sleep(30)
    quit_browser(Browser)