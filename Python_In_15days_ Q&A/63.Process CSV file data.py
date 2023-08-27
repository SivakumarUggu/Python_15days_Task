#Read a csv file and process its data.
import csv
data=[]
file1=open('C:\\Users\\Lenovo\\Desktop\\Sample_CSV_data.csv', 'r')
file_reading=csv.reader(file1, delimiter=';')
header_skipped = False
for row in file_reading:
    if not header_skipped:
        header_skipped=True
        continue

    login_email,identifier,first_name,last_name=row
    data.append((login_email,identifier,first_name,last_name))
print(data)

for email in data:
    print(email[0])