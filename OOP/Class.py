# class Car:
#
#     wheels=4
#     def __init__(self, name, color):
#         self.name=name
#         self.color=color
#
# #methods of the class
#     def drive(self):
#         print(self.name+' car is driving') # self mean that it related to selected instance
#
#     def drive(self,city):
#         print(self.name+' car is driving'+' to '+city) # self mean that it related to selected instance
#     def change_color(self,new_color):
#         self.color=new_color
#
# opel_car=Car('opel','red')
# opel_car.drive('Moscow')
# mazda=Car('CX5','blue')
# mazda.drive('London')
# mazda.change_color('yellow')
# print(mazda.color)
# mazda.drive('lviv')
# print(opel_car.drive)
# print(opel_car.wheels)
# print(opel_car.name)
# print(opel_car.color)
# methods of the class

# class Circle:
#     pi=3.14
#     def __init__(self,radius=1):
#         self.radius=radius
#         # it is possible to initialize property here
#         self.circle_length=2*self.pi*self.radius
#     def get_area(self):
#         return self.pi*(self.radius**2)
#     def get_circle_length(self):
#         return 2*self.pi*self.radius
#
# circle_1=Circle(3)
# print(circle_1.get_area())
# print(circle_1.circle_length) # just call the property and it will be calculated during init of the object
# circle_1=Circle()
# print(circle_1.get_area())
# circle_2=Circle(3)
# print(circle_2.get_area())
# circle_3=Circle(5)
# print(circle_3.get_area())
# print(circle_3.get_circle_length())

# class BankAccount:
#     def __init__(self, client_id, client_first_name, client_last_name, balance=0.0):
#         self.client_id=client_id
#         self.client_first_name=client_first_name
#         self.client_last_name=client_last_name
#         self.balance=balance
#
#     def add(self,cash):
#         self.balance+=cash
#
#
#     def withdraw(self,amount):
#         self.balance-=amount
#
# new_user=BankAccount(1,'Test','test',100)
# new_user.add(100)
# print(new_user.balance)
# new_user.withdraw(50)
# print(new_user.balance)