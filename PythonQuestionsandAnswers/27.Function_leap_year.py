#Implement a function to check if a given year is a leap year or not
def is_leap_year(year):
    if year%400==0 and year%100==0:
        return f'Given year {year} is a Leap Year.'
    elif year%4==0 and year%100!=0:
        return f'Given year {year} is a Leap Year.'
    else:
        return f'Given year {year} is not a Leap Year'

year=int(input('Enter any year:'))
print(is_leap_year(year))