#Write a function to remove all duplicate characters from a given string.
def remove_duplicates(string):
    string2=''
    for ch in string:
        if ch not in string2:
            string2+=ch
    return string2

string='geeksforgeeks'
result=remove_duplicates(string)
print(result)