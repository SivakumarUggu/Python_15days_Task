#8. Implement a program that uses a circle class to calculate the area and circumference of multiple circles.
import math
class Circle:
    def __init__(self,radius):
        self.pi=math.pi
        self.radius=radius

    def area(self):
        return (self.pi*self.radius**2)

    def circumference(self):
        return (2*self.pi*self.radius)

circle1=Circle(4)
circle2=Circle(6)
print('%.4f' %circle1.area())
print('%.4f' %circle1.circumference())

print('%.4f' %circle2.area())
print('%.4f' %circle2.circumference())