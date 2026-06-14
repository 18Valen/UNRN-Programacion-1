mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]


mediciones_dic = {}
tipos_mediciones = []


for medicion in mediciones:
    tipos_mediciones.append(medicion[0])
    if not medicion[2] in mediciones_dic:
        mediciones_dic[medicion[2]] = (medicion[0], medicion[1])   
    else:
        mediciones_dic[medicion[2]] += (medicion[0], medicion[1])

tipos_mediciones = set(tipos_mediciones)

print()
print(mediciones_dic)
print()
print(tipos_mediciones)
print()

