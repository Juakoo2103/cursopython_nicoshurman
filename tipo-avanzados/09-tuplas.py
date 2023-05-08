# Las tuplas son lo mismo que la lista a diferencia que no se pueden modificar

numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)

menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)

listaCambiado = list(numeros)
# Se "modifica" la tupla, pero realmente lo que hacemos es modificar una lista que obtuvimos mediante una tupla es decir el valor de la tupla sigue siendo el mismo
listaCambiado[0] = "chanchito feliz"

print(listaCambiado)
