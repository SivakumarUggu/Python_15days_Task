#Given a list of names, count the number of names that start with a vowel.
list1=['Jerry','tom','otto','elizabeth','elliot']
count=0
for name in list1:
    if name[0] in 'aeiouAEIOU':
        count+=1
print(f'Total number of names starts with vowel are:{count}')