# number_dict = {'first': 1, 'second': 2, 'third': 3}
# new_dict = {key:value**2 for key, value in number_dict.items()}
# print(new_dict)
#
# digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# new_digits={value:value*2 for value in digits}
# print(new_digits)
#
# new_digits={value:'positive' if value>0 else 'negative' if value<0 else 'zero'
# for value in digits}
# print(new_digits)

#set comprehension

# set_digits = {0, 1, 2, 3, 22, 5, 6, 7, 8, 9}
# print(type(set_digits))
# new_set={value*2 for value in set_digits}
# print(f'{new_set} {type(new_set)}')

set_digits = {0, 1, 2, 3, 22, 5, 6, 7, 8, 9}
new_set={value*2 for value in range(1,11)}
print(f'{new_set} {type(new_set)}')
