#Given a list of numbers, create a function to find the sum of all positive numbers
list1=[3.10,-67,0,43.50,-60,54.23,-45,9]
def sum_pos_num(list1) :
    sum=0
    for i in list1:
        if i>0:
            sum=sum+i
    return sum

list1=[3.10,-67,0,43.50,-60,54.23,-45,9]
result=sum_pos_num(list1)
print(int(result))