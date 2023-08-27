#7.8. Create a function that takes a list of dictionaries and sorts them based on a specified key.

def sorting(data):
    min1=data[0]['age']
    for i in range(1,len(data)):
        if data[i]['age']<data[0]['age']:
            data[i],data[0]=data[0],data[i]
    return data


data=[
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

result=sorting(data)
print(result)