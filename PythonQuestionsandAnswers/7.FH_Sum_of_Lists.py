# 8.7.Given a text file with a list of numbers, write a function that finds the sum of all numbers in the file.
import ast
def sum_of_list():
    sum=0
    with open('8.7.list of numbers', 'r') as f1:
        content=f1.read()
        list1= ast.literal_eval(content)
        for ele in list1:
            sum+=ele
        return f'Sum of list of numbers is: {sum}'

result=sum_of_list()
print(result)
