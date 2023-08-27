#Create a dictionary to store information about a person(name,age,address).

dict={}
Pairs=int(input('Enter number of pairs you want:'))
for pair in range(0,Pairs,1):
    key=input('Enter key:')
    value=input('Enter value:')
    dict.update({key:value})
print(dict)