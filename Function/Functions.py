# def print_greeting():
#     '''
#
#     :return:NONE
#     '''
#     print('Hello')
# print_greeting()

# with param
# def print_greeting_with_param(user_name='Jack'):  # Jack is default value
#     '''
#
#     :param name:user_name
#     :return: None
#     '''
#     print('Hello ' + user_name + ' !')
#
# print_greeting_with_param()
# print_greeting_with_param('Ivan')

# def sum_of_two_int(a=0, b=0):
#     '''
#
#     :param a:
#     :param b:
#     :return: sum of two int
#     '''
#     return a + b
#
#
# s = sum_of_two_int(11, 2)
# print(s)
# # return info about method
# help(sum_of_two_int)
#

# def is_hello_in_text (text):    # in return bolean value True if value contains and False if not
#     if 'hello' in text.lower(): # can be simplified 'hello' in text.lower() => no need if else
#         return True
#     else:
#         return False

# def is_hello_in_text (text='empty'):
#     return 'hello' in text.lower()
# print(is_hello_in_text("Hello"))
#
# def string_in_text(string, text):
#     return string in text
#
# print(string_in_text('he','The apple'))

# def greeting_depends_on_gender(name,gender):
#     if gender=='male':
#         print('hello '+name+' You looks good')
#         return gender
#     elif gender=='female':
#         print('hello '+name+' you are preaty')
#         return gender
#     else:
#         print('hello '+name+' Who are you?')
#         return gender
# returned_value=greeting_depends_on_gender('Jack','male')
# returned_value=greeting_depends_on_gender('Jane','female')
# returned_value=greeting_depends_on_gender('J','le')
# result=[]
# def odd_numbers(min,max):
#     for number in range(min,max+1):
#         if number%2!=0:
#             result.append(number)
#     return result


def odd_numbers(min, max):
    return [number for number in range(min, max + 1) if number % 2 != 0]

x= odd_numbers(1,11)
print(x)

