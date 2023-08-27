#Create a function that takes a list of strings and returns the list
#sorted by the length of the strings.
list1=['raaghav','ravi','krish','arjun','raj']
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if len(list1[i])>len(list1[j]):
            list1[i],list1[j]=list1[j],list1[i]
print(list1)