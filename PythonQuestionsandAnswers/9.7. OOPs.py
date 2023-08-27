#4. Write a python program that uses a rectangle class to calculate the area and perimeter of a rectangle.
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return (self.length*self.breadth)

    def perimeter(self):
        return 2*(self.length+self.breadth)

rect1=Rectangle(10,8)
print(rect1.area())
print(rect1.perimeter())