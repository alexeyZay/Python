# simple generator
# def get_number_from_list():
#     for number in range(10):
#         yield number
#
# list=get_number_from_list()
# print(list.__next__())
# print(next(list))
# print(next(list))

list=(number for number in range(10))

# it is good idea to use generator when working with the big data it takes less resources