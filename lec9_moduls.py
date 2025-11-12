import math
import random
# import string
import locale
import decimal
import datetime
from datetime import date, time, datetime
# ===============locale
locale.setlocale(locale.LC_ALL,"uk")
number=1234567.89
print(number)
formatted=locale.format_string("%.2f", number)
print(formatted)

formatted=locale.currency(number)
print(formatted)

print(locale.getlocale())
# #==============decimal
# number=0.1+0.1+0.1+0.1
# print("{0:f}".format(number))

number=decimal.Decimal("10.457575")
print(number)
print(number.quantize(decimal.Decimal("1.00000")))

# number=decimal.Decimal("10.4575")
# print(number.quantize(decimal.Decimal("1.000"),decimal.ROUND_FLOOR))

# number=decimal.Decimal("10.4571")
# print(number.quantize(decimal.Decimal("1.000"),decimal.ROUND_FLOOR))

# #=========================datetime=======
print(date(2023,10,10))
today=date.today()
print(today)
print(f"{today.year} year {today.month} month")

print(time())
print(time(10,43))

fulldate=datetime.now()
print(fulldate)
print(datetime(2023,9,15,12,43))
# # %d, %m, %y (23), %Y (2023), %H, %M, %S

date1="25/05/23"
print("date: ",datetime.strptime(date1,"%d/%m/%y"))

# ================================
# from string import printable
# print(random.sample(range(500), 8))
# # print(random.sample([x for x in string.printable], 8))
# print(random.sample([x for x in printable], 8))
# print(random.sample([x for x in "Python is lang"], 8))

# print(math.cos(45))
# import lec7_def_as_parametres

# print(__name__)  
