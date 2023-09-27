#
from datetime import datetime
fecha = datetime(2024,10,3,4,12,35)
print(fecha.second)
now = datetime.now()
print(now.year)
from datetime import time
my_time = time(4,34)
print(my_time.minute)
from datetime import date
my_day = date.today()
print(my_day.day)
new_year= datetime(2024,5,6)
print(new_year- now)