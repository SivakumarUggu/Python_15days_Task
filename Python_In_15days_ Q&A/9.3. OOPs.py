#3.Define a class for a circle with methods to calculate its area and circumference.
class circle:
    def __init__(self,pi,r):
        self.pi=pi
        self.r=r
    def area(self):
        return (self.pi*self.r**2)

    def circumference(self):
        return (2*self.pi*self.r)


result=circle(3.14,3)
print(result.area())
print(result.circumference())



