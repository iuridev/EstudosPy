import datetime
import pytz

d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(f'São Paulo {d}')

d = datetime.datetime.now(pytz.timezone("Europe/Lisbon"))
print(f'Portugal {d}')
