Create a loop that prints all prime numbers between 1 and 50.
count2=0
for number in range(1,51):
    count1=0
    for i in range(1,number+1):
         if number%i==0:
             count1+=1
    if count1==2:
       print(number,end=' ')
       count2+=1
print('\nTotal number of prime numbers are:',count2)