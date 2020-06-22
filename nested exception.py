try:
    print('The outer try block')
    print('The excepction is:',10/0)
    try:
        a=int(input('Enter the first number::'))
        b=int(input('Enter the second number::'))
        print('The result of the two number is ',a/b)
    except ValueError:
        print('The inner exceptions')
        print('Please enter a valid data you have entered a invalid data')
    except ZeroDivisionError:
        pirnt('The exception of inner')
        print('The number cannot be devieded with the zero;')

    finally:
        print('The final block of the inner try')
    print('This is outer try after the inner except:')

except:
    print('This is the outer except block ')

finally:
    print('This is the outer finally block')

print('This is the noraml block of code afert all the try:')
