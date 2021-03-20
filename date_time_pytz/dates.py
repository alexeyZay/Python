from datetime import date

# today = date.today()
# print(today)
# day = date.today() - date(2021, 3, 11)
# print(day)
#
# my_b_day = date(today.year, 7, 24)
# if my_b_day < date.today():
#     my_b_day = my_b_day.replace(year=today.year + 1)
# print(my_b_day)
#
# days_until_b_day = my_b_day - date.today()
# print(days_until_b_day)
#
# weekday = today.weekday()
# print(weekday)

year = input('please enter a year ')
month = input('please enter a month')
day = input('please enter a day')

date = date(int(year),int(month),int(day))
# print(date)
weekday=date.weekday()
if weekday==0:
    print(' day is a Monday')
elif weekday==1:
    print(' day is a Thusday')
elif weekday == 2:
    print(' day is a Wednsday')
elif weekday == 3:
    print(' day is a Thursday')
elif weekday == 4:
    print(' day is a Friday')
elif weekday == 5:
    print(' day is a Saturday')
elif weekday == 6:
    print(' day is a Sunday')