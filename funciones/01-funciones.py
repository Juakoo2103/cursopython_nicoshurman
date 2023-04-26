# def hola(nombre, apellido):  # Dentro de la funcion se llama parametro
#     print("hola mundo")
#     print(f"Bienvenido {nombre} {apellido}")


# hola("Joaquin", "Gonzalez")  # Aca pasa a ser un argumento para la funcion
# hola("Chanchito", "feliz")


# Parametros opcionales
def hola(nombre, apellido="Feliz"):  # se le asigna un valor al parametro
    print("hola mundo")
    print(f"Bienvenido {nombre} {apellido}")


hola("Joaquin", "Gonzalez")
# si no se le asigna un valor al argumento toma el valor asignado por defecto
hola("Chanchito")
hola("Chanchito", "Triste")


# Puedo asignarle un valor al argumento para que lo pase en la funcion correctamente
hola(apellido="Gonzalez", nombre="Joaquin")

