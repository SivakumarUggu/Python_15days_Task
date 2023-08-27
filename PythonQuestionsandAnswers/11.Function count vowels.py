#write a function to count total number of vowels in a given string.
def Total_vowels(string):
    count=0
    for ch in string:
       if ch in 'aeiouAEIOU':
           count+=1
    return count

string='pythOn@is&Easy!'
result=Total_vowels(string)
print('Total_Vowels in the given string is:',result)