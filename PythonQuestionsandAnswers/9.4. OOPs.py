#4. Create a class to represent a student with attributes like name,age and grades.
class student:
    def __init__(self,name, age, grades):
        self.name=name
        self.age=age
        self.grades=grades

student1=student('Raam',26,9.5)
student2=student('Krish',29,8)

print(student1.name)
print(student1.age)
print(student1.grades,'\n')

print(student2.name)
print(student2.age)
print(student2.grades)




