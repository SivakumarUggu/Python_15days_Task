#Create a function that takes a list of strings and returns the list sorted alphabetically.
list1=['Sanscrit','Hindhi','English','Maths','Science','Social']
def list_sorting(list1):
    for i in range(0,len(list1)):
        for j in range(i + 1,len(list1)):
            if list1[i]>list1[j]:
                list1[i],list1[j]=list1[j],list1[i]
    return list1

list1=['Sanscrit','Hindhi','English','Maths','Science','Social']
result=list_sorting(list1)
print(result)