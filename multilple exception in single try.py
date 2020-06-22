try:
    a=int(input('Enter the first number'))
    b=int(input('Enter the second number'))
    print('The result of the two number is ',a/b)
except ValueError:
    print('Please enter a valid data you have entered a invalid data')
except ZeroDivisionError:
    print('The number cannot be devieded with the zero;')
