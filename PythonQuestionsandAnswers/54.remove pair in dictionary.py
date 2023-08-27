#Implement a function that removes key-value pair from a dictionary.
dict={1:'one',2:'two',3:'three',4:'four'}
dict2={}
for key,value in dict.items():
    if key!=1:
        dict2[key]=value
print(dict2)