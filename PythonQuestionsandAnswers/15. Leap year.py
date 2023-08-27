#WAP that takes a year as a input and checks if it is a leap year or not
year=int(input('Enter any year:'))
if year%400==0 and year%100==0:
    print(year,'is a leap year')
elif year%4==0 and year%100!=0:
    print(year,'is a leap year')
else:
    print(year,'is not a leap year')