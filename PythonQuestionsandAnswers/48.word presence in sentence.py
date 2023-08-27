#Implement a program that takes a sentence and a word as input and checks
#if the word is present in the sentence.
def word_presence(sentence,word):
    list1=list(map(str,sentence.split()))
    if word in list1:
        return f'word is present in the sentencce'
    else:
        return f'word is not present in the sentence'

sentence='Coding requires analytical skills.'
word='skills.'
result=word_presence(sentence,word)
print(result)