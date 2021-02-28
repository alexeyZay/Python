# printing with int inside

name = 'alex'
age = 23
# print(name + ' ' + 'is' + ' ' + str(age) + ' ' + 'years old')

# using {} when printing
print('{0} is {1} years old'.format(name,age))
print('{0} is {1} years old'.format('alex',23))

# using new fromat for formatring string
print(f'{name} is {age} years old')

# ordering in formating string
print('{a} is {b} years old'.format(a='alex',b=23)) #this can be used when alot of items but not ordered

 # formating the numbers   number:numberOfdigits.numberOfDigitsAferDot f
float_number=1234.11232
print(f'{float_number:5.2f}')

print(f'{0:10.2f}'.format(float_number))

f1=123.43124
f2=344.45749857
f3=45897.232
f4=123.43124
f5=344.45749857
f6=45897.232
f7=123.43124
f8=344.45749857
print('''
{0:15.4f} {1:15.4f} {2:15.4f} {3:15.4f}
{4:15.4f} {5:15.4f} {6:15.4f} {7:15.4f}'''.format(f1,f2,f3,f4,f5,f6,f7,f8))