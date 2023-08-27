#Given a CSV file with student names and scores, find the student with the highest score.
import csv
data=[]
file1=open('student_data.csv','r')
reader=csv.reader(file1)
for row in reader:
    student, score=row
    data.append((student, int(score)))
print(data)
file1.close()

max_score=0
for student, score in data:
    if score>max_score:
        max_score=score
print(max_score)
print(student)