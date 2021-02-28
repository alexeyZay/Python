# # simple list with diffrent types
number_list = [32,'test',11.11]
# print(number_list)
# # number of items
# print(len(number_list))
#
# # list can be updated
# number_list[0]='updated'
# print(number_list)

#concatination
new_list = number_list+list('test')
#new_list2 = number_list+new_list
# print(f'{new_list}\n{number_list}\n{new_list2}')
#
# # adding new item to list
# new_list.append('added to the end')
# print(new_list)
#
# new_list.insert(0,'inserted to start')
# print(new_list)

# remove items by using 'pop' method deleted by index
#
# print(new_list)
# new = new_list.pop() # без параметра удаляет последний элемент в списке
# when you assign 'pop' method result to variable it return deleted item to this variable
# print(new_list)
# print(new)

# remove items by key 'remove' it removes by key first value that were found
# new = new_list.remove('s') # remopve will not return the value it just removing the item based on key (print will return NONE)
# print(new_list)
# print(new)
#
# # 'sort'
# new_list.pop(0)
# new_list.pop(1)
# new_list.sort()
#
# print(new_list)
# # append can work with other lists
# new_list.append(new_list2)
print(new_list)
t1=new_list[:3] #работает слайсинг
#t1=[new_list.pop(0),new_list.pop(1),new_list.pop(2)]
print(t1)
# t1.insert(1,new_list.pop(0))
# print(t1)