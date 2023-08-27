#Create a loop that prints the first 10 even numbers
count=0
for i in range(2,100):
    if i%2==0:
        print(i,end=' ')
        count=count+1
    if count==10:
        print('\ncount of even numbers:',count)
        break