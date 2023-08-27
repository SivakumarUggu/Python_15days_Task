#Create a program that generates the Fibonacci sequence up to a given number of terms.
Terms=int(input('Enter total number of terms: '))
a=0
b=1
print(a,end=' ')
print(b,end=' ')
for i in range(1,Terms+1):
    next_val=a+b
    print(next_val,end=' ')
    a,b=b,next_val