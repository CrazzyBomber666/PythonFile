import numpy as np

"""
Метод .shape возвращает количество строк и столбцов в матрице
Метод .flatten переконвертирует двумерный массив в одномерный массив
Метод np.sum(Name) и np.prod(Name) суммируют и перемножают все элементы матрицы соответственно
Name.mean() находит среднее арифметическое всей матрицы
Name.var() находит дисперсию всей матрицы
Name.std() находит стандартное отклонение всей матрицы
Name.argmin() возвращает индекс минимального элемента всей матрицы
Name.min() возвращает минимальный элемент всей матрицы
Name.mean(axis=0 or 1) находит среднее арифметическое по каждому столбцу or по строке соответственно
Name.clip(min_interval, max_interval) если элемент матрица меньше заданного интервала, то заменяет элемент на минимальный интервал и наоборот
np.unique(Name) выведит список элементов матрица без повторяющихся элементов в порядке возрастания
Name.diagonal() выведет диагоноль матрицы
np.where(Условие, если правда, если ложь)
Name.nonzero() возвращает индексы строк и столбцов элементов матрицы не равные 0
np.isnan(Name) проверка элементов матрицы на пустоту
np.isfinite(Name) проверка элементов матрицы на бесконечность
Name[Name > Numbers] or Name.take(Name, axis = 0) выведет все элементы массива удовлетворяют условию. axis изначально принимает значение по умолчанию
Name[Name_2] or Name[Name_2, Name_3] выведет все элементы массива или матрицы Name соответствующим индексам массива Name_2 или индексам массивов Name_2 и Name_3
Name.put([Number, Number_2], Name_2) Если в массиве Name присутствует число Number or Number_2, то заменит элементы массива Name на элементы массива Name_2,
                                                                                                                                начиная с нулевого индекса
np.poly(Name) передает элементы массива их корни для вычисления уравления полинома. Выдаст значения элементы уравнения
np.roots(Name) передает значения элементы из уравнения и возвращает элементы массива их корни
np.polyval(Name, Number) вычисляет уравнения, подставляя множители х из массива Name и заменяет х на число Number
Функции np.polyadd(), np.polysub(), np.polymul() и np.polydiv() также поддерживают суммирование, вычитание, умножение и деление коэффициентов 
                                                                                                                        многочлена, соответственно.


"""

'''spisok = np.array([[np.random.randint(1, 6) for _ in range(2)] for _ in range(5)])
print(spisok)
for (i, j) in spisok:
    print(i * j, end ='; ')
'''

'''import random as r
spisok = [[r.randint(1, 5) for _ in range(2)] for _ in range(5)]
print(spisok)
for (i, j) in spisok:
    print(i * j, end ='; ')
'''

'''spisok = np.array([[np.random.randint(1, 3) for _ in range(2)] for _ in range(5)])
print(spisok)
print(np.prod(spisok))
'''

'''spisok = np.array([[np.random.randint(0, 5) for _ in range(2)] for _ in range(5)])
print(spisok, spisok.mean(axis=0))
'''

#_____СРАВНЕНИЕ СТРОК_____

#проверить на длину строки
#если одинаковые, то в цикле проверить каждую
#иначе длина большей строки "Победила"

'''import requests

session = requests.Session()

headers = {
    'user-agent': 'Mozila'
    }

url = 'https://www.elibrary.ru/'

response = session.get(url=url, headers=headers)
if response.status_code == 200:
    print('Success!')
    print(response.text)
elif response.status_code == 404:
    print('Not Found.')'''

# class Toytota:

#     def __init__(self):
#         self.color = 'Бордовый'
#         self.price = '1 000 000 руб'
#         self.max_speed = '200 км/ч'
#         self.current_speed = '0 км/ч'
#         self.engine_rpm = 0
    
#     def start(self):
#         print('Мотор запущен')
#         self.engine_rpm = 900

#     def go(self):
#         print('Поехали')
#         self.engine_rpm = 2000
#         self.current_speed = '20 км/ч'


# my_car = Toytota()
# print('Color:', my_car.color)
# print('Price:', my_car.price)
# print('max_speed:', my_car.max_speed)
# print('rpm:', my_car.engine_rpm)
# print('current speed:', my_car.current_speed)

# my_car.start()
# print('\nrpm:', my_car.engine_rpm)
# # 
# my_car.go()
# print('\nrpm:', my_car.engine_rpm)
# print('current speed:', my_car.current_speed)
# 
# class Robot:
# 
    # def __init__(self):
        # self.name = 'R2D2'
# 
    # def hello(self):
        # print('Привет мир!')
# 
    # def __str__(self):      #метод __str__ сработае тогда, когда хотим распечатать значения объекта
        # return self.name
    # 
    # def __bool__(self):     #проверка на пустотсу или еще на что-нибудь
        # return self.name != ''
# 
    # def __len__(self):      #вывод длины
        # return len(self.name)
# 
    # def __eq__(self, other):    #сравнение двух объектов
        # return self.name == other.name
# 
    # def __iadd__(self, other):  #складывание двух объектов
        # self.name += other.name
        # return self
# 
    # def __del__(self):      #метод __del__ сработает тогда, когда программа закончится свое выполнение или объект будет равен None
        # print('Прощай объект...')
# 
# robot = Robot()
# 
# robot.temperature = 1       #Можно добавить атрибут к экземпляру, который нет в конструкторе
# while robot.temperature < 10:
#     robot.temperature *= 2
# print(robot.temperature)
# del robot.temperature       #Удаляет общедоступный, защищенный и приватный атрибут у экземпляра
#
# name_attribute = 'model'
# if hasattr(robot, name_attribute):  #Проверка на существующий общедоступный или защищенный атрибут
#     print(robot.model)
# else:
#     setattr(robot, name_attribute, 'android')   #создает общедоступный или защищенный атрибут model для экземпляра robot со значением 'android'
#     print(robot.model)
# print(getattr(robot, name_attribute))   #также можем получить общедоступный или защищенный атрибут
# delattr(robot, name_attribute)          #также можем удалить общедоступный или защищенный атрибут

# robot1 = Robot()
# robot = None
# robot1 = None

# robot.name = ''
# print(bool(robot), len(robot))
# if robot:                           #Если не будут предопределены методы __len__ или __bool__, а может еще какие-то, то он будет проверять условие
#                                     #на существование самого объекта. 
#     print('Имя присвоенно')
#     print('Имя:', robot.name, 'Состоит из', len(robot), 'символ(а, ов)')
# else:
#     print('Имя не присвоенно')

# __eq__(self, other)           -->     равенство двух объектов       ==
# __nq__(self, other)           -->     не равенство двух объектов    !=
# __lt__(self, other)           -->     строго меньше                 <
# __le__(self, other)           -->     меньше или равно              <=
# __gt__(self, other)           -->     строго больше                 >
# __ge__(self, other)           -->     больше или равно              >=

# robot1 = Robot()
# # robot1.name = 'R3D3'
# print(robot, robot1)
# if robot == robot1:
#     print('имена равны')

# __iadd__(self, other)         -->     сложить значения двух объектов                      +=
# __isub__(self, other)         -->     вычесть значения двух объектов                      -=
# __imul__(self, other)         -->     умножить значения двух объектов                     *=
# __itruediv__(self, other)     -->     делить значения двух объектов                       /=
# __ifloordiv__(self, other)    -->     целочисленное деление значения двух объектов        //=
# __imod__(self, other)         -->     вычисление остатка значения двух объектов           %=
# __ipow__(self, other)         -->     возведение в степень значения двух объектов         **=

# robot1 = Robot()
# robot1.name = '567'
# print(robot, robot1)
# robot += robot15
# print(robot, robot1)


# class Pet:
#     legs = 4
#     has_trail = True

#     def inspect(self):
#         print('Всего ног:', self.legs)
#         print('Хвост присутствует - ', 'да' if self.has_trail else 'нет')

# class Cat(Pet):
    
#     def sound(self):
#         print('Мяу')

# class Dog(Pet):

#     def sound(self):
#         print('Гав')

# class Hamster(Pet):

#     def sound(self):
#         print('Ццццццц')

# print('Котик')
# my_pet = Cat()
# my_pet.inspect()
# my_pet.sound()
# print('Собачка')
# my_pet = Dog()
# my_pet.inspect()
# my_pet.sound()
# print('Хомячок')
# my_pet = Hamster()
# my_pet.inspect()
# my_pet.sound()


""" 
Чекнуть библиотеку selenium_stealth 
Сайты не будут идеть, что это автоматизированное средство для тестирования
"""

# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,
 
# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

# from random import randint

# class House:
# 
    # def __init__(self):
        # self.__money = 100
        # self.__food = 50
        # self.__ashed = 0
# 
    # def _get_food(self):
        # return self.__food
# 
    # def _get_money(self):
        # return self.__money
# 
    # def _get_ashed(self):
        # return self.__ashed
# 
    # def _set_food(self, count_food):
        # self.__food += count_food
# 
    # def _set_money_after_buy(self, price):
        # self.__money -= price
# 
    # def _set_money_after_work(self, price):
        # self.__money += price
# 
    # def set_ashed(self):
        # self.__ashed += 5
# 
    # def _set_ashed(self):
        # self.__ashed = 0
# 
    # def __str__(self):
        # return 'В доме денег: {}, еды: {}, грязи: {}'.format(*self.__dict__.values())
# 
# class Human:
# 
    # def __init__(self, house):
        # self.__fullness = 30
        # self.__happiness = 100
        # self.__house = house
# 
    # def _get_fullness(self):
        # return self.__fullness
# 
    # def _get_happiness(self):
        # return self.__happiness
# 
    # def _get_house_food(self):
        # return self.__house._get_food()
# 
    # def _get_house_money(self):
        # return self.__house._get_money()
# 
    # def _get_house_ashed(self):
        # return self.__house._get_ashed()
# 
    # def _set_house_ashed(self, name):
        # self.__house._set_ashed()
        # print('{} убрала квартиру'.format(name))
# 
    # def _set_house(self):
        # self.__house._set_money_after_work(price=150)
# 
    # def _set_fullness_after_eat(self, name, fullness):
        # if self.__fullness + fullness > 100:
            # self.__fullness = 100
        # else:
            # self.__fullness += fullness
            # self.__house._set_food(count_food=-fullness)
        # print('{} покушал(а)'.format(name))
# 
    # def _set_fullness_after_other_act(self, fullness):
        # self.__fullness -= fullness
# 
    # def _set_happiness(self, count_happiness):
        # if self.__happiness + count_happiness > 100:
            # self.__happiness = 100
        # else:
            # self.__happiness += count_happiness
# 
    # def _buy_products(self, name, price):
        # if self._get_house_money() - price > 0:
            # self.__house._set_money_after_buy(price)
            # self.__house._set_food(price)
            # print('{} сходила в магазин и купила продукты на сумму {}'.format(name, price))
            # return True
        # else:
            # return False
# 
    # def __str__(self, name):
        # return 'У {} степень сытости: {}, степень счастья: {}'.format(name, *self.__dict__.values())
# 
# class Husband(Human):
# 
    # def __init__(self, name, house):
        # super().__init__(house)
        # self.__name = name
# 
    # def __str__(self):
        # return super().__str__(name=self.__name)
# 
    # def eat(self):
        # fullness = randint(1, 30)
        # if super()._get_house_food() - fullness < 0:
            # print('{} не хватает еды'.format(self.__name))
            # super()._set_happiness(count_happiness=-2)
            # super()._set_fullness_after_other_act(fullness=10)
        # else:
            # super()._set_fullness_after_eat(name=self.__name, fullness=fullness)
            # super()._set_happiness(count_happiness=-2)
# 
    # def play_game_WoT(self):
        # super()._set_fullness_after_other_act(fullness=10)
        # super()._set_happiness(count_happiness=20)
        # print('{} поиграл в World Of Tanks'.format(self.__name))
# 
    # def go_work(self):
        # super()._set_fullness_after_other_act(fullness=10)
        # super()._set_house()
        # super()._set_happiness(count_happiness=-10)
        # print('{} сходил на работу и заработал 150 денег'.format(self.__name))
# 
    # def act(self):
        # if super()._get_fullness() <= 0 or super()._get_happiness() <= 0:
            # print('--'*10 + '{} умер!!!!'.format(self.__name))
        # elif super()._get_house_money() < 60:
            # self.go_work()
        # elif super()._get_fullness() <= 30:
            # self.eat()
        # elif super()._get_happiness() <= 30:
            # self.play_game_WoT()
        # elif super()._get_house_money() <= 60:
            # self.go_work()
        # else:
            # act = randint(1, 3)
            # match act:
                # case 1:
                    # self.play_game_WoT()
                # case 2:
                    # self.eat()
                # case 3:
                    # self.go_work()
# 
# class Wife(Human):
# 
    # def __init__(self, name, house):
        # super().__init__(house)
        # self.__name = name
# 
    # def __str__(self):
        # return super().__str__(name=self.__name)
        # 
    # def eat(self):
        # fullness = randint(1, 30)
        # if super()._get_house_food() - fullness < 0:
            # print('{} не хватает еды'.format(self.__name))
            # super()._set_happiness(count_happiness=-2)
            # super()._set_fullness_after_other_act(fullness=10)
        # else:
            # super()._set_fullness_after_eat(name=self.__name, fullness=fullness)
            # super()._set_happiness(count_happiness=-2)
# 
    # def buy_products(self):
        # if super()._buy_products(name=self.__name, price=randint(30, 60)):
            # super()._set_happiness(count_happiness=-10)
            # super()._set_fullness_after_other_act(fullness=10)
        # else:
            # print('{} не хватило денег на продукты'.format(self.__name))
            # super()._set_fullness_after_other_act(fullness=10)
            # super()._set_happiness(count_happiness=-10)
# 
    # def buy_shuba(self):
        # if super()._buy_products(name=self.__name, price=150):
            # super()._set_happiness(count_happiness=60)
            # super()._set_fullness_after_other_act(fullness=10)
        # else:
            # print('{} не хватило денег на шубу'.format(self.__name))
            # super()._set_happiness(count_happiness=-10)
            # super()._set_fullness_after_other_act(fullness=10)
# 
    # def do_out_in_home(self):
        # super()._set_house_ashed(name=self.__name)
        # super()._set_fullness_after_other_act(fullness=10)
        # super()._set_happiness(count_happiness=-20)
        # 
    # def act(self):
        # if super()._get_fullness() <= 0 or super()._get_happiness() <= 0:
            # print('--'*10 + '{} умер!!!!'.format(self.__name))
        # elif super()._get_house_food() <= 60:
            # self.buy_products()
        # elif super()._get_happiness() <= 30:
            # self.buy_shuba()
        # elif super()._get_fullness() <= 30:
            # self.eat()
        # elif super()._get_house_ashed() >= 80:
            # self.do_out_in_home()
        # else:
            # act = randint(1, 3)
            # match act:
                # case 1:
                    # self.buy_products()
                # case 2:
                    # self.buy_shuba()
                # case 3:
                    # self.do_out_in_home()
            # pass
# 
# if __name__ == '__main__':
    # home = House()
    # maks = Husband(name='Макс', house=home)
    # masha = Wife(name='Маша', house=home)
    # print()
    # print(maks)
    # print(masha)
    # print(home)
# 
    # year = 30
    # for day in range(1, 365 * year + 1):
        # print('-'*25 + str(day) + ' День' + str('-')*25)
        # maks.act()
        # masha.act()
        # home.set_ashed()
        # print(maks)
        # print(masha)
        # print(home)
    # 
# 

# chr()     # Преобразование кода в символ
# ord()     # Преобразование символа в код
# hex()     # Преобразование кода в шестнадцатеричный код

# name_byte = b'\xd1\x84' хранение сырых байтов. Можно хранить состояние БД, символы, музыку и т.д.
# байты можно работать, как со строковыми типы данных
# Последовательность байта не изменяемая

# bytearray(b'hello')
# ba[0] = 32 # код пробела
# print(ba)

# bytearray('привет', encoding='utf-8') создать последовательность байт из юникодной строки.
 
# utf-16 
# cp866 DOSовская кодировка

# name_byte = b'\xd1\x84'.decode(encoding='utf-8) декодировать кодировку.

# from pprint import pprint

# print()
# file_name = 'byron' # - файл, который надо прочитать
# file = open(file_name, mode='rb')   # mode - режим бинарного чтения. r - чтение, b - бинарное
# file_content = file.read()       # прочитать файл
# file.close()            # закрыть файл
# pprint(file_content)    # английский текст можно не декодировать
# pprint(file_content.decode('utf-8'))    # остальыне зяыки надо декодировать


# print()
# file_name = 'byron'
# file = open(file_name, mode='r')    #на linux можно не указывать бинарность. Все прочтется. Операционная система выберит свою кодировку.
# file_content = file.read()
# file.close()
# pprint(file_content)


# print()
# file_name = 'byron'
# file = open(file_name, mode='r', encoding='utf-8')  # укажем сразу кодировку, которую надо перекодировать. 
# file_content = file.read()
# file.close()
# pprint(file_content)


# print()
# file_name = 'byron_magic'
# file = open(file_name, mode='w', encoding='utf-8')    # w - режим записи, символьная. Кодировка будет utf-8
# file_content = 'Hello, world!\n\nПривет, мир!'
# file.write(file_content)
# file.close()

# file = open(file_name, mode='r', encoding='utf-8')
# file_content = file.read()
# file.close()
# pprint(file_content)


# print()
# file_name = 'byron_magic'
# file = open(file_name, mode='wb')    # w - режим бинарной записи
# file_content = b'Hello, world!'     # можно бинарить только английский текст
# file.write(file_content)
# file.close()

# file = open(file_name, mode='r', encoding='utf-8')
# file_content = file.read()
# file.close()
# pprint(file_content)


# print()
# file_name = 'byron_magic'
# file = open(file_name, mode='a', encoding='utf-8')    # a - тоже, что и режим w, только файл не обнуляет, а добавляет содержимое в конец строки
                                                        # a - append(), как у список.
# file_content = 'Hello, world!'
# file.write(file_content)
# file.close()

# file = open(file_name, mode='r', encoding='utf-8')
# file_content = file.read()
# file.close()
# pprint(file_content)


# print()
# file_name = 'byron_magic'       # открыть существующий файл, иначе ошибка
# file = open(file_name, mode='r+', encoding='utf-8')    # r+ - режим чтение с записью
# file_content = file.read()
# file.write('\n я новая информация')
# file.close()

# file = open(file_name, mode='r', encoding='utf-8')
# file_content = file.read()
# file.close()
# pprint(file_content)
""" для режима w+ - создается пустой файл, если его нет, иначе обнуляет содержимое файла. 
    для бинарных режимов открываются video, music, image.
"""


# print()
# file_name = 'byron_magic'
# file = open(file_name, mode='r', encoding='utf-8)
# file_content = file.read(2)
# pprint(file_content)
# pprint(file.tell())         #указывает, сколько символов прочитано. Тут 2

# file_content = file.read(39)    
# pprint(file_content)
# pprint(file.tell())         #тут 41

# file_content = file.read(1)    
# pprint(file_content)
# pprint(file.tell())         #а вот тут 43. Так как пошли русские символы, то они уже содержат по 2 байта за каждый символ
#                             #и получается, что 41 + 2 = 43

# file_content = file.read(1)    
# pprint(file_content)
# pprint(file.tell())         #а вот тут 44. Так как пробел умещается в 1 байт.
# file.close()


# import io

# print()
# file_name = 'byron_magic'
# file = open(file_name, mode='r', encoding='utf-8')
# file_content = file.read(2)
# pprint(file_content)
# pprint(file.tell())

# new_position = file.seek(0, io.SEEK_SET) #--> можно хранить значения в переменных
# io.SEEK_SET --> начало файла
# io.SEEK_CUR --> текущая позиция файла
# io.SEEK_END --> конец файлв
# file.seek(0, io.SEEK_SET)
# file_content = file.read(2)
# pprint(file_content)
# pprint(file.tell())

# file.seek(0, io.SEEK_CUR)
# file_content = file.read(2)
# pprint(file_content)
# pprint(file.tell())

# file.seek(1, io.SEEK_SET) #сместились на 1 символ назад от начала файла
# file_content = file.read(2)
# pprint(file_content)
# pprint(file.tell())

# file.seek(0, io.SEEK_CUR)
# file_content = file.read(2)
# pprint(file_content)
# pprint(file.tell())

# new_position = file.seek(0, io.SEEK_END)
# file_content = file.read()
# pprint(file_content)
# pprint(file.tell())
# file.close()


# file.fluash()     #файл принудительно записывает весь буфер на диск, если вдруг что-то сломалось


# file_name = 'byron'
# file = open(file_name, mode='r', encoding='utf-8')
# for line in file:
#     print(line, end='')
# file.close()

# file_name = 'byron'
# file = open(file_name, mode='r', encoding='utf-8')
# lines = file.readlines()
# for line in lines:          # Минус такого подхода в том, что все прочитывается из памяти. Для маленьких файлов это простительно, быстрое управление
#     print(line, end='')     # а для больших это минус. Может зависнусть
# file.close()

# print()
# file_name = 'byron'
# file = open(file_name, mode='r', encoding='utf-8')
# for line in file:
#     if 'друзья' in line:
#         print('слово найдено в строке:', line)
#         break
# else:
#     print('запрашиваемое слово не найденно')
# file.close()


# Надо следить, чтобы файл при выходе из программ был закрыт. Если не закроем, то потеряем данные.
# print()
# file_name = 'byron'
# with open(file_name, mode='r', encoding='utf-8') as file:
#     """
#     Все что внутри выполняется, а как закончится, то закроет файл. Даже, если случится ошибка
#     то он принудительно закроет файл
#     """
#     for line in file:
#         print(line, end='')
#     print('Файл закрыт? -', 'Да' if file.closed else 'Нет')
# print('Файл закрыт? -', 'Да' if file.closed else 'Нет')


# class InOutBlock:

#     def __enter__(self):
#         print('Входим в блок кода')

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Выходим из блока кода')

# with InOutBlock() as file:
#     print('Блок кода')

# import os

# path = '/home/exflashgame/Рабочий стол'
# print('\n\n')
# for dirpath, dirname, filename in os.walk(path):
#     print(f'|{"Путь:" + dirpath:-<140}|')
#     print(f'|{"Папки":-^140}|')
#     for dir_name in dirname:
#         print(f'{dirpath:90s}, {dir_name}')
#     print(f'|{"Файлы":-^140}|')
#     for file in filename:
#         print(f'{dirpath:90s}, {file}')


# path = os.path.normpath(path)                                     # приведет к нормальному пути к каждой Операционной Системе
# full_dir_path = os.path.getctime(os.path.join(dirpath, file))     # выведет даты создания файлов или папок, а также сразу нормализует к каждой Операционной Системе
# secs = os.path.getctime(full_dir_path)                            # Эпоха, какая-то, которая отображается в секундах, а мы хотим видеть привычный год, месяц, день и т.д.
# file_time = time.gmtime(secs)                                     # https://docs.python.org/3/library/time.html#time.struct_time


""" 
Если нам нужно распоковать zip файл и достать нужный для нас файл (мы знаем точное его название)
"""
# import zipfile

# zip_file_name = 'Название zip файла'
# file_name = 'Название файла, которое ищем'
# zfile = zipfile.ZipFile(zip_file_name, mode='r')
# for filename in zfile.namelist():                   # перебор всех файлов в архиве
#     if file_name == filename:                       # Если название файла совпала с названием файла в архиве
#         zfile.extract(filename)                     # тогда распакуем в этуже дерикторию 


# def fun():
#     while True:
#         try:
#             a = int(input())
#             a = 10 / a
#             break
#         except ZeroDivisionError as Z:
#             print(f'Деление на ноль {Z}')

# fun()


# try:
#     10 / 0
#     print('Деление успешно')
# except ZeroDivisionError:
#     print('Деление на ноль')
# except NameError:
#     print('Неизвестная переменная')
# else:
#     print('Ошибок нет')
# finally:
#     print('Пока')


