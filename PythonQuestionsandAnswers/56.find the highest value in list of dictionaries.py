#Given a list of dictionaries, find the dictionary with the highest value for a specific key.
list=[{'a':25,'b':21},{'c':13,'d':43},{'e':58,'f':498,'g':100}]
max=0
for ele in list:
    print(max)
    for key,value in ele.items():
        print(key,value)
        if value>max:
            max=value
print(ele)
