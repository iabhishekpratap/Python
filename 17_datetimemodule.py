import datetime
from datetime import timedelta #for future date

print(datetime.datetime.now())

currdtm=datetime.datetime.now()
print(currdtm)

#formatting
formatted=currdtm.strftime('%y=%m=%d %H-%M')
print(formatted)

future=currdtm+timedelta(days=10)
print(future)

