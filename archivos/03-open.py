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

# with y seek
# with open('archivos/hola-mundo.txt', 'r') as archivo:
#         texto = archivo.readlines()
#         for linea in texto:
#             print(linea)

# agregar

# archivo = open('archivos/hola-mundo.txt', 'a+')
# archivo.write('Chao mundo')
# texto = archivo.read()
# print(texto)
# archivo.close()

# lectura y escritura simultaneameante

# with open('archivos/hola-mundo.txt', 'r+') as archivo:
#         texto = archivo.readlines()
#         archivo.seek(0)
#         texto[0] = 'Chanchito feliz'
#         archivo.writelines(texto)
