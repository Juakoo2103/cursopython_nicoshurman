from io import open

# #escritura
# texto = "hola mundo"

# archivo = open('archivos/hola-mundo.txt', 'w')
# archivo.write(texto)
# archivo.close()

# lectura
# archivo = open('archivos/hola-mundo.txt', 'r')
# texto = archivo.read()
# archivo.close()
# print(texto)

# lectura como lista
# archivo = open('archivos/hola-mundo.txt', 'r')
# texto = archivo.readlines()
# archivo.close()
# print(texto)

with open('archivos/hola-mundo.txt', 'r') as archivo:
    texto = archivo.read()
    print(texto)
