'''
   a
  / \
 b   c
  \ /
   d
   Lets see how methods will be invoked
'''

class a:
    def some_method(self):
        print('Class A')


class b(a):
    def some_method(self):
        print('Class B')

class c(a):
    def some_method(self):
        print('Class C')

class d(b,c):
    def some_method(self):
        print('Class D')


some_object=d()
some_object.some_method()

# here is how to identify the order of method executions
# 1) __mro__
print(d.__mro__)
#2) method mro()
print(d.mro())
# help for class d
print(help(d))