#Write a python program that counts the number of occurrences of each character
#in a given string using a dictionary.
String=input('Enter any string:')
dict={}
for ch in String:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
print(dict)
