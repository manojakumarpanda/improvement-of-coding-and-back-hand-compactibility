try:
    x=int(input('Enter a number::'))
    y=int(input('Enter the second number'))
    print('The result of the two number is:',x/y)
except ZeroDivisionError as msg:
    print('The type of the exception is:',type(msg))
    print('The exception class name is',msg.__class__)
    print('The exception  name is',msg.__class__.__name__)
    print('The exception is',msg)
