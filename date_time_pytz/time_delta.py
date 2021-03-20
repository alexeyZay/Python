from datetime import datetime, timedelta

year = timedelta(days=365)
print(year)


today = datetime.now()
print('today is',today)
print('23 days from today will be' , (today+timedelta(days=23)))