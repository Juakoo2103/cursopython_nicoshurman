numeros = [2, 5, 6, 8, 9, 1, 2, 3, 5, 76, 8]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)

print(numeros)
print(numeros2)

usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]


# funcion lambda es una funcion anonima donde se pasa el parametro : valorRetorno
usuarios.sort(key=lambda el: el[1])

print(usuarios)
