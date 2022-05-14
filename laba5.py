class Lerning:
    """
    Абстрактный класс
    """
    def __init__(self, family, name, otchestvo, name_zavedenie):
        """ 
        Конструктор
        """
        self.__family = family
        self.__name = name
        self.__otchestvo = otchestvo
        self.__name_zavedenie = name_zavedenie

    def get_all(self):
        """
        получение всех значений атрибутов (ФИО, название заведение)
        """
        return [self.__family, self.__name, self.__otchestvo, self.__name_zavedenie]

    def set_all(self, spisok):
        """ 
        установить новые значение
        """
        self.__family = spisok[0]
        self.__name = spisok[1]
        self.__otchestvo = spisok[2]
        self.__name_zavedenie = spisok[3]

    def check_FIO(self, FIRST_SYMBOL):
        """ 
        проверка первых символов в Имени, Фамилии и Отчестве на букву "А".
        Если буква "А" не встречается, то возвращается True
        """
        if self.__name[:1] != FIRST_SYMBOL and self.__family[:1] != FIRST_SYMBOL and self.__otchestvo[:1] != FIRST_SYMBOL:
            return True
        return False

class Student(Lerning):
    """ 
    Класс студентов
    """
    def __init__(self, family, name, otchestvo, name_zavedenie, number_student_ticket):
        """
        конструктор класса студента
        """
        super().__init__(family=family, name=name, otchestvo=otchestvo, name_zavedenie=name_zavedenie)
        """
        super() обращаемся к родительскому классу Lerning с вызывом его конструктора с передачей ФИО и название заведения
        """
        self.__number_student_ticket = number_student_ticket

    def __str__(self):
        """ 
        метод, отвечающий за вывод. Вызывается print(), а внутрь скобок название экземпляра класса (объект), 
        то есть создали экземпляр класса student_Petrov = Student(parametrs),
        а потом print(student_Petrov)
        """
        values = []
        for value in self.__dict__.values():    #__dict__ - это метод для словаря. Далее хочу получить только значения из этого словаря
            values.append(value)
        return f'Фамилия: {values[0]:12s}Имя: {values[1]:10s}Отчество: {values[2]:15s}Название заведения: {values[3]:6s} Номер студенческого билета: {values[4]:<3d}'

    def sort(self, other_object):
        """ 
        Сортировка пузырьковым методом. self - текущий объект; other_object - другой объект
        """
        self_spisok = self.get_all() # получаем текущие значение объекта self
        other_object_spisok = other_object.get_all() #получаем текущие значение other_object (другого объекта)
        if self_spisok[0] > other_object_spisok[0]: #сортировка по фамилии
            temp = []
            temp.extend(self_spisok)    #временная список с хранением значений объекта self
            temp_number_student_ticket = self.__number_student_ticket   #временная переменная с хранением номером билета объекта self
            self.set_all(other_object_spisok)   #устанавливаем новые значения объекта self на значения other_object 
            self.__number_student_ticket = other_object.__number_student_ticket #установим новое значение Номер билета объекта self на значение other_object
            other_object.set_all(temp)  #устанавливаем новые значения объекта other_object на значения объекта self, помещенные во временный список
            other_object.__number_student_ticket = temp_number_student_ticket   #установим новое значение Номер билета объекта other_object на знаачение self

    def compareTo(self, act, FIRST_SYMBOL, NUMBER_STUDENT_TICKET):
        """ 
        Назвал как в методочке
        """
        match act:
            case 1:
                if self.check_FIO(FIRST_SYMBOL):   #проверяем текущий объект на первичный символ. Если не встречаются, то проходим дальше
                    return True
            case 2:
                if self.__number_student_ticket != NUMBER_STUDENT_TICKET:   #проверяем текущий объект на Номер студенческого билета
                    return True                 #если не встречается, то возвращается True
        return False        #Если хоть одно условие не выполнилось, то вернет False

class SchoolBoy(Lerning):
    """ 
    Класс школьников
    """
    def __init__(self, family, name, otchestvo, name_zavedenie, arf_score):
        """ 
        Конструктор класса школьников
        """
        super().__init__(family=family, name=name, otchestvo=otchestvo, name_zavedenie=name_zavedenie)
        """ 
        Через super() вызываем родительский конструктор с передачей параметров ФИО и название заведения
        """
        self.__arf_score = arf_score

    def __str__(self):
        """ 
        метод, отвечающий за вывод. Вызывается print(), а внутрь скобок название экземпляра класса (объект), 
        то есть создали экземпляр класса student_Petrov = Student(parametrs),
        а потом print(student_Petrov)
        """
        values = []
        for value in self.__dict__.values():      # __dict__ - это метод для словаря. Далее хочу получить только значения из этого словаря .values()
            values.append(value)
        return f'Фамилия: {values[0]:12s}Имя: {values[1]:10s}Отчество: {values[2]:15s}Название заведения: {values[3]:17s}Средняя оценка: {values[4]:<1.2f}'

    def sort(self, other_object):
        """ 
        Сортировка пузырьковым методом. self - текущий объект; other_object - другой объект

        Все тоже само, только вместо номера билета - средняя арифметическая оценка
        """
        self_spisok = self.get_all()
        other_object_spisok = other_object.get_all()
        if self.__arf_score > other_object.__arf_score:
            temp = []
            temp.extend(self_spisok)
            temp_arf_score = self.__arf_score
            self.set_all(other_object_spisok)
            self.__arf_score = other_object.__arf_score
            other_object.set_all(temp)
            other_object.__arf_score = temp_arf_score
    
    def compareTo(self, START_LIMIT_ARF_SCORE, END_LIMIT_ARF_SCORE):
        """ 
        Назвал как в методочке
        """
        if START_LIMIT_ARF_SCORE < self.__arf_score <= END_LIMIT_ARF_SCORE:     #Проверяем диапазон (3.5 < X <= 4.5]
            return True     #Если условие выполняется, то вернет True
        return False        #Иначе False

def print_result(peoples):   #это обычная функция, чтобы не дублировать в main.
    """ 
    Печатает объекты. peoples - содержит множество объектов; human - содержит один объект из множества peoples
    """
    for human in peoples:
        print(human)

def sorted_high(people):    #тоже обычная функция, чтобы не дублировать в main.
    """ 
    Сам пузырьковый метод
    """
    for i in range(len(people) - 1):    
        for j in range(i + 1, len(people)):
            people[i].sort(people[j])   #текущий объект self - people[i]. Этот текущий объект вызывает свой метод people[i].sort()
                                        #а в метод сорт передается следующий объект people[j]
    print_result(people)    #Вызывает функцию в 137 строчке кода

class Main:
    """ 
    Основной класс
    """
    FIRST_SYMBOL, NUMBER_STUDENT_TICKET, START_LIMIT_ARF_SCORE, END_LIMIT_ARF_SCORE = 'А', 150, 3.5, 4.5
    """ 
    Константы
    """
    students = [] #Пустой список студентов
    print()
    for _ in range(int(input('Введите количество студентов: '))):
        """ 
        символ Нижнее подчеркивание можно употреблять в цикле, если нам не нужно никак взаимодействовать со счетчиком циклом.
        """
        print()
        students.append(Student(input('Фамилия студента: '), input('Имя студента: '), input('Отчество студента: '), input('Название заведения: '), int(input('Номер студенческого билета: '))))
        """ 
        В конец списка добавляем объекты. 
        """
    school_boys = [] #Пустой список школьников
    print()
    for _ in range(int(input('Введите количество школьников: '))):
        print()
        school_boys.append(SchoolBoy(input('Фамилия школьника: '), input('Имя школьника: '), input('Отчество школьника: '), input('Название заведения: '), float(input('Средняя оценка школьника: '))))
    print()
    print_result(students)              #вызываем функцию в 137 строчке кода
    print()
    print_result(school_boys)           #вызываем функцию в 137 строчке кода
    print('\nПосле сортировки по возрастанию\n')
    sorted_high(students)               #вызываем функцию в 144 строчке кода
    print()
    sorted_high(school_boys)            #вызываем функцию в 144 строчке кода
    act = int(input('''Выберите 1, если хотите сортировать студентов, ФИО которых не начинается на букву «А»
Выберите 2, если хотите сортировать стдуентов № студенческого билета не равен 150
Ваш ответ: '''))
    print('\nПосле сортировки по ограничениям\n')
    for student in students:
        if student.compareTo(act, FIRST_SYMBOL, NUMBER_STUDENT_TICKET):              #Объект вызывает метод в 78 строчке кода
            print(student)
    print()
    for school_boy in school_boys:
        if school_boy.compareTo(START_LIMIT_ARF_SCORE, END_LIMIT_ARF_SCORE):    #Объект вызывает метод в 129 строчке кода
            print(school_boy)

