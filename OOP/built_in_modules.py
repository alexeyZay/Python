# # to get functionality from other modules we should import them# import random  # provides an ability to use all the functions from that module# from random import randint## # x=random.randint(1,10)# # if you need only one method from module you should use the following## x = randint(1, 10)# # but you can't use shufle()# l = [1, 2, 3]# random.shuffle(l)# print(l)# print(x)## # it is possible to import with name that you selected# from random import shuffle as shuffle_my_list## my_l = [2, 3, 4, 5]# shuffle_my_list(my_l)# print(my_l)## import math## print(math.sqrt(123456789))# print(math.factorial(987))# print(math.pow(876, 54))