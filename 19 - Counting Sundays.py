import datetime
from calendar import monthrange

firstDay = datetime.datetime(1901, 1, 1)
lastDay = datetime.datetime(2000, 12, 31)
count = 0
while firstDay < lastDay:
    rangeDays = monthrange(firstDay.year, firstDay.month)[1]
    #print (firstDay, ' ', rangeDays, count)
    if (firstDay.weekday() == 6):
        count = count + 1
    firstDay = firstDay + datetime.timedelta(days= rangeDays)

print(count)