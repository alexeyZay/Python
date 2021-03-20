def add_rows_to_table(number_of_rows):
    entity_list = []
    counter = 0
    first_name = 'tester'
    last_name = 'l_tester'
    age = 10
    while counter <= number_of_rows:
		print(f'[INSERT INTO students (first_name,last_name,age) VALUES({first_name + str(counter)},{last_name + str(counter)},{age + counter});]')
# entity_list.append(f'[INSERT INTO students (first_name,last_name,age) VALUES({first_name + str(counter)},{last_name + str(counter)},{age + counter});'])
	counter += 1


# with open('sql_syntacs_basics.sql', 'a') as file:
#     sql_script_writer = writer(file)
#     for entity in entity_list:
#         sql_script_writer.append([entity])
add_rows_to_table(2)
