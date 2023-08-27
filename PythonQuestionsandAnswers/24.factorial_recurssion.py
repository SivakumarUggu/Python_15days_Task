#Implement a function that returns the factorial of a given number using recursion.
def fact(Number):
    if Number<=0:
        return 0
    elif Number==1:
        return 1
    else:
       return (Number * fact(Number-1))

Number=4
result=fact(Number)
print(f'The factorial of a given {Number} is: {result}')