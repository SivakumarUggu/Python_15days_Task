#Create a function that takes a number as input and prints its multiplication table.
def Mul_Table(Number):
    for i in range(1,11):
        print(Number,'*',i,'=',Number*i)

Number=int(input('Enter any number:'))
print(Mul_Table(Number))
