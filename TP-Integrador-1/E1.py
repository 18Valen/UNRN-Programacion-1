import datetime

from datetime import datetime

print("\n")

ahora = datetime.now()

print(ahora.day)
print(ahora.month)
print(ahora.year)
print(ahora.hour)
print(ahora.minute)
print(ahora.second)
print(ahora.microsecond)

print("\n")

fecha = datetime(2007, 12, 4, 12, 35)

print(fecha.year)
print(fecha.month)
print(fecha.day)
print(fecha.hour)
print(fecha.minute)

print("\n")

texto = "20/01/2005 13:23"
fecha2 = datetime.strptime(texto, "%d/%m/%Y %H:%M")

print(fecha2)
print(type(fecha2))