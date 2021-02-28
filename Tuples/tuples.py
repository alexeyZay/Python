# # tuple immutable if you ctreted it it can't be changed : name=(element1,element2)  it is possible  name=element1,element2
#
# tuple_1 = ('hello',12)
# tuple_2=(11,12.1)
#
# print(tuple_1,tuple_2)
#
# # print(tuple_1[0]) # error you can't change the value
#
# new_tuple=('hi',tuple_1[1])
# print(new_tuple)
#
# # multiple assignment
# x,y,z=1,2,3
# print(x,y,z)
#
# # assign all items of tuple to variables
# a,s=tuple_1 # in this case each variable gets values from tuple
# print(a,s)

# printing count of items based on some value
# tup = (1, 2, 3, 4, 5, 5)
# tup_string = ('a', 'vb', 'sd')
# print(tup.count(5))
# print(tup_string.count('vb'))
#
# print(tup.index(2))  # will return the index of '3'
# print(tup_string.index('vb'))  # will return the index of 'vb'

tup_pc = ('win', '16Gb', 'amd')
os, ram, cpu = tup_pc
print(os, ram, cpu)
