class Counterfoil:

    def __init__(self, data, summa):
        self.__data = data
        self.__summa = summa

    def get_data(self):
        return self.__data

    def get_summa(self):
        return self.__summa

class CounterfoilForElectricalEnergy(Counterfoil):

    def __init__(self, *args, wasted_electical_energy):
        super().__init__(*args)
        self.__wasted_electical_energy = wasted_electical_energy

    def __lt__(self, other_object):
        return self.get_data() < other_object.get_data()

    def __str__(self):
        return f'{super().get_data()} {super().get_summa()} {self.__wasted_electical_energy}'

    def compare(self, END_LIMIt_SUMMA):
        return self.__str__() if super().get_summa() <= END_LIMIt_SUMMA else None

    
class CounterfoilForHotWaterSupply(Counterfoil):

    def __init__(self, *args, wasted_water):
        super().__init__(*args)
        self.__wasted_water = wasted_water

    def __lt__(self, other_object):
        return self.get_summa() < other_object.get_summa()

    def __str__(self):
        return f'{super().get_data()} {super().get_summa()} {self.__wasted_water}'

def print_on_screen(objects, title):
    print(f'\n{title}') if objects != [] else '\n'
    for object in objects:
        print(object)

def print_on_screen_limit(objects, title, END_LIMIT_SUMMA):
    print(f'\n{title}') if objects != [] else '\n'
    for object in objects:
        object.compare(END_LIMIT_SUMMA)

class main:
    print()
    END_LIMIT_SUMMA = 1500
    count_counterfoil_for_electrical_energy = int(input('Введите количество объектов "Квитанции за электроэнергию": '))
    count_counterfoil_for_hot_water_supply = int(input('Введите количество объектов "Квитанции за горячее водоснабжение": '))
    counterfoil_for_electrical_energys, counterfoil_for_hot_water_supplys = [], []
    for _ in range(count_counterfoil_for_electrical_energy):
        counterfoil_for_electrical_energys.append(CounterfoilForElectricalEnergy(input('Дата оплаты: '), float(input('Сумма оплаты: ')), wasted_electical_energy=int(input('Потрачено электроэнергии: '))))
        print()
    for _ in range(count_counterfoil_for_hot_water_supply):
        counterfoil_for_hot_water_supplys.append(CounterfoilForHotWaterSupply(input('Дата оплаты: '), float(input('Сумма оплаты: ')), wasted_water=int(input('Потрачено воды: '))))
        print()
    for object in counterfoil_for_electrical_energys:
        print(object)
    counterfoil_for_electrical_energys.sort()
    counterfoil_for_hot_water_supplys.sort()
    print_on_screen(objects=counterfoil_for_electrical_energys, title='Отсортированные объекты "Квитанции за электроэнергию" по датам')
    print_on_screen(objects=counterfoil_for_hot_water_supplys, title='Отсортированные объекты "Квитанции за горячее водоснабжение по суммам"')
    print_on_screen_limit(objects=counterfoil_for_electrical_energys, title=f'Перечень объектов "Квитанции за электроэнергию" сумма которых не более {END_LIMIT_SUMMA} руб.', END_LIMIT_SUMMA=END_LIMIT_SUMMA)
    # print_on_screen_limit(objects=counterfoil_for_hot_water_supplys, title=f'Перечень объектов "Квитанции за горячее водоснабжение по суммам"')
