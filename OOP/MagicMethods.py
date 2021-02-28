# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     # def __init__(self,first_name):
#     #     self.first_name=first_name
#
#     def __str__(self):
#         return self.first_name + ' ' + self.last_name
#
#     def __del__(self):
#         print(f'object {self.first_name} was deleted')
#
#     def __len__(self):
#         return self.age
#
#     def __add__(self, other):
#         return self.age+other.age
#
#
# p1 = Person('F_name', 'L_name', 33)
# p2 = Person('F_name', 'L_name', 33)
# print(p1+p2)
# # print(p.first_name)
# print(len(p))
#
# class Chain:
#     def __init__(self,number_of_item):
#         self.number_of_item=number_of_item
#     def __print__(self):
#         print(f'Chain with {self.number_of_item} items')
#
#     def __len__(self):
#         return self.number_of_item
