# numero = 1

# while numero <= 100: # es que numero es menor que 100 es true entonces se itera hasta llegar a la ultima iteracion
#     print(numero)
#     numero *= 2

# Terminar virtual para ejecutar comandos
# comando = ""

# while comando.lower() != "salir":
#     comando = input("$")
#     print(comando)

# Loop infinito siempre debe llevar un break dentro de la condicion
while True:
    comando = input("$")
    print(comando)
    if comando.lower() == "salir":
        break
