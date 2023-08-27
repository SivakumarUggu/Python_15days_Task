# Given two sets find the union, intersection and difference between them.
set1={4,2,5,6,9,1}
set2={5,3,7,6,0}
union=set()

#union
for i in set1:
        union.add(i)
for j in set2:
        union.add(j)
print(f'AuB is: {union}')

#Intersection
intersection=set()
for i in set1:
    for j in set2:
        if i==j:
            intersection.add(i)
print(f'A intersection B is: {intersection}')

#Difference
difference=set()
for i in union:
    if i not in intersection:
       difference.add(i)
print(f'diff between Union and Intersection of A and B is: {difference}')




