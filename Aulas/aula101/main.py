#https://docs.python.org/3.0/library/datetime.html

from datetime import datetime, timedelta
"""
data = datetime(2021, 1, 12, 20, 22, 30)
print(data.strftime('%d/%m/%Y %H:%M:%S'))
"""

#data = datetime.strptime('20/04/2019','%d/%m/%Y')
#print(data.timestamp())

#data = datetime.fromtimestamp(1555729200.0)
#print(data)

d1 = datetime.strptime('10/01/2021 20:59:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('12/01/2021 21:00:00', '%d/%m/%Y %H:%M:%S')

d3 = d1 - d2

print(d3)

