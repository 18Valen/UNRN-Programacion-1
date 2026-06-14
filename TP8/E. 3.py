nombres = []

while len(nombres) < 4:
    nombre = input("escriba el nombre de un estudiante: ").lower().capitalize()
    if nombre.strip():
        nombres.append(nombre)
    else:
        print("se ha ingresado un texto vacío, por favor volver a ingresar un nombre")

archivo = open("nombres.txt", "w")

for nombre in nombres:
    archivo.write(nombre)
    archivo.write("\n")

archivo.close()