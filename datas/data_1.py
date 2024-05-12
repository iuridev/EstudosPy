from datetime import date, MAXYEAR, MINYEAR,datetime, time, timedelta

d = date(1994,4,26)
print(d)

MAX_YEAR = MAXYEAR
MIN_YEAR = MINYEAR
print(f'\nData Ano maximo: {MAX_YEAR}\nData Ano minimoS: {MIN_YEAR}\n')

d = date.today()
print(d)

d = datetime.today()
print(d)

d = datetime.now()
print(d)

e = time(10,20,45)
print(e)

y = d + timedelta(weeks=1)
print(y)

