from math import pi
from random import uniform

class CapacityFigura:

    def __init__(self, radius):
        self.radius = radius

class Ball(CapacityFigura):

    def compute_area(self):
        self.area = 4 * pi * self.radius ** 2

    def compute_capacity_figura(self):
        self.capacity = 4/3 * pi * self.radius ** 3

    def exist_figura(self):
        return True if self.radius > 0 else False
    
    def toString(self):
        if self.exist_figura():
            self.compute_area()
            self.compute_capacity_figura()
            return f'Радиус шара: {round(self.radius, 3):6f}, Объём шара: {round(self.capacity, 3):12f}, Площадь поверхности: {round(self.area, 3):12f}'
        return f'Шар не существует'

class BallSector(CapacityFigura):

    def __init__(self, height, radius):
        super().__init__(radius=radius)
        self.height = height

    def compute_area(self):
        self.area = 1/2 * self.radius * self.height

    def compute_capacity_figura(self):
        self.capacity = 2/3 * pi * (self.radius ** 2) * self.height

    def exist_figura(self):
        return True if self.radius and self.height > 0 else False

    def toString(self):
        if self.exist_figura():
            self.compute_area()
            self.compute_capacity_figura()
            return f'Радиус сектора: {round(self.radius, 3):6f}, Объём сектора: {round(self.capacity, 3):12f}, Площадь сектора: {round(self.area, 3):12f}'
        return f'Шар не существует'
        
class main:
    print()
    count_ball, count_ball_sector = int(input('Введите количество шаров: ')), int(input('Введите количество секторов: '))
    print()
    balls = []
    for _ in range(count_ball):
        balls.append(Ball(radius=uniform(0, 10)))
    for _ in range(count_ball_sector):
        balls.append(BallSector(height=uniform(0, 10), radius=uniform(0, 10)))
    for object in balls:
        print(object.toString())
    print()