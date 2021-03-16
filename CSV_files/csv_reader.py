import csv

# with open('car.csv') as file:
#     csv_reader = csv.reader(file)
#     for car in csv_reader:
#       #  print(car)
#         print(f'{car[1]} {car[2]} price:{car[4]}')
#
# with open('car.csv') as file:
#     csv_reader = csv.reader(file)
#     list_of_data=list(csv_reader)
#     print(list_of_data) # List of lists of data

# Dict reader
# with open('car.csv') as file:
#     csv_reader = csv.DictReader(file)
#     for car in csv_reader:
#         print(car)
#         print(f'{car["Make"]} {car["Model"]} price:{car["Price"]}')
# with open('cars1.csv') as file:
#     csv_reader = csv.DictReader(file,delimiter=";")
#     for car in csv_reader:
#         print(f'{car["Make"]} {car["Model"]} price:{car["Length"]}')
# with open('cars1.csv') as file:
#     csv_reader = csv.reader(file,delimiter=";")
#     for car in csv_reader:
#         print(f'{car[1]} {car[2]} price:{car[3]}')
#

with open('cars2.csv') as file:
    csv_reader = csv.DictReader(file,delimiter="|")
    for car in csv_reader:
        print(f'{car["Make"]} {car["Model"]} price:{car["Length"]}')