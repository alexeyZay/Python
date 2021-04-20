import pytz
import datetime

for country in pytz.country_names:
    print(country, pytz.country_names[country], pytz.country_timezones.get(country))

time_zone_dict = {
    'AD': ('Andorra', 'Europe/Andorra'),
    'AE': ('United Arab Emirates', 'Asia/Dubai'),
    'AF': ('Afghanistan ', 'Asia/Kabul'),
    'AG': ('Antigua & Barbuda', 'America/Antigua'),
    'AI': ('Anguilla', 'America/Anguilla'),
    'AL': ('Albania', 'Europe/Tirane'),
    'AM': ('Armenia', 'Asia/Yerevan'),
    'AO': ('Angola', 'Africa/Luanda')
}
# print('please enter two letters code of the country to choose timezone or "q" to quit')

for key in time_zone_dict:
    print(key,time_zone_dict[key])
print('please enter two letters code of the country to choose timezone or "q" to quit')
while True:
    country_code=input()
    if country_code=='q':
        break
    if country_code in time_zone_dict.keys():
        timezone = pytz.timezone(time_zone_dict[country_code][1])
        print('local time is {}'.format(datetime.datetime.now(tz=timezone)))
        print('UTC time is {}'.format(datetime.datetime.utcnow()))