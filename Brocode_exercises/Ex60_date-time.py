# Date and Time

import datetime

date = datetime.date(2025,2,1)
today = datetime.date.today()
present = datetime.datetime.now()
#Modify
present = present.strftime("Time - %H:%M:%S  Date -%d-%m-%y")

print(present)
print(date)
print(today)