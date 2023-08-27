#Write a function that takes two lists and returns their intersection(common elements).

def Lists_Intersection(list1,list2):
         for i in range(0,len(list1)):
             for j in range(0,len(list2)):
                 if list1[i]==list2[j]:
                     list3.append(list1[i])
                 else:
                      pass
         return list3


list1=[33,76,21,9,65,70]
list2=[22,76,19,9,126,70]
list3=[]
print(Lists_Intersection(list1,list2))
