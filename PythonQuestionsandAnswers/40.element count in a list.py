#Write a python program to count the occurrences of each element in a given list.
list1=[1,3,7,1,3,7,9,7,1,7]
dict={}
for ele in list1:
    if ele in dict:
        dict[ele]+=1
    else:
        dict[ele]=1
print(dict)