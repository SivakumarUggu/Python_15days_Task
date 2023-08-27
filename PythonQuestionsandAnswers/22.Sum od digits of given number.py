#Calculate the sum of digits of a given number
Number=int(input('Enter any number:'))
sum=0
while(Number>0):
    digit=Number%10
    sum+=digit
    Number=Number//10
print('sum of all digits of a given number is:',sum)