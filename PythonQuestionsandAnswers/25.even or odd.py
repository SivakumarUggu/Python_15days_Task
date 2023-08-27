#Write a function to check if a number is even or odd and return
"Even" or "Odd" accordingly.
def even_odd(Number):
    if Number>0:
        if Number%2==0:
            return 'Even'
        else:
            return 'Odd'

Number=int(input('Enter any number:'))
result=even_odd(Number)
print(f'Entered number {Number} is {result}.')