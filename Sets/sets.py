# new_set = {'blue', 'green', 'yelow', 'grey', 'orange'}
# # print(new_set)
# # print(type(new_set))
#
# # actions with set
# # add items from the tuple and from the list
# t_tuple = (1, 2, 3)
# l_list = ['aa', 'cc', 'bb', 'cc']
#
# set_from_list = set(l_list)
# set_from_tuple = set(t_tuple)
#
# # empty set
# empty_set = set()
# # print(empty_set)
# # print(type(empty_set))
# #
# print(type(set_from_tuple))
# # print(set_from_list)
# # print(type(t_tuple))
# # print(type(l_list))
#
# # adding items to set
#
# set_from_list.add('hello')
# print(set_from_list)      # no duplicates because it does not support duplicates
#
# # removing items form set
#
# #removing by pop
# set_from_list.pop() # deleting one element 'pop' in this case
# print(set_from_list)
#
# #delete by remove
# # set_from_list.remove('cc')  #
# # print(set_from_list)
#
# # set_from_list.remove('aa')  # when deleted by remove and there is no item to delete than you will see an error message
# # print(l_list)
#
# set_from_list.discard('DD')  #
# print(set_from_list)
#
# #DELETE all the data
# set_from_list.clear()
# print(set_from_list)
print( 'a' > 'A' )
# ord() return the code of the character
print(ord('a'),ord('A'))