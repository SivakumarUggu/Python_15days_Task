#Implement a function that takes two lists and returns their union
#(all unique elements from both lists).

def lists_union(list1,list2):
    union=[]
    for ele in list1:
        if ele not in union:
            union = union+[ele]

    for ele in list2:
        if ele not in union:
            union = union+[ele]
    return union

list1=[2,6,1,5,9]
list2=[1,6,7,3,8]
result=lists_union(list1,list2)
print(result)