# # range range(number of items(or first item if there is next number fter',',last number,step)
# for x in range(5): #
#     print(x)    #0-4

# for x in range(2,10):
#     print(x) #2-9

# for x in range(1,10,2):
#     print(x) #1.3.5.7.9

# print(range(5)) # return the object range range(0,5)
# print(list(range(5))) # return the list of (5) range items  [0,1,2,3,4]


# index of items in string

# letter_index = 0
# my_string = "hello"
# for letter in my_string:
#     print(letter+" with index "+str(letter_index))
#     letter_index+=1
#
# # index of item by using enumerate
# for letter in enumerate(my_string):
#     print(letter)
#     letter_index+=1
#
# for index,letter in enumerate(my_string):             #unpack tuple items index,letter
#     print(letter+" with index "+str(index))

  # in
# # return bolean when checking condition like
# print("a"in"hello")  #=> false noa in this word
#
# # you have to convert to string when comaping character from string with numbers
# print(str(1) in 'abs')
#
# # look into list
# some_list=['1','a',True]
# print(True in some_list) # no need to convert types because each element could have its own typein the list

# dictionary in looking to key by default but you also can use value
# some_dict = {1:'a',2:'b',3:'c'}
# print (1 in some_dict)
# print (1 in some_dict.keys())
# print ('a' in some_dict.values())

# # min/max
# print(min(1,3,2,5))
# list_l=[1,6,5,9]
# print(max(list_l))
# print(max('Hello'))
# for x in 'Hello':
#     print(ord(x))

# #shafle you need to import it before use
# from random import shuffle
# list_l=[1,6,5,9]
# shuffle(list_l)
# print(list_l)
#
# from random import randint

# print(randint(1,100)) # return rundon between 1 and 100

s='hello'
ss=s[1]
print(ss)