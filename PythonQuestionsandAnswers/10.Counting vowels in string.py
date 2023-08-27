#WAP to count the number of vowels in a given string
string=input('Enter any string:')
count=0
for ch in string:
    if ch in 'aeiouAEIOU':
        count+=1
print('Total number of vowels:',count)