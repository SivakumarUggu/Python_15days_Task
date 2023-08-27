#Create a program that finds the common elements between two lists and stores them in a new list.
list1=[4,7,1,9,6]
list2=[1,4,8,6]
list3=[]
for ele in list1:
    if ele in list2:
        list3.append(ele)
print(list3)