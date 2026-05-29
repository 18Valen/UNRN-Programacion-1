# Ejercio 3 - TP 7 - Acomodar Nombres

nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombres_normalizados = []
for nombre in nombres:
    nombre_n = nombre.strip().capitalize()
    nombres_normalizados.append(nombre_n)
    

print(nombres_normalizados)
