# *args **kwargs
# def ten_percent_of_product(x,y):
#     return (x*y)*0.1
#
# print(ten_percent_of_product(10,20))

# def ten_percent_of_product_with_args(*args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product
#
# print(ten_percent_of_product_with_args(23,11,22))
# # args is a tuple
# # if you need to add spec arg to function with args it should be on the first place
#
# def percent_of_product_with_args(percent,*args):
#     product = 1
#     for number in args:
#         product = product * number/percent
#     return product

# kwargs  is like dictionary
# def func_with_kwargs(**kwargs):
#      print(kwargs)
#
# func_with_kwargs(first=1,second=2,third=3)

# def func_with_kwargs(greeting, **kwargs):
#     if 'food' in kwargs:
#         print('{} your favorite food is {}'.format(greeting, kwargs['food']))
#
# func_with_kwargs('HI', food='milk')

# import random
# def func_with_args_and_kwargs(*args, **kwargs):
#     if 'food' in kwargs:
#
#         print('{} your favorite food is {}'.format(random.choice(args), kwargs['food']))
#
# func_with_args_and_kwargs('joe','nic', food='milk')


# def is_item_here(item, *args):
#     print(str(item).lower() in str(args).lower())
#
#
# is_item_here('joe',1,'Joe')

def your_favorite_color(my_color,**kwargs):
    if 'color' in kwargs:
        print('My favorite color is {}, but {} is also pretty good!'.format(my_color,kwargs['color']))
    else:
        print('My favorite color is {}, what is your favorite color?'.format(my_color))


your_favorite_color('red',colorr='blue')