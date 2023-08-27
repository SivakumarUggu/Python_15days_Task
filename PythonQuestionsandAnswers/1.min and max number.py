#write a python program to find out minimum number and maximum number in a list
list1=[34,59,14,9]
max=0
for i in list1:
    if i>max:
        max=i
print(max)

list2=[34,59,14,9]
min=list2[0]
for i in list2:
    if i<min:
        min=i
print(min)