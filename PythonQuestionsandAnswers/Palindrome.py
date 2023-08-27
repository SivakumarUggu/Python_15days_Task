#write a python function to check given string is a palindrome or not
def ispalindrome(string):
    string1=''
    for ch in string:
        string1=ch+string1
    if string1==string:
       print(string,'is a palindrome')
    else:
       print(string,'is not a palindrome)


string='madam'
ispalindrome(string)

string2='python'
ispalindrome(string2)


