class Lerning:
    def __init__(self, family, name, otchestvo, name_zavedenie):
        self.__family = family
        self.__name = name
        self.__otchestvo = otchestvo
        self.__name_zavedenie = name_zavedenie

    def get_all(self):
        return [self.__family, self.__name, self.__otchestvo, self.__name_zavedenie]

    def set_all(self, spisok):
        self.__family = spisok[0]
        self.__name = spisok[1]
        self.__otchestvo = spisok[2]
        self.__name_zavedenie = spisok[3]

    def check_FIO(self, FIRST_SYMBOL):
        if self.__name[:1] != FIRST_SYMBOL and self.__family[:1] != FIRST_SYMBOL and self.__otchestvo[:1] != FIRST_SYMBOL:
            return True
        return False

class Student(Lerning):

    def __init__(self, family, name, otchestvo, name_zavedenie, number_student_ticket):
        super().__init__(family=family, name=name, otchestvo=otchestvo, name_zavedenie=name_zavedenie)
        self.__number_student_ticket = number_student_ticket

    def __str__(self):
        values = []
        for value in self.__dict__.values():
            values.append(value)
        print('-' * 50)
        return 'Фамилия: \t\t\t{}\nИмя: \t\t\t\t{}\nОтчество: \t\t\t{}\nНазвание заведения:\t\t{}\nНомер студенческого билета: \t{}'.format(*values)

    def sort(self, other_object):
        self_spisok = self.get_all()
        other_object_spisok = other_object.get_all()
        if self_spisok[0] > other_object_spisok[0]:
            temp = []
            temp.extend(self_spisok)
            temp_number_student_ticket = self.__number_student_ticket
            self.set_all(other_object_spisok)
            self.__number_student_ticket = other_object.__number_student_ticket
            other_object.set_all(temp)
            other_object.__number_student_ticket = temp_number_student_ticket

    def compareTo(self, FIRST_SYMBOL, NUMBER_STUDENT_TICKET):
        if self.check_FIO(FIRST_SYMBOL):
            if self.__number_student_ticket != NUMBER_STUDENT_TICKET:
                return True
        return False

class SchoolBoy(Lerning):
    
    def __init__(self, family, name, otchestvo, name_zavedenie, arf_score):
        super().__init__(family=family, name=name, otchestvo=otchestvo, name_zavedenie=name_zavedenie)
        self.__arf_score = arf_score

    def __str__(self):
        values = []
        for value in self.__dict__.values():
            values.append(value)
        print('-' * 50)
        return 'Фамилия: \t\t\t{}\nИмя: \t\t\t\t{}\nОтчество: \t\t\t{}\nНазвание заведения:\t\t{}\nСредняя оценка: \t\t{}'.format(*values)

    def sort(self, other_object):
        self_spisok = self.get_all()
        other_object_spisok = other_object.get_all()
        if self_spisok[0] > other_object_spisok[0]:
            temp = []
            temp.extend(self_spisok)
            temp_arf_score = self.__arf_score
            self.set_all(other_object_spisok)
            self.__arf_score = other_object.__arf_score
            other_object.set_all(temp)
            other_object.__arf_score = temp_arf_score
    
    def compareTo(self, START_LIMIT_ARF_SCORE, END_LIMIT_ARF_SCORE):
        if START_LIMIT_ARF_SCORE < self.__arf_score <= END_LIMIT_ARF_SCORE:
            return True
        return False

def print_result(people):
    for boy in people:
        print(boy)
    if not people:
        print('-' * 50)

def sorted_high(people):
    for i in range(len(people) - 1):
        for j in range(i + 1, len(people)):
            people[i].sort(people[j])
    print_result(people)

class Main:
    FIRST_SYMBOL, NUMBER_STUDENT_TICKET, START_LIMIT_ARF_SCORE, END_LIMIT_ARF_SCORE = 'А', 150, 3.5, 4.5
    students = []
    print()
    for _ in range(int(input('Введите количество студентов: '))):
        print()
        students.append(Student(input('Фамилия студента: '), input('Имя студента: '), input('Отчество студента: '), input('Название заведения: '), 
                                int(input('Номер студенческого билета: '))))
    school_boys = []
    print()
    for _ in range(int(input('Введите количество школьников: '))):
        print()
        school_boys.append(SchoolBoy(input('Фамилия школьника: '), input('Имя школьника: '), input('Отчество школьника: '), input('Название заведения: '), 
                                float(input('Средняя оценка школьника: '))))
    print_result(students)
    print_result(school_boys)
    print('\nПосле сортировки по возрастанию\n')
    sorted_high(students)
    sorted_high(school_boys)
    print('\nПосле сортировки по ограничениям\n')
    for student in students:
        if student.compareTo(FIRST_SYMBOL, NUMBER_STUDENT_TICKET):
            print(student)
    for school_boy in school_boys:
        if school_boy.compareTo(START_LIMIT_ARF_SCORE, END_LIMIT_ARF_SCORE):
            print(school_boy)


