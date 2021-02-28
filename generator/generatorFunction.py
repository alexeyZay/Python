# import datetime
# # simple function
# def get_the_number(x):
#     return x
#
#def count_up_to():


# day_of_week = {1: 'Sunday', 2: 'Monday', 3: 'Thuesday', 4: 'Wednsday', 5: 'Thersday', 6: 'Friday', 7: 'Suturday'}
# count = 1
# while count <= 7:
#     yield day_of_week[count]
#     count += 1
#
# for number in v:
#     print(number)
# --------------------------test
# def get_week_day():
#     day_of_week = {1: 'Sunday', 2: 'Monday', 3: 'Thuesday', 4: 'Wednsday', 5: 'Thersday', 6: 'Friday', 7: 'Suturday'}
#     day = 1
#     while day <= len(day_of_week.keys()):
#         yield day_of_week[day]
#         day += 1
#
# z = get_week_day()
# print(z.__next__())
# print(z.__next__())
# print(z.__next__())
# print(z.__next__())
# print(z.__next__())
# print(z.__next__())
# print(z.__next__())
# # print(get_week_day().__next__())

def even_odd():
    even_odd=['even','odd']
    count=0
    while count<=2:
        if count == 2:
            count = 0
        yield even_odd[count]
        count+=1

even_odd_generator=even_odd()
print(even_odd_generator.__next__())
print(even_odd_generator.__next__())
print(even_odd_generator.__next__())
print(even_odd_generator.__next__())
print(even_odd_generator.__next__())
print(even_odd_generator.__next__())