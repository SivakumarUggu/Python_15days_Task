#Given a list of names, remove all duplicate names and print the unique names.
list1=['raam','ravi','gopal','raam','krish','ravi','raam']
list2=[]
for name in list1:
    if name not in list2:
        list2+=[name]
print(list2)