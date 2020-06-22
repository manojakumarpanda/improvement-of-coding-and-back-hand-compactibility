def exception_error():
    try:
        a,b=12,0
        c=a/b
        raise NameError
        
    except ZeroDivisionError as ZDE:
        print('Error:',ZDE)
    finally:
        print('The finally statement executed after except block')

exception_error()
