#1. Create a class to represent a basic calculator with add, subtract,multiply and divide methods.

class calculator:
    def add(self,num1,num2):
        return num1+num2
    def sub(self,num1,num2):
        return num1-num2
    def mult(self,num1,num2):
        return num1*num2
    def div(self,num1,num2):
        if num2!=0:
            return num1/num2
        else:
            raise ValueError('Can not divide by zero.')

calcy=calculator()

sum=calcy.add(4,6)
subtract=calcy.sub(6,4)
mul=calcy.mult(5,5)
divide=calcy.div(9,3)

print('sum is:', sum)
print('subtract is:', subtract)
print('multiplication is:', mul)
print('division is: %.2f'%divide)





