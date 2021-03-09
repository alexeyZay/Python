from functools import wraps

def print_function_data(function):
    '''

    :param function: takes function with any number of params
    :return: name and documentation from initial function
    '''
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"you are using {function.__name__} ")
        print(f"you are using {function.__doc__} ")
        return function(*args,**kwargs)
    return wrapper
@print_function_data
def square_count(x, y):
    '''

    :param x: one param
    :param y: second param
    :return: the sum of suqres x **2 + y **2
    '''
    result = x **2 + y **2
    return result


print(square_count(2, 3))
# if you will try to get doc or name from square_count function directly 'Print(square_count.__name__)' you will see the name
# of wrapper method to avoid such situation you should use 'wraps()' function before wrapper in this case direct call to
# 'Print(square_count.__name__)' return the correct data
print(square_count.__name__)
print(square_count.__doc__)


def print_args(function):
    def wrapper(*args, **kwargs):
        print(f'This is args:{args} and that is kwargs:{kwargs}')
        return function(*args, **kwargs)

    return wrapper


def some_function(x, y, name='vasya'):
    print(x, y, name)


some_function(1, 2, name="Brock")