class Adress:

    def __init__(self, name_street, number_house, number_kvartira):
        self.__name_street = name_street
        self.__number_house = number_house
        self.__number_kvartira = number_kvartira

    def __lt__(self, other_object):
        return self.__number_kvartira < other_object.__number_kvartira

    def __str__(self):
        return f'Название улицы: {self.__name_street:10s}, Номер дома: {self.__number_house:3d}, Номер квартиры: {self.__number_kvartira:3d}'

def print_on_screen(objects, title):
    print('\n' + title + '\n')
    for object in objects:
        print(object)

class main:
    print()
    count_adress = int(input('Введите количество объектов: '))
    if count_adress <= 0:
        print('Error')
    else:
        adress = []
        for _ in range(count_adress):
            adress.append(Adress(name_street=input('Введите название улицы: '), number_house=int(input('Введите номер дома: ')), number_kvartira=int(input('Введите номер квартиры:'))))
        print_on_screen(objects=adress, title='Список введенных адресов до сортировки')
        adress.sort()
        print_on_screen(objects=adress, title='Список введенных адресов после сортировка по "номерам квартирам"')

        
