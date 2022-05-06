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

# my_car.go()
# print('\nrpm:', my_car.engine_rpm)
# print('current speed:', my_car.current_speed)


class Robot:

    def __init__(self):
        self.name = 'R2D2'

    def hello(self):
        print('Привет мир!')

    def __str__(self):      #метод __str__ сработае тогда, когда хотим распечатать значения объекта
        return self.name
    
    def __bool__(self):     #проверка на пустотсу или еще на что-нибудь
        return self.name != ''

    def __len__(self):      #вывод длины
        return len(self.name)

    def __eq__(self, other):    #сравнение двух объектов
        return self.name == other.name

    def __iadd__(self, other):  #складывание двух объектов
        self.name += other.name
        return self

    def __del__(self):      #метод __del__ сработает тогда, когда программа закончится свое выполнение или объект будет равен None
        print('Прощай объект...')

robot = Robot()

# robot.temperature = 1       #Можно добавить атрибут к экземпляру, который нет в конструкторе
# while robot.temperature < 10:
#     robot.temperature *= 2
# print(robot.temperature)
# del robot.temperature       #Удаляет общедоступный, защищенный и приватный атрибут у экземпляра

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
# robot += robot1
# print(robot, robot1)
