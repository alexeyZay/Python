# initialize {key:value}
car_prices = {'mazda': 2000, 'Toyota': 5000, 'Volvo': 15000}

print(car_prices['mazda'])

# adding new item to dictionary ( dictionary is not sorted so no need to provide index when adding new item )

car_prices['porche'] = 120000

print(car_prices)

# deleting from dictionary

del car_prices['porche']  # BE CEARFULL because if you leave it without key it will delete whole the dictionary

print(car_prices)

# clear dict but not delete

car_prices.clear()  # will clear the dict but not delete it  so result is-empty dict
print(car_prices)

# dictionary can contain str int lists dict's

person = {'first name': 'jack',
          'last name': 'black',
          'age': 33,
          'hobbies': ['football', 'golf', 'photo'],
          'childrens': {'son': 'Peter', 'doughter': 'olga'}}
print(person['age'])
print(person['hobbies'])
print(person['hobbies'][1])  # getting list from dict as a slice

# add new record to dict
person['car'] = 'porche'
print(person)
# updating the elements
person['car'] = 'mazda'
print(person)

person['hobbies'][1] = 'basketball'
print(person)

person['childrens']['son'] = 'John'
print(person)

