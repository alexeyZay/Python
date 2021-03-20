from datetime import datetime

today = datetime(2021,3,28)
print(today)
today_tme_now =datetime.now()
print(today)
timestamp = datetime.timestamp(today)
print(timestamp)
timestamp_now = datetime.timestamp(today_tme_now)
print(timestamp_now)