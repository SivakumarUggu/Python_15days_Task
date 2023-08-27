#Given a list of words find the word with the maximum length and its length
list1=['cat','monkey','rabbit','lion','tiger']
max_length=0
longest_word=' '

for word in list1:
    current_length=0
    for ch in word:
        current_length+=1
    if current_length>max_length:
        max_length=current_length
        longest_word=word
print("longest word is:",longest_word)
print("maximum length is:",max_length)
