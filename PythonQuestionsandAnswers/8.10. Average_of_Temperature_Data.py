import csv
temp_data=[]
sum=0
count=0
averages=[]
with open('C:\\Users\\Lenovo\\Desktop\\bengaluru last7days.csv', 'r') as f1:
    data=csv.reader(f1, delimiter=',')
    skip_header_data=False
    for row in data:
        if not skip_header_data:
            skip_header_data=True
            continue

        temp_data.append((row[1],row[2]))
    for tup in range(0,len(temp_data),23):
       for ele in temp_data[tup:tup+23]:
         sum+=float(ele[1])
         count+=1
       avg=sum/count
       averages.append(avg)
       print('%.4f'%avg)
    print('max avg is:', max('%.4f'%avg for avg in averages))

