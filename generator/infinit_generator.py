# def create_pattern():
#     max_pattern_number=10
#     patterns=('first','second','third','forth','fifth')
#     i=0
#     result_list=[]
#     while len(result_list)<max_pattern_number:
#         if i>=len(patterns):
#             i=0
#         result_list.append(patterns[i])
#         i+=1
#     return result_list
#
# print(create_pattern())
# def get_current_pattern():
#     existing_patterns = ('first', 'second', 'third', 'forth', 'fifth')
#     i = 0
#     while True:
#         if i >= len(existing_patterns):
#             i = 0
#         yield  existing_patterns[i]
#         i+=1
#
# current_pattern=get_current_pattern()
# print(current_pattern.__next__())
# print(current_pattern.__next__())
# print(current_pattern.__next__())
# print(current_pattern.__next__())
# print(current_pattern.__next__())
# print(current_pattern.__next__())
# print(current_pattern.__next__())

def  get_infinite_square_generator():
    i=1
    while True:
        yield i**2
        i+=1

infinite_square_generator = get_infinite_square_generator()
print(next(infinite_square_generator))
print(next(infinite_square_generator))
print(next(infinite_square_generator))
print(next(infinite_square_generator))