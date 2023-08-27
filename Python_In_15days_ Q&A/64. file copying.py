#Write a python program to copy the contents of one text file into another.
import csv
data=[]
file1=open('student_data.csv','r')
file2=open('abc.txt','w')
data_reading=csv.reader(file1)
for row in data_reading:
    file2.write(str(row))
    file2.write('\n')
file1.close()
file2.close()
