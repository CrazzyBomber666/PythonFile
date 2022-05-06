from selenium import webdriver
import pyperclip

option = webdriver.ChromeOptions()
option.add_argument("--disable-blink-features=AutomationControlled")
option.add_argument("--headless")
option.add_argument("user-agent=" + str("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.0.1044 Yowser/2.5 Safari/537.36"))
Browser = webdriver.Chrome(executable_path = r"C:\Users\EXCLUSIVE\Desktop\repositoriy\Test\chromedriver.exe", options = option)
URL = "https://www.youtube.com/live_chat?is_popout=1&v=oHnq3CpGxJU"
Browser.get(url = URL)
temp = Browser.find_element_by_xpath('//div[@id="items"]')
temp = temp.find_elements_by_xpath('//*[@id="message"]')
for i in range(0, len(temp)):
    if len(temp[i].text.replace("*", "")) == 17:
        print(temp[i].text.replace("*", ""))
        pyperclip.copy(temp[i].text.replace("*", ""))
lengthTemp = int(len(temp))
temp.clear()
while True:
    temp_1 = Browser.find_element_by_xpath('//div[@id="items"]')
    temp_1 = temp_1.find_elements_by_xpath('.//*[@id="message"]')
    lengthTemp_1 = int(len(temp_1))
    if lengthTemp < lengthTemp_1:
        count = lengthTemp_1 - (lengthTemp_1 - lengthTemp)
        for i in range(count, lengthTemp_1):
            if len(temp_1[i].text.replace("*", "")) == 17: #ABCDE-FGHIK-LMNOP 15 букв и 2 дефиса
                print(temp_1[i].text.replace("*", ""))
                pyperclip.copy(temp[i].text.replace("*", ""))
        lengthTemp = lengthTemp_1