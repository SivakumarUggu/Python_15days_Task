#WAP that converts a given number of minutes into hours and minutes
Total_minutes = int(input('Enter total number of minutes:'))
Hours = Total_minutes // 60
Minutes = (Total_minutes % 60)
print('Total_Hours:', Hours)
print('Total_Minutes:', Minutes)