import datetime
import pytz

print(datetime.datetime.utcnow())
# print(pytz.tzin)

kiev = 'Europe/Moscow'
tz_kiev = pytz.timezone(kiev)
kiev_time = datetime.datetime.now(tz_kiev)
print(kiev_time)

for tz in pytz.all_timezones:
    print(tz)