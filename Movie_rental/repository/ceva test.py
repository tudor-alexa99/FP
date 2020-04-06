from datetime import datetime
from datetime import timedelta

d = timedelta(days=15)
n=40
today = datetime.now()
duedate= datetime.now() + timedelta(days=n)

# today += timedelta
# ret = today + retr

print(duedate)
print(duedate>today)

newtime = datetime(2018, 3, 21)
print(newtime)