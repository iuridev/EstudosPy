from datetime import date, MAXYEAR, MINYEAR, datetime, time, timedelta

ats = datetime(2023,4,20)
prox = ats + timedelta(days=1825)
print(f'previsão de proximo ats em : {prox.date().strftime("%d/%m/%Y")}')
