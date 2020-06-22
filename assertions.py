def substraction(am,pm):
    cm=am-pm
    print('The addition of the two number is {}+{} is={}'.format(am,pm,cm))

am=int(input('Enter the first number::'))
pm=int(input('Enter the second numbaer::'))
print(am<pm)
assert am<pm
raise ('The am value cannot be less then pm')
substraction(am,pm)
