# List comprehension
#
# greeting = 'hello'
#list_l=[]
# # to cretae a list from latter of this word you should use
# for l in greeting:
#     list_l.append(l)
# print(list_l)
# simplify previous
# list_l=[letter for letter in greeting]
# print(list_l)
#
# list_numb=[n for n in range(1,11)]
# print(list_numb)
#
# list_numb=[n for n in '1112121'.replace(',','')]
# print(list_numb)

# adding if else to short form
# list_n=[11,-11,3]
# # only if statment
# result=[number for number in list_n if number>=0]
# print(result)
# # if else
# result=['+'+str(number) if number>=0 else number for number in list_n]
# print(result)
# odd_list=[]
# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in digits:
#     if number%2!=0:
#         odd_list.append(number)
# print(odd_list)

#
# new_list=[]
# greetings = ['hello', 'hi', 'hey', 'hola']
# for letter in greetings:
#     new_list.append(letter[1])
# print(new_list)