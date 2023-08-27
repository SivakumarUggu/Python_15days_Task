# write a python program to find out minimum number and maximum number in a list
# list1=[34,59,14,9]
# max=0
# for i in list1:
#     if i>max:
#         max=i
# print(max)
#
# list2=[34,59,14,9]
# min=list2[0]
# for i in list2:
#     if i<min:
#         min=i
# print(min)

# -------------------------------------------------------
# calculate the compound interest of given principal(p),time period(t), and interest(I)
# P=float(input('enter principal:'))
# T=float(input('enter time period:'))
# R=float(input('enter rate of interest:'))
# N=float(input('enter the number of times interest compounded per year:'))
# Amount=P*(1+(R/N))**(N*T)
# print('total amount is: %.4f'%Amount)
# CI=Amount-P
# print('Compound interest(CI) is: %.4f'%CI)
# ---------------------------------------------------------------------------------------

# write a program that converts a given number of days into years,weeks,days
# Total_days=int(input('Enter total number of days:'))
# years=Total_days//365
# weeks=(Total_days%365)//7
# days=(Total_days%365)%7
# print('years:',years)
# print('weeks:',weeks)
# print('days:',days)
# -----------------------------------------------------------------------------------------
# Given a list of integers, find the sum of all positive numbers.

# -------------------------------------------------------------------------------------------
# Create a program that takes a sentence as input and counts the number of words in it.
# ---------------------------------------------------------------------------------------------
# implement a program that swaps the values of two variables.
# a=30
# b=50
# print('Initially values of a,b is:',a,b)
# a,b=b,a
# print('After swapping values of a,b is:',a,b)

# ----------------------------------------------------------------------------------------
# 1. Create variables for storing a persons name,age,and average test score.

# Name='Ram'
# print('Name:',Name)
# age=30
# print('age:',age)
# sum=0
# average=0
# values_count=0
#
# dict1={'Telugu':89,'kannada':85,'english':83}
# for values in dict1.values():
#     sum+=values
#     values_count+=1
# average=sum/values_count
# print('average of test scores is:%.4f'%average)
# ------------------------------------------------------------------------------------------------
# 2. Concatenate two strings and print the result
# str1=input('enter any string1:')
# print('string1 is:', str1)
# str2=input('enter any string2:')
# print('string2 is:',str2)
# after_concatenation=str1+str2
# print('after concatenation:', after_concatenation)

# -------------------------------------------------------------------------------------------------
# 3. Create a list of fruits and access elements using indexing.
# list1=['apple','orange','grapes','bananas','mangoes']
# print(list1[0])
# print(list1[-1])
# print(list1[0::2])
# print(list1[:3:1])
# print(list1[-2:-4:-1])
# print(list1[2:4:-1])
# print(list1[-2:-4:1])
# print(list1[2::-2])
# print(list1[::-1])

# ------------------------------------------------------------------------------------------------
# 4. Given a list of names concatenate them into a single string seperated by spaces
# list1=['prakash','kiran','raam','rahim','sandy']
# string=''
# for name in list1:
#     string=string+name+' '
# print(string)
# ----------------------------------------------------------------------------------
# 5. WAP that converts a given number of minutes into hours and minutes
# Total_minutes = int(input('Enter total number of minutes:'))
# Hours = Total_minutes // 60
# Minutes = (Total_minutes % 60)
# print('Total_Hours:', Hours)
# print('Total_Minutes:', Minutes)
#----------------------------------------------------------------------------------------
#6. WAP to count the number of vowels in a given string
# string=input('Enter any string:')
# count=0
# for ch in string:
#     if ch in 'aeiouAEIOU':
#         count+=1
# print('Total number of vowels:',count)

#write a function to count total number of vowels in a given string.
# def Total_vowels(string):
#     count=0
#     for ch in string:
#        if ch in 'aeiouAEIOU':
#            count+=1
#     return count
#
# string='pythOn@is&Easy!'
# result=Total_vowels(string)
# print('Total_Vowels in the given string is:',result)

#---------------------------------------------------------------------------
#1. WAP to check if a given string is pangram or not
# string="The quick brown fox jumps over the lazy Dog"
# count=0
# unique_chars=set(string.lower())
# print(unique_chars)
# for ch in unique_chars:
#     count=count+1
# if count==26:
#   print('given string is a Pangram')
# else:
#   print('given string is not a pangram')

                     #OR

#function Defination
# def ispangram(string):
#     Alphabet='abcdefghijklmnopqrstuvwxyz'
#     for ch in Alphabet:
#          if ch not in string:
#                return False
#     return True
#
# #Driver Code
# string="the quick brown fox jumps over the lazy dog"
# if (ispangram(string)==True):
#     print('given string is a pangram')
# else:
#     print('given string is not a pangram')

#-------------------------------------------------------------------------------
#WAP to check if a number is prime
# def isprime(number): #5
#     count=0
#     for i in range(1,number+1):  #1,2,3,4,5
#         if number%i==0:
#             count=count+1
#     print(count)
#     if count==2:
#         return True
#
# number=int(input('enter any number:'))
# if isprime(number)==True:
#     print('given number is a prime')
# else:
#     print('given number is not a prime')

#-------------------------------------------------------------------------
#Create a loop that prints the first 10 even numbers
# count=0
# for i in range(2,100):
#     if i%2==0:
#         print(i,end=' ')
#         count=count+1
#     if count==10:
#         print('\ncount of even numbers:',count)
#         break

#-------------------------------------------------------------------------
#WAP that takes a year as a input and checks if it is a leap year or not
# year=int(input('Enter any year:'))
# if year%400==0 and year%100==0:
#     print(year,'is a leap year')
# elif year%4==0 and year%100!=0:
#     print(year,'is a leap year')
# else:
#     print(year,'is not a leap year')

#----------------------------------------------------------------------------
#Create a program that generates the Fibonacci sequence up to a given number of terms.
#Terms=int(input('Enter total number of terms: '))
# a=0
# b=1
# print(a,end=' ')
# print(b,end=' ')
# for i in range(1,Terms+1):
#     next_val=a+b
#     print(next_val,end=' ')
#     a,b=b,next_val
#----------------------------------------------------------------------------
#Given a list of names, print all names starting with the letter 'A'
# list1=['Aakash','raamu','john','Aadya','Anand']
# for name in list1:
#     if name[0].upper()=='A':
#         print(name)
#------------------------------------------------------------------------------
#Write a program that prints multiplication table of a given number
# for Number in range(1,21):
#     for i in range(1,11):
#          print(Number,'*',i,'=',Number*i)
#     print()
#------------------------------------------------------------------------------
#Write a program that calculates the factorial of a given number
# Number=int(input('Enter any number:'))
# fac=1
# for i in range(1,Number+1):
#     fac=fac*i
# print(fac)
#------------------------------------------------------------------------------
#Create a loop that prints all prime numbers between 1 and 50.
# count2=0
# for number in range(1,51):
#     count1=0
#     for i in range(1,number+1):
#          if number%i==0:
#              count1+=1
#     if count1==2:
#        print(number,end=' ')
#        count2+=1
# print('\nTotal number of prime numbers are:',count2)

#-------------------------------------------------------------------------
#Given a list of words, count the number of words with more than 5 characters
# list1=['grapes','potatos','rank','ring','vegetables','fruits']
# count2=0
# for name in list1:
#     count1=0
#     for ch in name:
#         count1+=1
#     if count1>5:
#        count2+=1
# print('Total number of words with more than five chars are:',count2)
#----------------------------------------------------------------------------------------
#Calculate the sum of digits of a given number
# Number=int(input('Enter any number:'))
# sum=0
# while(Number>0):
#     digit=Number%10
#     sum+=digit
#     Number=Number//10
# print('sum of all digits of a given number is:',sum)
#----------------------------------------------------------------------------------------
#Implement a function that reverses a given string
#
#------------------------------------------------------------------------------------
#Given a list of numbers, create a function to find the sum of all positive numbers
#list1=[3.10,-67,0,43.50,-60,54.23,-45,9]
# def sum_pos_num(list1) :
#     sum=0
#     for i in list1:
#         if i>0:
#             sum=sum+i
#     return sum
#
# list1=[3.10,-67,0,43.50,-60,54.23,-45,9]
# result=sum_pos_num(list1)
# print(int(result))

#---------------------------------------------------------------------
#Implement a function that returns the factorial of a given number using recursion.
# def fact(Number):
#     if Number<=0:
#         return 0
#     elif Number==1:
#         return 1
#     else:
#        return (Number * fact(Number-1))
#
# Number=4
# result=fact(Number)
# print(f'The factorial of a given {Number} is: {result}')

#----------------------------------------------------------------------------
#Create a function to find the square of each element in a given list

#-----------------------------------------------------------------------------
#Write a function to check if a number is even or odd and return
# "Even" or "Odd" accordingly.
# def even_odd(Number):
#     if Number>0:
#         if Number%2==0:
#             return 'Even'
#         else:
#             return 'Odd'
#
# Number=int(input('Enter any number:'))
# result=even_odd(Number)
# print(f'Entered number {Number} is {result}.')

#------------------------------------------------------------------------------------
#Create a function that takes a list of strings and returns the list sorted alphabetically.
#list1=['Sanscrit','Hindhi','English','Maths','Science','Social']
# def list_sorting(list1):
#     for i in range(0,len(list1)):
#         for j in range(i + 1,len(list1)):
#             if list1[i]>list1[j]:
#                 list1[i],list1[j]=list1[j],list1[i]
#     return list1
#
# list1=['Sanscrit','Hindhi','English','Maths','Science','Social']
# result=list_sorting(list1)
# print(result)

#------------------------------------------------------------------------------------------------
#Implement a function to check if a given year is a leap year or not
# def is_leap_year(year):
#     if year%400==0 and year%100==0:
#         return f'Given year {year} is a Leap Year.'
#     elif year%4==0 and year%100!=0:
#         return f'Given year {year} is a Leap Year.'
#     else:
#         return f'Given year {year} is not a Leap Year'
#
# year=int(input('Enter any year:'))
# print(is_leap_year(year))

#---------------------------------------------------------------------------------------------
#Create a function that takes a number as input and prints its multiplication table.
# def Mul_Table(Number):
#     for i in range(1,11):
#         print(Number,'*',i,'=',Number*i)
#
# Number=int(input('Enter any number:'))
# print(Mul_Table(Number))

#--------------------------------------------------------------------------------------------------
#Write a function that takes two lists and returns their intersection(common elements).

# def Lists_Intersection(list1,list2):
#          for i in range(0,len(list1)):
#              for j in range(0,len(list2)):
#                  if list1[i]==list2[j]:
#                      list3.append(list1[i])
#                  else:
#                       pass
#          return list3
#
#
# list1=[33,76,21,9,65,70]
# list2=[22,76,19,9,126,70]
# list3=[]
# print(Lists_Intersection(list1,list2))

#-----------------------------------------------------------------------------------
#Write a function to count the number of vowels in a given string.
# def Vowels_Count(String):
#     count=0
#     for i in String:
#         if i in 'aeiouAEIOU':
#             count=count+1
#     return f'Total count of vowels in a given string {String} is: {count}'
#
#
# String='RaamRahimJesus'
# print(Vowels_Count(String))

#---------------------------------------------------------------------------------------
#Write a program that takes a sentence as input and count the number of words in it.
# Sentence='Python is objected oriented programming language.'
# list1=list(map(str,Sentence.split()))
# print(list1)
# count=0
# for i in list1:
#     count+=1
# print(count)

#-------------------------------------------------------------------------------------------
# Implement a function that checks if a given string is a pangram. (contains all letters of the alphabet)
# Alphabet='abcdefghijklmnopqrstuvwxyz'
# String='Hello, World!'
# String2=''
# for i in String:
#     if i in Alphabet:
#         String2+=i
#
# if String2==Alphabet:
#     print('Given input is a Pangram')
# else:
#     print('Given input is not a pangram')

#-------------------------------------------------------------------------------------------
# Given a string, write a function to remove all vowels from it and return the modified string!
# String='Elephant is bigger but lion is king.'
# def Vowel_Removal(String):
#     result=''
#     for ch in String:
#         if ch not in 'aeiouAEIOU':
#             result+=ch
#     return result
#
# String='Elephant is bigger but lion is king.'
# print(Vowel_Removal(String))

#------------------------------------------------------------------------------------------------
#Write a python program to find the length of the longest word in a sentence.

# sentence='Hardwork is the key for success.'
# list1=list(map(str,sentence.split()))
# print(list1)
# Largest_word=sorted(list1,key=len)
# print(Largest_word)
# result=Largest_word[-1]
# print(result)

#----------------------------------------------------------------------------------------------
# #Create a function that takes a sentence as input and returns the sentence in reverese order.
# Sentence='Bengaluru is a beautyful city'
# list1=list(map(str, Sentence.split()))
# list_reversal=list1[::-1]
# result=' '.join(list_reversal)
# print(result)
#------------------------------------------------------------------------------------------------
#1. Given a list of numbers find the sum and average using built in functions.
# from statistics import mean
# list1=[34,21,65,39,56]
# sum_of_numbers=sum(list1)
# print(sum_of_numbers)
# average = mean(list1)
# print(average)
#-----------------------------------------------------------------------------------
#Create a list of fruits and add a new fruit to the list.
# list1=['mango','lemon','orange','grapes']
# new_fruit='kiwi'
# list2=list1+[new_fruit]
# print(list2)
#------------------------------------------------------------------------------------
#Access elements in a tuple using indexing.
#Create a program that finds the common elements between two lists and stores them in a new list.
# list1=[4,7,1,9,6]
# list2=[1,4,8,6]
# list3=[]
# for ele in list1:
#     if ele in list2:
#         list3.append(ele)
# print(list3)
#-----------------------------------------------------------------------------------
#Given a list of words find the word with the maximum length and its length
# list1=['cat','monkey','rabbit','lion','tiger']
# max_length=0
# longest_word=' '
#
# for word in list1:
#     current_length=0
#     for ch in word:
#         current_length+=1
#     if current_length>max_length:
#         max_length=current_length
#         longest_word=word
# print("longest word is:",longest_word)
# print("maximum length is:",max_length)

#------------------------------------------------------------------------------------
# Write a python program to count the occurrences of each element in a given list.
# list1=[1,3,7,1,3,7,9,7,1,7]
# dict={}
# for ele in list1:
#     if ele in dict:
#         dict[ele]+=1
#     else:
#         dict[ele]=1
# print(dict)

#---------------------------------------------------------------------------------------
#Given a list of names, remove all duplicate names and print the unique names.
# list1=['raam','ravi','gopal','raam','krish','ravi','raam']
# list2=[]
# for name in list1:
#     if name not in list2:
#         list2+=[name]
# print(list2)

#-----------------------------------------------------------------------------------------
#Create a function that takes a list of strings and returns the list
# sorted by the length of the strings.
# list1=['raaghav','ravi','krish','arjun','raj']
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if len(list1[i])>len(list1[j]):
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)
#---------------------------------------------------------------------------------------------
#Write a program that checks if a given list is sorted in ascending order.
# def islist_ascended(list1):
#     for i in range(len(list1)):
#         for j in range(i+1,len(list1)):
#             if len(list1[i])>len(list1[j]):
#                 return False
#     return True
#
# list1=['raj','ravi','arjun']
# list2=['arjun','ravi','raj']
# list3=['cat','ravi','raj','arjun']
# result1=islist_ascended(list1)
# result2=islist_ascended(list2)
# result3=islist_ascended(list3)
# print(result1)
# print(result2)
#print(result3)

#----------------------------------------------------------------------------------------------
#Implement a function that takes two lists and returns their union
# (all unique elements from both lists).

# def lists_union(list1,list2):
#     union=[]
#     for ele in list1:
#         if ele not in union:
#             union = union+[ele]
#
#     for ele in list2:
#         if ele not in union:
#             union = union+[ele]
#     return union
#
# list1=[2,6,1,5,9]
# list2=[1,6,7,3,8]
# result=lists_union(list1,list2)
# print(result)
#-------------------------------------------------------------------------------------------------
#Create a function that takes a sentence as input and returns the sentence in reverse order.
# string1='Python is an interpreted programming.'
# string2=''
# for ch in string1:
#     string2=ch+string2
# print(string2)
#----------------------------------------------------------------------------------------------
#Given a list of names, count the number of names that start with a vowel.
# list1=['Jerry','tom','otto','elizabeth','elliot']
# count=0
# for name in list1:
#     if name[0] in 'aeiouAEIOU':
#         count+=1
# print(f'Total number of names starts with vowel are:{count}')
#--------------------------------------------------------------------------------------------------
# Write a function to remove all duplicate characters from a given string.
# def remove_duplicates(string):
#     string2=''
#     for ch in string:
#         if ch not in string2:
#             string2+=ch
#     return string2
#
# string='geeksforgeeks'
# result=remove_duplicates(string)
# print(result)
#----------------------------------------------------------------------------------------------------
#Implement a program that takes a sentence and a word as input and checks
# if the word is present in the sentence.
# def word_presence(sentence,word):
#     list1=list(map(str,sentence.split()))
#     if word in list1:
#         return f'word is present in the sentencce'
#     else:
#         return f'word is not present in the sentence'
#
# sentence='Coding requires analytical skills.'
# word='skills.'
# result=word_presence(sentence,word)
#print(result)
#-----------------------------------------------------------------------------------------------
#Create a dictionary to store information about a person(name,age,address).

# dict={}
# Pairs=int(input('Enter number of pairs you want:'))
# for pair in range(0,Pairs,1):
#     key=input('Enter key:')
#     value=input('Enter value:')
#     dict.update({key:value})
# print(dict)

#--------------------------------------------------------------------------
#Add a new key-value pair to an existing dictionary.
# dict={1:'one',2:'two',3:'three'}
# print(dict)
# dict[4]='four'
# print(dict)
# dict['tinky']='pinky'
# print(dict)
# print(dict.get('tinky'))
# print(dict.get('sony','not found'))

#------------------------------------------------------------------------------
#Create a set of unique numbers from a list of numbers.
# list=[4,6,1,4,3,2,6]
# uniques=set(list)
# print(uniques)

#------------------------------------------------------------------------------
#Given two dictionaries merge them into a single dictionary.
# dict1={1:'one',2:'two',3:'three'}
# dict2={4:'four',5:'five',6:'three'}
# for i in dict2.keys():
#     print(i)
#     dict1[i]=dict2[i]
# print(dict1)

#---------------------------------------------------------------
#Write a program that finds the most frequent element in a list.
# list=[1,4,1,5,1,6,4,4]
# dict={}
# for num in list:
#     if num in dict:
#         dict[num]+=1
#     else:
#         dict[num]=1
# print(dict)
# max=0
# for value in dict.values():
#     if value>max:
#         max=value
# print('maximum count:',max)
# print('Most frequent value',value)

#-------------------------------------------------------------------------------------
# Implement a function that removes key-value pair from a dictionary.
# dict={1:'one',2:'two',3:'three',4:'four'}
# dict2={}
# for key,value in dict.items():
#     if key!=1:
#         dict2[key]=value
# print(dict2)

#-----------------------------------------------------------------------------------
# Create a program that checks if two sets have any elements in common.
# def uniqueness(set1,set2):
#          for i in set1:
#              for j in set2:
#                  if i==j:
#                      return f'Given sets are not unique'
#          return f'Given sets are unique'
# set1=[2,7,1,9,3]
# set2=[4,0,5,8,3]
# result=uniqueness(set1,set2)
# print(result)

#------------------------------------------------------------------------------------------
# Given a list of dictionaries, find the dictionary with the highest value for a specific key.
# list=[{'a':25,'b':21},{'c':13,'d':43},{'e':58,'f':498,'g':100}]
# max=0
# for ele in list:
#     print(max)
#     for key,value in ele.items():
#         print(key,value)
#         if value>max:
#             max=value
# print(ele)

#-----------------------------------------------------------------------------------------------
# Write a python program that counts the number of occurrences of each character
# in a given string using a dictionary.
# String=input('Enter any string:')
# dict={}
# for ch in String:
#     if ch not in dict:
#         dict[ch]=1
#     else:
#         dict[ch]+=1
# print(dict)

#-----------------------------------------------------------------------------------------------
# Implement a function that takes a list of strings and returns a set of
#unique characters present in all strings.
# def unique_chars(list):
#     dict={}
#     for string in list:
#         dict[string]=' '
#         for ch in string:
#             if ch not in dict[string]:
#                 dict[string]+=ch
#             else:
#                 continue
#     return dict
#
# list=['geeks','wool','madam','jinni']
# result=unique_chars(list)
# print(result)

#-----------------------------------------------------------------------------
# Write a program that finds the average value of all the elements in a list of dictionaries.
# list=[{'a':10,'b':7},{'c':6,'d':2,'e':4},{'f':3,'g':4}]
# sum=0
# count=0
# for dict in list:
#     for value in dict.values():
#         sum+=value
#         count+=1
#     average=(sum/count)
# print('average is %.4f'%average)

#---------------------------------------------------------------------------------------
# Write a program that reads a text file and prints its content.
# file1=open('Python_FH','r')
# #print(file1.read())
# for data in file1:
#     print(data)

#------------------------------------------------------------------------------------------
#Given a CSV file with student names and scores, find the student with the highest score.
# import csv
# data=[]
# file1=open('student_data.csv','r')
# reader=csv.reader(file1)
# for row in reader:
#     student, score=row
#     data.append((student, int(score)))
# print(data)
# file1.close()
#
# max_score=0
# for student, score in data:
#     if score>max_score:
#         max_score=score
# print(max_score)
# print(student)

#------------------------------------------------------------------------------------------
# Create a new text file and write some content into it.
# file1=open('abc.txt','w')
# file1.write('Welcome to python file handling.\n')
# file1.write('File Handling is an advanced topic in python.\n')
# file1.write('but easy topic.\n')
# file1.close()

#----------------------------------------------------------------------------------------------
# Read a csv file and process its data.
# import csv
# data=[]
# file1=open('C:\\Users\\Lenovo\\Desktop\\Sample_CSV_data.csv', 'r')
# file_reading=csv.reader(file1, delimiter=';')
# header_skipped = False
# for row in file_reading:
#     if not header_skipped:
#         header_skipped=True
#         continue
#
#     login_email,identifier,first_name,last_name=row
#     data.append((login_email,identifier,first_name,last_name))
# print(data)
#
# for email in data:
#     print(email[0])

#------------------------------------------------------------------------------------
#Write a python program to copy the contents of one text file into another.
# import csv
# data=[]
# file1=open('student_data.csv','r')
# file2=open('abc.txt','w')
# data_reading=csv.reader(file1)
# for row in data_reading:
#     file2.write(str(row))
#     file2.write('\n')
# file1.close()
# file2.close()

#------------------------------------------------------------------------------------
# Implement a program that reads a text file and counts the number of words and lines in it.
# try:
#     with open('Python_FH','r') as file1:
#         lines_count=0
#         words_count=0
#         content=file1.read()
#         lines=content.split('\n')
#         words=content.split()
#         for line in lines:
#                  lines_count+=1
#         print('Total lines are:',lines_count)
#         for word in words:
#              words_count+=1
#         print('Total words are:',words_count)
# except FileNotFoundError:
#         print('file not found')

#--------------------------------------------------------------------------------------
#Create a function that takes a list of sentences and writes them to a new text file
#each on a new line.
# import ast
# def copy_content(file1,file2):
#     try:
#          with open(file1,'r') as f1:
#              content=f1.read()
#              list_strings=ast.literal_eval(content)   #Parse the list
#          with open(file2,'w') as f2:
#              for line in list_strings:
#                    f2.write(line+'\n')
#     except FileNotFoundError:
#            print('file1 not found')
#
# copy_content('Python_FH','abc')

#----------------------------------------------------------------------------------------
#Given a CSV file with employee details (name,age,salary) . Calculate the average salary of all employees.
# import csv
# with open('C:\\Users\\Lenovo\\Desktop\\Employee_Details.csv','r') as f1:
#     content=csv.reader(f1,delimiter=';')
#     sum=0
#     count=0
#     data=[]
#     header_skipped=False
#     for row in content:
#         if not header_skipped:
#             header_skipped=True
#             continue
#         name,age,salary=row
#         data.append((name,age,salary))
#
#     for tuple in data:
#         salary=tuple[2]
#         sum+=int(salary)
#         count+=1
#     average=(sum/count)
#     print(f'Average of salaries is: {average}')

#----------------------------------------------------------------------------------------------------
# Write a program that reads a csv file and finds the total sales revenue
#for a specific product.
# import csv
# list_data=[]
# total_sales=0
# count=0
# with open('C:\\Users\\Lenovo\\Desktop\\Sales_September_2019.csv', 'r') as csv_file:
#         csv_reader = csv.reader(csv_file,delimiter=',')
#         header=next(csv_reader)
#         header_skipped=False
#         for row in csv_reader:
#             if not header_skipped:
#                 header_skipped=True
#                 continue
#
#             #header[1],header[3]=row[1],row[3]
#             list_data.append((row[1],row[3]))
#
#         for product,price in list_data:
#             if product=='USB-C Charging Cable':
#                 count=count+1
#                 total_sales=total_sales+float(price)
#         print(f'Total number of {product} are: {count}')
#         print(f'Total_sales is: ${total_sales}')

#---------------------------------------TO BE CONTINUED----------------------------------------#































































































































































