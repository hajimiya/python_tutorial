from datetime import date, datetime, timedelta

today = date.today()
now = datetime.now()
tomorrow = today + timedelta(days=1)

print("Today:", today)
print("Current date-time:", now)
print("Tomorrow:", tomorrow)
print(now.strftime("%d-%m-%Y %H:%M"))
