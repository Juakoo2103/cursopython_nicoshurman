usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]
# nombres = []

# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# expresion es el valor que quiero retornar el item es el dato y el items es la lista

# nombres = [expresion for item in items]
# map
# nombres = [usuario[0] for usuario in usuarios]
# filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# filtrar y transformar
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]


# nombres = list(map(lambda usuario: usuario[0], usuarios))

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)

