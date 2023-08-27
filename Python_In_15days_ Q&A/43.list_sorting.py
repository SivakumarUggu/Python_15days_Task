#Write a program that checks if a given list is sorted in ascending order.
def islist_ascended(list1):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if len(list1[i])>len(list1[j]):
                return False
    return True

list1=['raj','ravi','arjun']
list2=['arjun','ravi','raj']
list3=['cat','ravi','raj','arjun']
result1=islist_ascended(list1)
result2=islist_ascended(list2)
result3=islist_ascended(list3)
print(result1)
print(result2)
print(result3)