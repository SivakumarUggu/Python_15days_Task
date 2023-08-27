#Given a list of words, count the number of words with more than 5 characters
list1=['grapes','potatos','rank','ring','vegetables','fruits']
count2=0
for name in list1:
    count1=0
    for ch in name:
        count1+=1
    if count1>5:
       count2+=1
print('Total number of words with more than five chars are:',count2)