# Aplicacion interactiva
# verificar si se ha ingresado un numero y si se ingreso un numero ingresar la operacion.
# Despues pedir que ingrese el segundo numero el resultado se guarda el primer numero y se pide segundo numero

print("bienvenidos a la calculadora")
print("para salir escribe salir")
print("las operaciones son suma, resta, multi, div")

resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese un numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("ingrese una operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingrese el siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("operacion no valida")

    print(f"el resultado es {resultado}")
