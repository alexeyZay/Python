import csv

# with open('students.csv','w') as file:
#     csv_writer=csv.writer(file)
#     csv_writer.writerow(['FirstName','LastName','Age'])
#     csv_writer.writerow(['Jane', 'White', '24'])

# with open('students.csv') as file:
#     csv_reader=csv.reader(file)
#     for student in csv_reader:
#         print(student)

# with open('car.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     car_list=[]
#     for car in csv_reader:
#         car_list.append([car[1],car[2]])
#     print(car_list)
#
# with open('new_car.csv','w') as file:
#     csv_writer = csv.writer(file)
#     for car in car_list:
#         csv_writer.writerow(car)

# with open('car.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     with open('new_car.csv', 'w') as file:
#         csv_writer = csv.writer(file)
#         for car in csv_reader:
#             csv_writer.writerow([car[1], car[2]])

with open('students1.csv','w') as file:
    headers_list=['FirstName','LastName','Age']
    csv_writer=csv.DictWriter(file,fieldnames=headers_list)
    csv_writer.writeheader()
    csv_writer.writerow({
        'FirstName':'Jane',
        'LastName':'White',
        'Age':'24'})
    csv_writer.writerow({
        'FirstName':'Joe',
        'LastName':'Black',
        'Age':'25'})