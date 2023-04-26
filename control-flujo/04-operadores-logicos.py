# and, or ,not
# and dos condiciones son true o false
# or una de las condiciones es true
# not negar el resultado de la operacion

gas = False  # Si cambiamos a false entonces no se imprime
encendido = True
edad = 18

# if gas and encendido:
#     print("puedes avanzar")
# if gas or encendido:            # imprime todo el tiempo
#     print("puedes avanzar")
# if not gas or encendido:
#     print("puedes avanzar")


if not gas and encendido and edad > 17:
    print("puedes avanzar")

# Operaciones de corto circuito es cuando la operacion de la izquierda corta toda la condicion
