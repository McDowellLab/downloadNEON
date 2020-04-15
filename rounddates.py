from datetime import datetime

def round15min(dt, timeagg):

    rounded = datetime(dt.year, dt.month, dt.day, dt.hour, int(timeagg * round((float(dt.minute) + (float(dt.second) / 60)) / timeagg)))
    return rounded


dtstart = datetime.strptime('2019-09-28 20:16:07', "%Y-%m-%d %H:%M:%S")
dtstart2 = datetime.strptime('2019-09-28 20:32:07', "%Y-%m-%d %H:%M:%S")
# startd.strftime("%Y-%m-%d %H:%M")

f = round15min(dtstart,15)
print(f)
f = round15min(dtstart,30)
print(f)
f = round15min(dtstart2,30)
print(f)
