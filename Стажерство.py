"""def WriteCity():
    City = []
    for i in range(int(input("Введите количество городов: "))):
        City.append(input())
    return City

def ResultCity(City):
    for i in City:
        if City.index(i) != len(City) - 1:
            print(str(i) + ",", end = " ")
        else:
            print(str(i) + ".")
    pass

City = WriteCity()
ResultCity(City)"""

"""def WriteNumber():
    Number = float(input("Введите число: "))
    return Number

def Proccess(Number):
    #Okryglenie = Number - (Number % 5)
    if Number % 5 >= 2.5:
        Okryglenie = (Number // 5) + 5 * 5
        print(Okryglenie)
    else:
        Okryglenie = int(Number // 5 * 5)
        print(Okryglenie)
    pass

Number = WriteNumber()
Proccess(Number)"""

"""comp = int(input())
co = list(str(comp))
if comp == 1:
	print(str(comp) + " компьютер")
elif comp >= 2 and comp < 5:
	print(str(comp) + " компьютера")
elif comp >= 5 and comp < 21:
	print(str(comp) + " компьютеров")
else:
	if int(co[-1]) == 1:
		print(str(comp) + " компьютер")
	if int(co[-1]) >= 2 and int(co[-1]) < 5:
		print(str(comp) + " компьютера")
	elif int(co[-1]) >= 5 and int(co[-1]) <= 9 or int(co[-1]) == 0:
		print(str(comp) + " компьютеров")"""

"""def WriteNumber():
    Number = int(input())
    return Number

def Proccess(Number):
    CountSymbols = str(Number)
    if Number == 1:
        print(Number, "компьютер")
    elif 2 <= Number <= 4:
        print(Number, "компьютера")
    elif 5 <= Number <= 20:
        print(Number, "компьютеров")
    else:
        if int(CountSymbols[-1]) == 1:
            print(Number, "компьютер")
        if 2 <= int(CountSymbols[-1]) <= 4:
            print(Number, "компьютера")
        if 5 <= int(CountSymbols[-1]) <= 9 or int(CountSymbols[-1]) == 0:
            print(Number, "компьютеров")
    pass

Number = WriteNumber()
Proccess(Number)"""

"""from math import sqrt

a = int(input("Введите число"))

if sqrt(5*(a**2)-4)%1 == 0 or sqrt(5*(a**2)+4)%1 == 0:
	print("True")
else:
	print("False")"""

"""def WriteNumber():
    Number = int(input())
    return Number

def Proccess(Number):
    k = 0
    for i in range(1, Number + 1):
        if Number % i == 0:
            k += 1
    if k == 2:
        print("True")
    else:
        print("False")
    pass

Number = WriteNumber()
Proccess(Number)"""

"""mas1= []
mas2 = []
mas3 = []
c1 = int(input("Укажите сколько чисел в 1 массиве"))
for i in range(c1):
	mas1.append(int(input("Введите числа: ")))
c2 = int(input("Укажите сколько чисел в 2 массиве"))
for i in range(c2):
	mas2.append(int(input("Введите числа: ")))
for i in range(len(mas1)):
	for j in range(len(mas2)):
		if mas1[i] == mas2[j]:
			mas3.append(mas1[i])
mas3 = list(set(mas3)) 
print(mas3, end="")"""

def WriteNumberMassiv():
    Massiv = []
    print("Введиче необходимые числа через пробел")
    Massiv = map(int, input().split())
    return Massiv

def Proccess(Massiv1, Massiv2):
    Massiv, k= [], 1
    for i in Massiv1:
        for j in range(1, len(Massiv1)):
            if i == Massiv1[j]:
                k += 1
        if k < 1:
            break
        for j in Massiv2:
            if i == j:
                k += 1
        if k >= 4:
            if Massiv.count(i) < 1:
                Massiv.append(i)
        k = 0
    Massiv.sort()
    print(Massiv)
    pass

Massiv1 = WriteNumberMassiv()
Massiv2 = WriteNumberMassiv()
Proccess(list(Massiv1), list(Massiv2))