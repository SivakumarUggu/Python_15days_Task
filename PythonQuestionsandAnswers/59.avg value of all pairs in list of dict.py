#Write a program that finds the average value of all the elements in a list of dictionaries.
list=[{'a':10,'b':7},{'c':6,'d':2,'e':4},{'f':3,'g':4}]
sum=0
count=0
for dict in list:
    for value in dict.values():
        sum+=value
        count+=1
    average=(sum/count)
print('average is %.4f'%average)