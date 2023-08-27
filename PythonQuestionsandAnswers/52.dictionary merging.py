#Given two dictionaries merge them into a single dictionary.
dict1={1:'one',2:'two',3:'three'}
dict2={4:'four',5:'five',6:'three'}
for i in dict2.keys():
    print(i)
    dict1[i]=dict2[i]
print(dict1)