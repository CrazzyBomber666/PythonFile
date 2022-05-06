matrix = []
matrixx = []
matrixy = []
polex = [int(i) for i in input('Введите размер поля').split()]
pole = [[0 for x in range(polex[0])] for y in range(polex[1])]
qq=[]
kol = int(input())
matrix = [[0 for x in range(2)] for y in range(kol)]
for i in range(kol):
		del qq;
		qq = [int(i) for i in input('Введите строку ').split()]
		for j in range ( len(matrix[i]) ): 
			  matrix[i][j] = qq[j]
print(matrix)

def printMatrix ( matrix ): 
   for i in range ( len(matrix) ): 
      for j in range ( len(matrix[i]) ): 
          print ( "{:4d}".format(matrix[i][j]), end = "" ) 
      print ()
printMatrix(pole)

for i in matrix:
	matrixx.append(i[0] -1)
	matrixy.append(i[1] -1)
print(matrixx)
print(matrixy)
n = 1
try:
	for i in range(kol):
		pole[matrixy[i]][matrixx[i]] = n
		n=n+1
except:
	pole.reverse()
	printMatrix(pole)
pole.reverse()
print(matrix)
print(pole)
printMatrix(pole)

		


























a = []
c = [0,0,0]
i1= 0
i2 = 0
i3 = 0
a = [int(i) for i in input().split()]
if a[1] > a[0] and a[1] < a[2]:
	i2=1
elif a[1] > a[2] and a[1] < a [0]:
	i2 = 1
else:
	i1 = 0 
for i in range(0, len(a)):
	for j in range(0, len(a)):
		c.clear()
		c.append(a[0])
		c.append(a[1])
		c.append(a[2])
		if i == j:
			continue
		c[i] = c[i] - c[j]
		if  c[0] > c[1] and c[0] < c[2] :
			i1 = 1
		elif   c[0] > c[2] and c[0] < c[1]:
			i1 = 1
		else:
			if i1 == 0:
				i1 = 0
		if  c[1] > c[0] and c[1] < c[2]:
			i2 = 1
		elif  c[1] > c[2] and c[1] < c[0]:
			i2 = 1
		else:
			if i2 == 0:
				i2 = 0
		if  c[2] > c[1] and c[2] < c[0]:
			i3 = 1
		elif  c[2] > c[0] and c[2] < c[1]:
			i3 = 1
		else:
			if i3 == 0:
				i3 = 0
		if c[0] == c[1]:
			i1 = 1
			i2 = 1
		if c[0] == c[2]:
			i1 = 1
			i3 = 1
		if c[1] == c[2]:
			i2 = 1
			i3 = 1
		if c[0] == c[1] == c[2]:
			i1= 1
			i2 =1 
			i3 = 1
print("Yes" if i1 == 1 else "NO")
print("Yes" if i2 == 1 else "NO")
print("Yes" if i3 == 1 else "NO")














a = [3,1,2,5,4,7,6,9,0,8]

try:
	print(a.index(3,1)) # ищет индекс числа 3, начиная с 1 индекса
except:
	print("Нет такого")

a.append(11)
print(a,"\n")
a.insert(0,12)# вставил на место индекса 0 число 12 
a[1] = 100 # замена
print(a,"\n")
a.remove(1) # удалет значение из списка
print(a,"\n")
a.pop(1) # delete index number 1 from list a if wtirt pop() then delet last index in list a
print(a,"\n")
print(a[-1])

del a[-1]
print(a.count(5))
print(a.count(2))
print(a.count(7))
print(a,"\n")
a.sort()
print(a,"\n")
print(a,"\n")
num = list(range(1,10))
print(num)
x = all([x > 0 for x in num])
print(x)

ss= [ 1 ,2 ,'qq', 'a'  ]
ss = [str(i) for i in ss]
print(ss)
def factorial(n):
	assert n >= 0, "Такого нет"  #вызов ошибки, если число меньше 0
	if n == 0:
		return 1
	return factorial(n - 1) * n

print(factorial(4), "\n\n")

zz = list(input())
cc = list(input())
print("1" if sorted(zz) == sorted(cc) else "0")

aaa = "33"

if len(aaa) == 2:
	print("2")
else:
	print("0")

matrix = []
qq = []
z = int(input("Сколько строк в матрице "))
x = int(input("Сколько столбцов в матрице "))
matrix = [[0 for x in range(z)] for y in range(x)]
for i in range ( len(matrix) ): 
		del qq;
		qq = [int(i) for i in input('Введите строку ').split()]
		for j in range ( len(matrix[i]) ): 
			  matrix[i][j] = qq[j]
print(matrix)
def printMatrix ( matrix ): 
   for i in range ( len(matrix) ): 
      for j in range ( len(matrix[i]) ): 
          print ( "{:4d}".format(matrix[i][j]), end = "" ) 
      print ()
printMatrix(matrix)

"""
for i in range(z):
	matrix.append([])
	if i> 0:
		print("Строка заполнена")
	for j in range(x):
		a = int(input("Введите значения для 1й строки через ентер"))
		matrix[i].append(a) 
print(matrix)
"""
aa = int(input("Введите кол чисел"))
z = 0
x = []
for i in range(aa):
	e = input()
	if e != z:
		x.append(e)
	z = e
x.sort()
for i in x:
	print(i)

aa = int(input("Введите кол чисел"))
z = set()
x = []
a = []
for i in range(0,aa):
	x.append(int(input())) 
print("\n")
x.sort()
for i in range(aa):
	z.add(x[i])
print(z)
"""
aa = int(input("Введите кол чисел"))
z = set()
x = -1
a = []
for i in range(0,aa):
	z.add(int(input())) 
print("\n")
sorted(z)
for i in z:
	print(z)
"""
qq = int(input())
q1 = []
q2 = []
for i in range(0,qq):
	q1.append(int(input()))
for i in range(qq):
	for j in range (qq):
		try:
			
			if q1[i] == q1[j]:
				if q1[i] == 0:
					continue
					q1[i] = 0
		except:
			print("Ошибка")

print(q1)


	

