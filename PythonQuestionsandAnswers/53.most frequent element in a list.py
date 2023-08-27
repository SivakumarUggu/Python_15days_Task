#Write a program that finds the most frequent element in a list.
list=[1,4,1,5,1,6,4,4]
dict={}
for num in list:
    if num in dict:
        dict[num]+=1
    else:
        dict[num]=1
print(dict)
max=0
for value in dict.values():
    if value>max:
        max=value
print('maximum count:',max)
print('Most frequent value',value)