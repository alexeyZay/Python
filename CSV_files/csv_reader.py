import csv

# with open('car.csv') as file:
#     csv_reader = csv.reader(file)
#     for car in csv_reader:
#       #  print(car)
#         print(f'{car[1]} {car[2]} price:{car[4]}')
#
with open('car.csv') as file:
    csv_reader = csv.reader(file)
    list_of_data=list(csv_reader)
    print(list_of_data) # List of lists of data
