#Implement a function that checks if a given string is a pangram. (contains all letters of the alphabet)
Alphabet='abcdefghijklmnopqrstuvwxyz'
String='Hello, World!'
String2=''
for i in String:
    if i in Alphabet:
        String2+=i

if String2==Alphabet:
    print('Given input is a Pangram')
else:
    print('Given input is not a pangram')