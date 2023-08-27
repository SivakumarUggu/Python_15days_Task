#Write a python program to find the length of the longest word in a sentence.

sentence='Hardwork is the key for success.'
list1=list(map(str,sentence.split()))
print(list1)
Largest_word=sorted(list1,key=len)
print(Largest_word)
result=Largest_word[-1]
print(result)