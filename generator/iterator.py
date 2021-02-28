# iterate

#iterable objects
number_list=[1,2,3,4,5]
#for n in numbeer_list:
#    print(n)

#for letter in 'some String':
#    print(letter)

#Iterator

# number_list_iterator=iter(number_list)
# print(type(number_list_iterator))

# string_iterator=iter("Some String")
# print(type(string_iterator))

# how to use iterator
# 1 use method __next__
#print(number_list_iterator.__next__()) # will return one element from iterable (error when there is nothing to show)
#print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())

# print(string_iterator.__next__())
# print(string_iterator.__next__())
# print(string_iterator.__next__())


# also it is possible to use next function to open iterator objects

# print(next(number_list_iterator))
# print(next(string_iterator))

def my_for_loop(iterable):
    iterator=iter(iterable)
 #   print(iterator.__next__())
    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            print('Nothing to iterat')
            break
    
my_for_loop("hello")