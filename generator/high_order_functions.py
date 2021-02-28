# def count(x, func):
#     result = 1
#     for number in range(1, x):
#         result *= func(number)
#     return result
#
#
# def sqare(x):
#     return x * x
#
#
# def cube(c):
#     return c ** 3
#
#
# s = count(4, sqare)
# print(s)
# c = count(4, cube)
# print(c)
#
# def my_func(a,b,func):
#     result=func([a,b])
#     return result
#
# print(my_func(20,12,sum))
#
from random import choice
# nested function
# def colorize(thing):
#     def get_random_color():
#         color=('green','red','yellow')
#         result=choice(color)
#         return result
#     result = get_random_color()+' '+thing
#     return result
#
# print(colorize('apple'))

# return a function as a result of function
# def retun_function():
#     def get_random_color():
#         color_tuple=('green','red','yellow')
#         color=choice(color_tuple)
#         return color
#     return get_random_color
#
# fu=retun_function()
# print(fu())
# fu2=retun_function()
# print(fu2())
# fu3=retun_function()
# print(fu3())

# nested function can use outer function variables
# nested function
def colorize(thing):
    def get_random_color():
        color=('green','red','yellow')
        result=choice(color)
        return result +' '+thing
    return get_random_color

# print(colorize('dog')())
dog_in_color=colorize('dog')
print(dog_in_color())