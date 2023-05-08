# from pprint import pprint para imprimir diccionarios mas legibles

string = "Hola mundo este es mi string"


def quita_espacios(texto):
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def mensaje(diccionario):
    mensaje = "los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones\n"
    return mensaje


sin_espacios = quita_espacios(string)
cuenta = cuenta_caracteres(sin_espacios)
ordenados = ordena(cuenta)
mayores = mayores_tuplas(ordenados)
men = mensaje(mayores)
print(men)
