#Write a program that calculates the factorial of a given number
Number=int(input('Enter any number:'))
fac=1
for i in range(1,Number+1):
    fac=fac*i
print(fac)