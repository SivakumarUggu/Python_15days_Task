#Write a program that takes a sentence as input and count the number of words in it.
Sentence='Python is objected oriented programming language.'
list1=list(map(str,Sentence.split()))
print(list1)
count=0
for i in list1:
    count+=1
print(count)