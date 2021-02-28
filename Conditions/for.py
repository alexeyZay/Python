# x=['1','2','3','4','5','6','7']
# for a in x:
#     print(x.__getitem__(1))
#     print('Hi')
# print('Hi')

# x=['1','2','3','4','5','6','7']
# for a in x:
#     print(a) # return an item from list
#     print('Hi')
# print('Hi')
# sum=0
# for a in x:
#     sum=sum+int(a)
#     # sum+=int(a) same but short form
#     if int(a)%2==0:
#         print('{0} is even number'.format(a))
#     else:
#         print('{0} is odd number'.format(a))
# print(sum)

# it works for strings
# list_l='Hello World'
# for char in list_l:
#     print(char)

# it works with tuple
# tup=[('a','b'),('c','d'),('e','f')]
# for t in tup:
#     print(t)
# # if you want to print out individ from tuple use unpack
# for t1,t2 in tup: # defining each element in tuple
#     print(t1,t2)

# it works for dictionary

#dic={'key1':'value1', 'key2':'value2','key3':'value3'}
#for element in dic.items(): # return key and values
#for element in dic.keys(): # return keys
#for element in dic.values(): #return values
#    print(element) # this will return keys by default
# ti print individualy use 'key' and 'value' spec words
# for key,value in dic.items():
#     print(key)
#     print(value)

# func range define the number of iteration that should be done
# for x in range(5):
#     print(x)
#
# # if do not need spec var in 'for' then use '_'
#
# for _ in range(5):
#     print(_)
#     print('some text to show several times')