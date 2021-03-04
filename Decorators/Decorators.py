#
#
# # creating a decorator, the function that will extend the simple function code
# def simple_function_decorator(original_function):
#     def decor():
#         print('More values to simple function')
#         original_function()
#         print('More and More functionality to Simple function')
#     return decor
#
# @simple_function_decorator
# def simple_function():
#     print("I'm a simple function")
#
# simple_function()
#
#
# def make_complenemt_function(function):
#     print("We are glad to see you here")
#     function()
#     print('stay with us !!')
#
#
# @make_complenemt_function
# def hello():
#     print('Hello user')
#
# to make decorator function more flexible we can use *args and **kwargs as a parameter in decorator

def make_complenemt_function(func):
    def function_wraper(*args):
        print("We are glad to see you here")
        func(*args)
        print('stay with us !!')

    return function_wraper


# @make_complenemt_function
def hello():
    print('Hello user')


@make_complenemt_function
def set_user_name(func):
    greeting = func()
    print(greeting + ' ' + 'name')


# set_user_name('Ivan', hello)
f=hello()
f