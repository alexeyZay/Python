# class Swimable:
#     def __init__(self, name):
#         self.name = name
#         print('Method init() of Swimable')
#
#     def greeting(self):
#         print(f'Hello My name is {self.name} and I can swim')
#
#     def swim(self):
#         print(f'I\'m can swiming')
#
#
# class Walkable:
#     def __init__(self, name):
#         self.name = name
#         print('Method init() of Walkable')
#
#     def greeting(self):
#         print(f'Hello My name is {self.name} and I can walk')
#
#     def walk(self):
#         print(f'I\'m can walking')
#
#
# class Flyable:
#     def __init__(self, name):
#         self.name = name
#         print('Method init() of Flyable')
#
#     def greeting(self):
#         print(f'Hello My name is {self.name} and I can fly')
#
#     def fly(self):
#         print(f'I\'m can flying')
#
#
# class GameCharacter(Swimable, Walkable, Flyable):
#     def __init__(self, name):
#         self.name = name
#         print(isinstance(self, GameCharacter))
#         Swimable.__init__(self, name)
#         Walkable.__init__(self, name)
#         Flyable.__init__(self, name)
#
#     def greeting(self):
#         print(f'Hello My name is {self.name}')
#
#
# james = GameCharacter('James')
# james.greeting()  # return 'SWIM' because swimable on the first place in the list of inheritance
# james.swim()
# james.fly()
# james.walk()
# print(isinstance(james, Flyable))  # cheking that the instance is the type of Flyable
# print(isinstance(james, Swimable))  # cheking that the instance is the type of Swimable
# print(isinstance(james, Walkable))  # cheking that the instance is the type of Walkable
# print(isinstance(james, list))  # cheking that the instance is the type of List
# print(isinstance(james, object))  # cheking that the instance is the type of Object
