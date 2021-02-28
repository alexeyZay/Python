# # Inheritance
# class Car:
#     wheels_number = 4
#
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#     def drive(self, city):
#         print(self.name + 'is driving to' + city)
#
#     def change_color(self, new_color):
#         self.color = new_color
#
#
# class Truck(Car):
#     def __init__(self, name, color, year, is_crashed):
#         Car.__init__(self, name, color, year, is_crashed)
#         print('Truck is created')
#
#     def drive(self, city):
#         print('Truck' + self.name + 'is driving to' + city)
#
#     def load_cargo(self, weight):
#         print('The cargo is Loaded. The weight is:' + str(weight))
#
#
# man_truck = Truck('Man', 'white', 2011, False)
#
# man_truck.load_cargo(2500)
#
# man_truck.change_color('red')
#
# print(man_truck.color)

# Polymorphism
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         raise NotImplementedError('Class successor must implement this method')
#
#
# class Dog(Animal):
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(self.name+' is saying woof')
#
#
# class Cat(Animal):
#     def __init__(self,name):
#         self.name=name
#
#     def speak(self):
#         print(self.name+' is saying meow')
#
#
# class Mouse(Animal):
#     def __init__(self,name):
#         self.name=name
#
#     # def speak(self):
#     #     print(self.name+' is saying piii')
#
# spike=Dog('Spike')
# tom=Cat('Tom')
# jerry=Mouse('jerry')
#
# pet_list=[spike,tom, jerry]
#
# for pet in pet_list:
#     pet.speak()
#
# def pet_voice(pet):
#     pet.speak()
#
# pet_voice(tom)
# pet_voice(jerry)

# class GameCharacter:
#
#     def __init__(self, name, health, level):
#         self.name = name
#         self.health = health
#         self.level = level
#
#     def speak(self):
#         print('Hi, my name is' + self.name+'and I will kill you')
#
#     def kill(self):
#         self.health = 0
#         print('Bang-bang, now you\'re dead')

#
# g=GameCharacter('test',11,99)
# print(g.health)
# GameCharacter.kill(g)
# print(g.health)

