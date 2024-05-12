from datetime import date, MAXYEAR, MINYEAR, datetime, time, timedelta

entrada = input("Quando foi seu ultimo ATS: ")
ats = datetime.strptime(entrada,"%d/%m/%Y")
prox = ats + timedelta(days=1825)
print(f'previsão de proximo ats em : {prox.date().strftime("%d/%m/%Y")}')
