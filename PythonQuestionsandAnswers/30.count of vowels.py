#Write a function to count the number of vowels in a given string.
def Vowels_Count(String):
    count=0
    for i in String:
        if i in 'aeiouAEIOU':
            count=count+1
    return f'Total count of vowels in a given string {String} is: {count}'


String='RaamRahimJesus'
print(Vowels_Count(String))