# Ejercicio 4 - TP 7 - Edad Valida

print()
edad_ingresada = input("Por favor ingrese su edad en números: ").strip()


if edad_ingresada.isnumeric():
    edad = int(edad_ingresada)
    if 0 < edad < 120:
        print()
        print(f"edad registrada: {edad}")
    else:
        print()
        print("la edad ingresada no es valida")
else:
    print()
    print("la edad ingresada no es valida")
