#Create variables for storing a persons name,age,and average test score.

Name='Ram'
print('Name:',Name)
age=30
print('age:',age)
sum=0
average=0
values_count=0

dict1={'Telugu':89,'kannada':85,'english':83}
for values in dict1.values():
    sum+=values
    values_count+=1
average=sum/values_count
print('average of test scores is:%.4f'%average)