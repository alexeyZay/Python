nested_list=[[True,1.12,1,1,1],['test',2,4,3],[1,2,3,4,5],[11,21,34]]
# using loops to print elements
# for inner_list in nested_list:
#     for element in inner_list:
#         print(element)

#Comprehension
[[print(element) for element in iner_list] for iner_list in nested_list]