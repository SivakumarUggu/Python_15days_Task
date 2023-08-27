#7. Write a program that uses a person class to keep track of a person's name,age and address.
class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def display_info(self):
        print(f'name is: {self.name}')
        print(f'age is: {self.age}')
        print(f'address is:  {self.address}')

person1=Person('Gopal',33,'123, schipol,BE')
person2=Person('Doe',26,'456,Zaventum,BE')

person1.display_info()
person2.display_info()
