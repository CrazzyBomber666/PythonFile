from selenium import webdriver
from bs4 import BeautifulSoup as BS
import sqlite3 as SQL
import time
import random
from datetime import datetime
from fake_useragent import UserAgent
import os

def FirstConnectionInSQL():
    try:
        connectionSQL = SQL.connect("AuthorAndStatie.db")
        cursors = connectionSQL.cursor()
        #cursors.execute("DROP TABLE IF EXISTS Author")
        #cursors.execute("DROP TABLE IF EXISTS Statie")
        #cursors.execute("DROP TABLE IF EXISTS AuthorAndStatie")
        cursors.execute("""CREATE TABLE IF NOT EXISTS Author (
        AuthorID INTEGER PRIMARY KEY AUTOINCREMENT,
        FamiliaAuthor TEXT, 
        NameAuthor TEXT, 
        OtchestvoAuthor TEXT
        )""")
        cursors.execute("""CREATE TABLE IF NOT EXISTS AuthorAndStatie (
        StatieID INTEGER PRIMARY KEY AUTOINCREMENT,
        AuthorID INTEGER,
        NameStatie TEXT, 
        YearStatie INTEGER
        )""")
        connectionSQL.commit()
    except SQL.Error as e:
        if connectionSQL: connectionSQL.rollback()
        print("Ошибочка в выполнении создании таблиц")
    finally:
        if connectionSQL: connectionSQL.close()
    pass

def NewStatie(Author, name, year):
    try:
        connectionSQL = SQL.connect("AuthorAndStatie.db")
        cursors = connectionSQL.cursor()
        cursors.execute("INSERT INTO AuthorAndStatie (AuthorID, NameStatie, YearStatie) VALUES(?, ?, ?)", (Author, name, year))
        connectionSQL.commit()
    except SQL.Error as e:
        if connectionSQL: connectionSQL.rollback()
        print("Ошибочка в выполнении добавлении автора и статьи в таблицу")
    finally:
        if connectionSQL: connectionSQL.close()
    pass

def CheckStatie(name):
    try:
        connectionSQL = SQL.connect("AuthorAndStatie.db")
        cursors = connectionSQL.cursor()
        cursors.execute("SELECT NameStatie from AuthorAndStatie WHERE NameStatie = ?", (name,))
        result = cursors.fetchone()
        return result
    except SQL.Error as e:
        if connectionSQL: connectionSQL.rollback()
        print("Ошибочка в выполнении поиска статьи в таблице")
    finally:
        if connectionSQL: connectionSQL.close()
    pass

def SleepPage():
    time.sleep(5)
    pass

def StartChrome(option):
    Browser = webdriver.Chrome(executable_path = r"C:\Users\EXCLUSIVE\Desktop\repositoriy\Test\chromedriver.exe", options = option)
    Browser.set_page_load_timeout(30)
    return Browser

def DisableWebDriver():
    option = webdriver.ChromeOptions()
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_argument("user-agent=" + str(UserAgent().random))
    #option.add_argument("--proxy-server=142.93.167.225:3128")
    #option.add_argument("--headless")
    #Можно и верхним способом скрыть открытия браузера, а можно и нижнем, чтобы не нагружать ЦП (для вузов самое то)
    #option.headless = True
    return option

def EnterElibrary(Browser):
    try:
        URL = "https://www.elibrary.ru/defaultx.asp"#"https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"#"https://www.elibrary.ru/defaultx.asp"
        Browser.get(url = URL)
    except:
        print("Открываю занова сайт елибрири")
        EnterElibrary(Browser)
    SleepPage()
    pass

def EnterAccountElibrary(Browser):
    LoginPole = Browser.find_element_by_id("login")
    LoginPole.clear()
    LoginPole.send_keys("Serega22841")
    PasswordPole = Browser.find_element_by_id("password")
    PasswordPole.clear()
    PasswordPole.send_keys("Serega22848")
    Browser.find_element_by_class_name("butred").click()
    SleepPage()
    pass

def ExitAccountElibrary(Browser):
    #занова написать
    pass

def ExitCrome(Browser):
    Browser.delete_all_cookies()
    Browser.quit()
    #os.system("taskkill /f /im chromedriver.exe /T")
    SleepPage()
    pass

def FindSPINAuthor(Browser, SPIN):
    FindPole = Browser.find_element_by_id("ftext")
    FindPole.clear()
    FindPole.send_keys(SPIN)
    Browser.find_element_by_class_name("butblue").click()
    SleepPage()
    pass

def ReturnHtmlCode(Browser):
    Html = BS(Browser.page_source, "lxml")
    return Html

def FindPageNum(Html):
    pagenumEnd = Html.find("tr", {"align": "center", "valign": "middle", "class": "menurb"}).find_all("td", {"nowrap": "", "width": "15%"})
    if len(pagenumEnd) != 0:
        SaveLastStrokaPageNum = []
        for i in pagenumEnd:
            SaveLastStrokaPageNum.append(i.find("a").get("href"))
            #Len_Stroka = len(SaveLastStrokaPageNum[-1])
            indexStart = SaveLastStrokaPageNum[-1].find("(") + 1
            indexEnd = SaveLastStrokaPageNum[-1].find(")")
            SaveLastPageNum = ""
        while indexEnd - indexStart > 0:
            SaveLastPageNum += SaveLastStrokaPageNum[-1][indexStart]
            indexStart += 1
        SleepPage()
        return SaveLastPageNum
    else:
        SleepPage()
        return 0

def NextPage(Browser, Html, NumberPage):
    try:
        temp = Browser.find_elements_by_class_name("mouse-hovergr")
        for i in temp:
            if i.text == str(NumberPage):
                temp[temp.index(i)].click()
                break
            print("Ошибочка", i, "\n\n", str(NumberPage))
            SleepPage()
            Html = ReturnHtmlCode(Browser)
    except:
        print("Открываю занова страницу с поиском")
        Html = NextPage(Browser, Html, NumberPage)
    finally:
        return Html

def NextLinkForYear(Browser, UrlPage):
    try:
        Browser.get(url = "https://elibrary.ru" + UrlPage)
        SleepPage()
        Html = ReturnHtmlCode(Browser)
        Browser.back()
        SleepPage()
    except:
        print("Открываю занова статью")
        Html = NextLinkForYear(Browser, UrlPage)
    finally:
        return Html

def Parsing(Html, Browser, Author, SPIN, pageNum):
    global k, summa
    kolvo, AFK = 0, 0
    Html = Html.find("table", {"id": "restab"}).find_all("td", {"align": "left", "valign": "top"})
    for i in Html:
        try:
            if None != i.find("table", {"width": "100%", "border": "0", "cellspacing": "0", "cellpadding": "0"}):
                i.select_one("table:nth-of-type(1)").decompose()
        except:
            pass
    random.shuffle(Html)
    #randomStatiePause = random.randint(k + 1, k + 4 + 1)
    for i in Html:
        if i.text != "":
            if None != i.find("a").find("span"):
                result = CheckStatie(i.find("span").text.replace("\n", "").replace("  ", " ").replace("\r", ""))
                if result != "":
                    Html = NextLinkForYear(Browser, i.find("a").get("href"))
                    Html = Html.find("table", {"width": "580", "cellspacing": "0", "cellpadding": "2", "border": "0"}).find_all("font")
                    k += 1
                    for j in Html:
                        if j.text.isdigit() and len(j.text) == 4:
                            print(k, i.find("span").text.replace("\n", "").replace("  ", " ").replace("\r", ""), end = " ")
                            print(j.text)
                            NewStatie(Author, i.find("span").text.replace("\n", "").replace("  ", " ").replace("\r", ""), j.text)
                            break
                    if k % 30 == 0:
                        #EnterElibrary(Browser)
                        #ExitAccountElibrary(Browser)
                        ExitCrome(Browser)
                        AFK = random.uniform(10800, 10860)
                        summa += AFK
                        print("Перерыв между открытием следующей статьи:", AFK)
                        print("--- Общее время AFK:", summa,"---\n")
                        DateTime()
                        time.sleep(AFK)
                        Option = DisableWebDriver()
                        Browser = StartChrome(Option)
                        EnterElibrary(Browser)
                        #EnterAccountElibrary(Browser)
                        user_agent = Browser.execute_script("return navigator.userAgent;")
                        print(user_agent)
                        FindSPINAuthor(Browser, SPIN)
                        Html = NextPage(Browser, Html, pageNum)
                    else:
                        AFK = timesleep()
                        summa += AFK
                        print("Перерыв между открытием следующей статьи:", AFK)
                        print("--- Общее время AFK:", summa,"---\n")
                        time.sleep(AFK)
            #if randomStatiePause == k:
            #   randomStatiePause = random.randint(k + 1, k + 4 + 1)
            #  AFK = random.uniform(10, 20)
            # summa += AFK
                #print("Дополнительный перерыв между открытием следующей статьи:", AFK)
                #print("--- Общее время AFK:", summa,"---\n")
                #time.sleep(AFK)
            else:
                if not i.find("font").text.replace("\n", "").replace("\r", "").replace("  ", " ") == "":
                    result = CheckStatie(i.find("font").text.replace("\n", "").replace("\r", "").replace("  ", " "))
                    if result != "":
                        k += 1
                        name = i.find("font").text.replace("\n", "").replace("\r", "").replace("  ", " ")
                        print(k, i.find("font").text.replace("\n", "").replace("\r", "").replace("  ", " "), end = " ")
                        i.select_one("font:nth-of-type(1)").decompose()
                        i.select_one("font:nth-of-type(1)").decompose()
                        temp = i.find("font").text
                        year = ""
                        for j in temp:
                            if j.isdigit() or j == "." or j == "-" or j == ")":
                                year += j
                                if year.find(")") != -1:
                                    year = ""
                                if year[0] == ".":
                                    year = ""
                                else:
                                    if len(year) == 5:
                                        if year.isdigit():
                                            kolvo += 1
                                        if year[-1] == ".":
                                            TableYear = year[:4]
                                            year = ""
                                            print(TableYear)
                                            NewStatie(Author, name, TableYear)
                                            break
                                        elif year.find("-") != -1:
                                            kolvo += 1
                                        elif year.find(".") != -1:
                                            pass
                                    if len(year) == 10:
                                        TableYear = year[6:]
                                        year = ""
                                        print(TableYear)
                                        NewStatie(Author, name, TableYear)
                                        break
                            else:
                                year = ""
                            if kolvo != 0:
                                year, kolvo = "", 0
                        if k % 30 == 0:
                            #EnterElibrary(Browser)
                            #ExitAccountElibrary(Browser)
                            ExitCrome(Browser)
                            AFK = random.uniform(10800, 10860)#AFK = random.uniform(21600, 21660)
                            summa += AFK
                            print("Перерыв между открытием следующей статьи:", AFK)
                            print("--- Общее время AFK:", summa,"---\n")
                            DateTime()
                            time.sleep(AFK)
                            Option = DisableWebDriver()
                            Browser = StartChrome(Option)
                            EnterElibrary(Browser)
                            #EnterAccountElibrary(Browser)
                            user_agent = Browser.execute_script("return navigator.userAgent;")
                            print(user_agent)
                            FindSPINAuthor(Browser, SPIN)
                            Html = NextPage(Browser, Html, pageNum)
        #if k % 5 == 0:
            #break
                    #if randomStatiePause == k:
                    #   randomStatiePause = random.randint(k + 1, k + 4 + 1)
                    #  AFK = random.uniform(10, 20)
                    # summa += AFK
                        #print("Дополнительный перерыв между открытием следующей статьи:", AFK)
                        #print("--- Общее время AFK:", summa,"---\n")
                        #time.sleep(AFK)
    return Browser

def timesleep():
	AFK = 0#random.uniform(60, 90)
	return AFK

def DateTime():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print(current_time, "\n")
	pass

def main():
    try:
        global summa, k, AFK
        summa, k, AFK = 0, 0, 0
        FirstConnectionInSQL()
        Options = DisableWebDriver()
        Browser = StartChrome(Options)
        SleepPage()
        while True:
            Author = "Новицкий В О"
            SPIN = "7890-5920"
            pagenum = 1
            EnterElibrary(Browser)
            user_agent = Browser.execute_script("return navigator.userAgent;")
            print(user_agent)
            #EnterAccountElibrary(Browser)
            FindSPINAuthor(Browser, SPIN)
            Html = ReturnHtmlCode(Browser)
            EndPage = FindPageNum(Html)
            DateTime()
            print(Author)
            print("Всего страниц:", EndPage, end = " Сейчас открыта: ")
            print(pagenum)
            pagenum1 = list(range(2, int(EndPage) + 1))
            random.shuffle(pagenum1)
            AFK = random.uniform(5, 10)
            summa += AFK
            print("\nПерерыв между началом парсинга:", AFK)
            print("--- Общее время AFK:", summa,"---\n")
            time.sleep(AFK)
            Browser = Parsing(Html, Browser, Author, SPIN, pagenum)
            for i in pagenum1:
                print(i)
                Html = NextPage(Browser, Html, i)
                print("переход выполнен")
                AFK = random.uniform(5, 10)
                summa += AFK
                print("\nПерерыв между открытием следующей страницы:", AFK)
                print("--- Общее время AFK:", summa,"---\n")
                time.sleep(AFK)
                Browser = Parsing(Html, Browser, Author, SPIN, i)
            
            Author = "Белова Ю Н"
            SPIN = "7618-5047"
            pagenum = 1
            EnterElibrary(Browser)
            FindSPINAuthor(Browser, SPIN)
            Html = ReturnHtmlCode(Browser)
            EndPage = FindPageNum(Html)
            print(Author)
            print("Всего страниц:", EndPage, end = " Сейчас открыта: ")
            print(pagenum)
            pagenum1 = list(range(2, int(EndPage) + 1))
            random.shuffle(pagenum1)
            AFK = random.uniform(5, 10)
            summa += AFK
            print("\nПерерыв между началом парсинга:", AFK)
            print("--- Общее время AFK:", summa,"---\n")
            time.sleep(AFK)
            Browser = Parsing(Html, Browser, Author, SPIN, pagenum)
            for i in pagenum1:
                print(i)
                Html = NextPage(Browser, Html, i)
                print("переход выполнен")
                AFK = random.uniform(5, 10)
                summa += AFK
                print("\nПерерыв между открытием следующей страницы:", AFK)
                print("--- Общее время AFK:", summa,"---\n")
                time.sleep(AFK)
                Browser = Parsing(Html, Browser, Author, SPIN, i)
            
            Author = "Максимов А С"
            SPIN = "7284-7751"
            pagenum = 1
            EnterElibrary(Browser)
            FindSPINAuthor(Browser, SPIN)
            Html = ReturnHtmlCode(Browser)
            EndPage = FindPageNum(Html)
            print(Author)
            print("Всего страниц:", EndPage, end = " Сейчас открыта: ")
            print(pagenum)
            pagenum1 = list(range(2, int(EndPage) + 1))
            random.shuffle(pagenum1)
            AFK = random.uniform(5, 10)
            summa += AFK
            print("\nПерерыв между началом парсинга:", AFK)
            print("--- Общее время AFK:", summa,"---\n")
            time.sleep(AFK)
            Browser = Parsing(Html, Browser, Author, SPIN, pagenum)
            for i in pagenum1:
                print(i)
                Html = NextPage(Browser, Html, i)
                print("переход выполнен")
                AFK = random.uniform(5, 10)
                summa += AFK
                print("\nПерерыв между открытием следующей страницы:", AFK)
                print("--- Общее время AFK:", summa,"---\n")
                time.sleep(AFK)
                Browser = Parsing(Html, Browser, Author, SPIN, i)

            Author = "Прокофьев Е А"
            SPIN = "2023-0101"
            pagenum = 1
            EnterElibrary(Browser)
            FindSPINAuthor(Browser, SPIN)
            Html = ReturnHtmlCode(Browser)
            EndPage = FindPageNum(Html)
            print(Author)
            print("Всего страниц:", EndPage, end = " Сейчас открыта: ")
            print(pagenum)
            pagenum1 = list(range(2, int(EndPage) + 1))
            random.shuffle(pagenum1)
            AFK = random.uniform(5, 10)
            summa += AFK
            print("\nПерерыв между началом парсинга:", AFK)
            print("--- Общее время AFK:", summa,"---\n")
            time.sleep(AFK)
            Browser = Parsing(Html, Browser, Author, SPIN, pagenum)
            for i in pagenum1:
                print(i)
                Html = NextPage(Browser, Html, i)
                print("переход выполнен")
                AFK = random.uniform(5, 10)
                summa += AFK
                print("\nПерерыв между открытием следующей страницы:", AFK)
                print("--- Общее время AFK:", summa,"---\n")
                time.sleep(AFK)
                Browser = Parsing(Html, Browser, Author, SPIN, i)

            Author = "Назойкин Е А"
            SPIN = "6158-5583"
            pagenum = 1
            EnterElibrary(Browser)
            FindSPINAuthor(Browser, SPIN)
            Html = ReturnHtmlCode(Browser)
            EndPage = FindPageNum(Html)
            print(Author)
            print("Всего страниц:", EndPage, end = " Сейчас открыта: ")
            print(pagenum)
            pagenum1 = list(range(2, int(EndPage) + 1))
            random.shuffle(pagenum1)
            AFK = random.uniform(5, 10)
            summa += AFK
            print("\nПерерыв между началом парсинга:", AFK)
            print("--- Общее время AFK:", summa,"---\n")
            time.sleep(AFK)
            Browser = Parsing(Html, Browser, Author, SPIN, pagenum)
            for i in pagenum1:
                print(i)
                Html = NextPage(Browser, Html, i)
                print("переход выполнен")
                AFK = random.uniform(5, 10)
                summa += AFK
                print("\nПерерыв между открытием следующей страницы:", AFK)
                print("--- Общее время AFK:", summa,"---\n")
                time.sleep(AFK)
                Browser = Parsing(Html, Browser, Author, SPIN, i)

            Author = "Савватеев Е В"
            SPIN = "7636-2203"
            pagenum = 1
            EnterElibrary(Browser)
            FindSPINAuthor(Browser, SPIN)
            Html = ReturnHtmlCode(Browser)
            EndPage = FindPageNum(Html)
            print(Author)
            print("Всего страниц:", EndPage, end = " Сейчас открыта: ")
            print(pagenum)
            pagenum1 = list(range(2, int(EndPage) + 1))
            random.shuffle(pagenum1)
            AFK = random.uniform(5, 10)
            summa += AFK
            print("\nПерерыв между началом парсинга:", AFK)
            print("--- Общее время AFK:", summa,"---\n")
            time.sleep(AFK)
            Browser = Parsing(Html, Browser, Author, SPIN, pagenum)
            for i in pagenum1:
                print(i)
                Html = NextPage(Browser, Html, i)
                print("переход выполнен")
                AFK = random.uniform(5, 10)
                summa += AFK
                print("\nПерерыв между открытием следующей страницы:", AFK)
                print("--- Общее время AFK:", summa,"---\n")
                time.sleep(AFK)
                Browser = Parsing(Html, Browser, Author, SPIN, i)

            Author = "Ахмедова Х Г"
            SPIN = "5676-5382"
            pagenum = 1
            EnterElibrary(Browser)
            FindSPINAuthor(Browser, SPIN)
            Html = ReturnHtmlCode(Browser)
            EndPage = FindPageNum(Html)
            print(Author)
            print("Всего страниц:", EndPage, end = " Сейчас открыта: ")
            print(pagenum)
            pagenum1 = list(range(2, int(EndPage) + 1))
            random.shuffle(pagenum1)
            AFK = random.uniform(5, 10)
            summa += AFK
            print("\nПерерыв между началом парсинга:", AFK)
            print("--- Общее время AFK:", summa,"---\n")
            time.sleep(AFK)
            Browser = Parsing(Html, Browser, Author, SPIN, pagenum)
            for i in pagenum1:
                print(i)
                Html = NextPage(Browser, Html, i)
                print("переход выполнен")
                AFK = random.uniform(5, 10)
                summa += AFK
                print("\nПерерыв между открытием следующей страницы:", AFK)
                print("--- Общее время AFK:", summa,"---\n")
                time.sleep(AFK)
                Browser = Parsing(Html, Browser, Author, SPIN, i)

            Author = "Логунова Н Ю"
            SPIN = "7813-9631"
            pagenum = 1
            EnterElibrary(Browser)
            FindSPINAuthor(Browser, SPIN)
            Html = ReturnHtmlCode(Browser)
            EndPage = FindPageNum(Html)
            print(Author)
            print("Всего страниц:", EndPage, end = " Сейчас открыта: ")
            print(pagenum)
            pagenum1 = list(range(2, int(EndPage) + 1))
            random.shuffle(pagenum1)
            AFK = random.uniform(5, 10)
            summa += AFK
            print("\nПерерыв между началом парсинга:", AFK)
            print("--- Общее время AFK:", summa,"---\n")
            time.sleep(AFK)
            Browser = Parsing(Html, Browser, Author, SPIN, pagenum)
            for i in pagenum1:
                print(i)
                Html = NextPage(Browser, Html, i)
                print("переход выполнен")
                AFK = random.uniform(5, 10)
                summa += AFK
                print("\nПерерыв между открытием следующей страницы:", AFK)
                print("--- Общее время AFK:", summa,"---\n")
                time.sleep(AFK)
                Browser = Parsing(Html, Browser, Author, SPIN, i)

            Author = "Благовещенский И Г"
            SPIN = "7057-5071"
            pagenum = 1
            EnterElibrary(Browser)
            FindSPINAuthor(Browser, SPIN)
            Html = ReturnHtmlCode(Browser)
            EndPage = FindPageNum(Html)
            print(Author)
            print("Всего страниц:", EndPage, end = " Сейчас открыта: ")
            print(pagenum)
            pagenum1 = list(range(2, int(EndPage) + 1))
            random.shuffle(pagenum1)
            AFK = random.uniform(5, 10)
            summa += AFK
            print("\nПерерыв между началом парсинга:", AFK)
            print("--- Общее время AFK:", summa,"---\n")
            time.sleep(AFK)
            Browser = Parsing(Html, Browser, Author, SPIN, pagenum)
            for i in pagenum1:
                print(i)
                Html = NextPage(Browser, Html, i)
                print("переход выполнен")
                AFK = random.uniform(5, 10)
                summa += AFK
                print("\nПерерыв между открытием следующей страницы:", AFK)
                print("--- Общее время AFK:", summa,"---\n")
                time.sleep(AFK)
                Browser = Parsing(Html, Browser, Author, SPIN, i)

            Author = "Гольденберг С П"
            SPIN = "3362-4012"
            pagenum = 1
            EnterElibrary(Browser)
            FindSPINAuthor(Browser, SPIN)
            Html = ReturnHtmlCode(Browser)
            EndPage = FindPageNum(Html)
            print(Author)
            print("Всего страниц:", EndPage, end = " Сейчас открыта: ")
            print(pagenum)
            pagenum1 = list(range(2, int(EndPage) + 1))
            random.shuffle(pagenum1)
            AFK = random.uniform(5, 10)
            summa += AFK
            print("\nПерерыв между началом парсинга:", AFK)
            print("--- Общее время AFK:", summa,"---\n")
            time.sleep(AFK)
            Browser = Parsing(Html, Browser, Author, SPIN, pagenum)
            for i in pagenum1:
                print(i)
                Html = NextPage(Browser, Html, i)
                print("переход выполнен")
                AFK = random.uniform(5, 10)
                summa += AFK
                print("\nПерерыв между открытием следующей страницы:", AFK)
                print("--- Общее время AFK:", summa,"---\n")
                time.sleep(AFK)
                Browser = Parsing(Html, Browser, Author, SPIN, i)
    except:
        print("except")
    finally:
        print("finally")
    pass

if __name__ == "__main__":
    main()