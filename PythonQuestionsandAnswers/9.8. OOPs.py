#5. Create a class to represent a car with attributes like make,model and year.
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

car1=Car('BMW','sports',2014)
print(car1.make)
print(car1.model)
print(car1.year)
