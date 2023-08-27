#5. Given a CSV file with employee details (name,position,salary), create a class to represent an employee.
class Employee:
    def __init__(self,Name,Position,Salary):
        self.Name=Name
        self.Position=Position
        self.Salary=Salary
import csv
data=[]
with open('C:\\Users\\Lenovo\\Desktop\\Employee_Details.csv', 'r') as file1:
        content=csv.reader(file1, delimiter=';')
        skip_header=False
        for row in content:
            if not skip_header:
                skip_header=True
            else:
                Name, Position, Salary=row
                data.append((Name, Position, Salary))
        print(data)




employee1=Employee(data[0][0], data[0][1], data[0][1])
employee2=Employee(data[1][0], data[1][1], data[1][2])
print(employee1.Name)
print(employee2.Position)
