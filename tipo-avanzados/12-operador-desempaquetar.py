# lista = [1,2,3,4]
# # print(lista)
# # print(*lista)

# lista2 = [5,6]

# combinada = [*lista, *lista2]
# print(combinada)


punto1 = {"x": 19}
punto2 = {"y": 15}
# se pueden añadir nuevos valores y llaves
nuevoPunto = {**punto1, **punto2, "z": "hola"}
print(nuevoPunto)
