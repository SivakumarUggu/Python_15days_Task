#Given a CSV file with employee details (name,age,salary) . Calculate the average salary of all employees.
import csv
with open('C:\\Users\\Lenovo\\Desktop\\Employee_Details.csv','r') as f1:
    content=csv.reader(f1,delimiter=';')
    sum=0
    count=0
    data=[]
    header_skipped=False
    for row in content:
        if not header_skipped:
            header_skipped=True
            continue
        name,age,salary=row
        data.append((name,age,salary))

    for tuple in data:
        salary=tuple[2]
        sum+=int(salary)
        count+=1
    average=(sum/count)
    print(f'Average of salaries is: {average}')
