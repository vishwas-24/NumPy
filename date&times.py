import datetime

date = datetime.date(2026, 9, 2)    # YYYY/MM/DD
today = datetime.date.today()
time = datetime.time(12, 30, 0)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S  %d-%m-%y")
target_datetime = datetime.datetime(2026, 2, 9, 10, 10, 00)
current_datetime = datetime.datetime.now()

# print(date)
# print(today)
# print(now)

if target_datetime < current_datetime:
    print("Target date has passed")

else:
    print("Target date has not passed")