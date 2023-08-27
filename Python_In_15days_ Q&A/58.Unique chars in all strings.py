#Implement a function that takes a list of strings and returns a set of
#unique characters present in all strings.
def unique_chars(list):
    dict={}
    for string in list:
        dict[string]=' '
        for ch in string:
            if ch not in dict[string]:
                dict[string]+=ch
            else:
                continue
    return dict

list=['geeks','wool','madam','jinni']
result=unique_chars(list)
print(result)