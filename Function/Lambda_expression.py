#map and filter before lambda
# def sum_of_two_numbers(x):
#     return x+x
#
# some_list=[1,2,3,4,5,6,7,8.88]
#
# print(map(sum_of_two_numbers,some_list))  #return object with type MAP
#
# # one way to print results
# result=map(sum_of_two_numbers,some_list)
# for item in result:
#     print(item)
# # another way to show results
#
# for item in map(sum_of_two_numbers,some_list):
#     print(item)
#
# # one more way to display results is to convert results into list
# print(list(map(sum_of_two_numbers,some_list)))

# def is_a_in_string (string):
#     if 'a' in string:
#         print('String has "a"')
#         return True
#     else:
#         print('Sting has not "a"')
#         return False
#
# list_of_strings=['hi', 'hello','hack','jack']

# def is_number_odd(number):
#     return number%2==1
#
# list_of_numbers=[1,2,3,4,5,6,7]
#
# print(filter(is_number_odd, list_of_numbers)) # return filter object
#
# print(list(filter(is_number_odd,list_of_numbers))) # return odd numbers list
#
# for num in filter(is_number_odd,list_of_numbers):
#     print(num)

# def is_a_in_string (string):
#     if 'a' in string:
#         print('String has "a"')
#         return True
#     else:
#         print('Sting has not "a"')
#         return False
#
# list_of_strings=['hi', 'hello','hack','jack']
#
# print(list(filter(is_a_in_string,list_of_strings)))

#lambda expression

# def cube(number):
#     return number**3

#lambda number:number**3


# number_list=[1,2,3,4,5,6,7]
# #print(list(map(cube,number_list)))
# print(list(map(lambda number:number**3,number_list)))
#
# print(list(filter(lambda odd:odd%2==1,number_list)))
# print(list(filter(lambda odd:odd%2==0,number_list)))

# list_of_strings=['hi', 'hello','hack','jack']
# print(list(map(lambda string:string[-1],list_of_strings)))
# print(list(map(lambda string:string[::-1],list_of_strings))) # развернет строки наоборот