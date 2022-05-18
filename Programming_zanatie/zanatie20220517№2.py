from math import pi
from random import uniform, randint

class Orbit:

    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        self.area = pi * (self.radius ** 2)

    def exist(self):
        if self.radius > 0:
            return True
        return False

    def __str__(self):
        if self.exist():
            self.compute_area()
            return f'Радиус круга: {self.radius:3.3f}, Площадь круга: {self.area:4.3f}'
        return f'Круг не существует'

class Ball(Orbit):

    def compute_area(self):
        self.area = 4 * pi * (self.radius ** 2)

    def compute_capacity(self):
        self.capacity = 4/3 * pi * (self.radius ** 3)

    def __str__(self):
        if super().exist():
            self.compute_area()
            self.compute_capacity()
            return f'Радиус шара: {self.radius:3.3f}, Площадь поверхности шара: {self.area:4.3f}, Объём шара: {self.capacity:4.3f}'
        return f'Шар не существует'

class Towed_target(Ball):

    def __init__(self, radius, height):
        super().__init__(radius=radius)
        self.height = height

    def compute_area(self):
        self.area = pi * (self.radius ** 2)
        self.area += pi * self.radius * self.height

    def compute_capacity(self):
        self.capacity = 1/3 * pi * (self.radius ** 2) * self.height

    def exist(self):
        if self.radius > 0 and self.height > 0:
            return True
        return False

    def __str__(self):
        if self.exist():
            self.compute_area()
            self.compute_capacity()
            return f'Радиус конуса: {self.radius:3.3f}, Высота конуса: {self.height:5.3f}, Площадь поерхности конуса: {self.area:4.3f}, Объём конуса: {self.capacity:4.3f}'
        return f'Конус не существует'

class main:
    print()
    count = int(input('Введите количество фигур: '))
    print()
    objects = []
    
    for _ in range(count):
        match randint(1, 3):
            case 1:
                objects.append(Orbit(radius=uniform(0, 10)))
            case 2:
                objects.append(Ball(radius=uniform(0, 10)))
            case 3:
                objects.append(Towed_target(radius=uniform(0, 10), height=uniform(0, 10)))
    for object in objects:
        print(object)