#Create a program that checks if two sets have any elements in common.
def uniqueness(set1,set2):
         for i in set1:
             for j in set2:
                 if i==j:
                     return f'Given sets are not unique'
         return f'Given sets are unique'
set1=[2,7,1,9,3]
set2=[4,0,5,8,3]
result=uniqueness(set1,set2)
print(result)