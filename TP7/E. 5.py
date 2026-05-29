# Ejercicio 5 - TP 7 - Codigo de Materia

codigo_materia_ingresado = input("Por favor ingrese su codigo de materia, debe tener este formato (PROG-101): ").strip()

if codigo_materia_ingresado.count("-") == 1:
    codigo_materia_ingresado = codigo_materia_ingresado.split("-")
    materia = codigo_materia_ingresado[0]
    numero = codigo_materia_ingresado[1]
    if materia.isalpha():
        materia = materia.upper()
        if numero.isdigit():
            print(f"Codigo valido: {materia}-{numero}")
        else:
            print("lo ingresado despues de el guion medio, no cumple con el formato pedido")
    else:
        print("lo ingresado antes del guion medio, no cumple con el formato pedido")
else:
    print("el texto ingresado no cumple con el formato pedido")
    
    
        