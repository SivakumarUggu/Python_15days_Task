#WAP to check if a given string is pangram or not
string="The quick brown fox jumps over the lazy Dog"
count=0
unique_chars=set(string.lower())
print(unique_chars)
for ch in unique_chars:
    count=count+1
if count==26:
  print('given string is a Pangram')
else:
  print('given string is not a pangram')

                     OR

function Defination
def ispangram(string):
    Alphabet='abcdefghijklmnopqrstuvwxyz'
    for ch in Alphabet:
         if ch not in string:
               return False
    return True

#Driver Code
string="the quick brown fox jumps over the lazy dog"
if (ispangram(string)==True):
    print('given string is a pangram')
else:
    print('given string is not a pangram')