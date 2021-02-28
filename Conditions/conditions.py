# if conditions
# if: should start from the beginig of the line
# executable code should have 'tab' before
# next can be 'elif'
# else at the end this is the filnal condition if other doesn't work
# x = input('enter \'a\'')
# if x == 'a':
#     print('all good')
# else:
#     print('try again')

# !!! in case if 0 => will see an error that cade unreachable  0-is False other numbers are True
# same for empty string '' => False / None / []

# if input('Enter any number') =='7':
#     print('7 is a lucky number! Today is your lucky day!')
# else:
#     print('Thank you! Have a nice day!')

if int(input('Enter an integer number'))%2 ==0:
    print( 'The number is even')
else:
    print('The number is odd')