#Given a string, write a function to remove all vowels from it and return the modified string!
String='Elephant is bigger but lion is king.'
def Vowel_Removal(String):
    result=''
    for ch in String:
        if ch not in 'aeiouAEIOU':
            result+=ch
    return result

String='Elephant is bigger but lion is king.'
print(Vowel_Removal(String))