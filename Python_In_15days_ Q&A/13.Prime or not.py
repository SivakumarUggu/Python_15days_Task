#WAP to check if a number is prime
def isprime(number): #5
    count=0
    for i in range(1,number+1):  #1,2,3,4,5
        if number%i==0:
            count=count+1
    print(count)
    if count==2:
        return True

number=int(input('enter any number:'))
if isprime(number)==True:
    print('given number is a prime')
else:
    print('given number is not a prime')