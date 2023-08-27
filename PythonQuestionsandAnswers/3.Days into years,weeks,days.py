#write a program that converts a given number of days into years,weeks,days
Total_days=int(input('Enter total number of days:'))
years=Total_days//365
weeks=(Total_days%365)//7
days=(Total_days%365)%7
print('years:',years)
print('weeks:',weeks)
print('days:',days)