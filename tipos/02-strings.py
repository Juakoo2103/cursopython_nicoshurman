nombre_curso = "Ultimate Python"

# las comillas triples se utilizan para crear cadenas de varias lineas o tambien conocidas como texto multilinea

descripcion_curso = """Ultimate Python, este curso contempla todos los
detalles que necesitas aprender para encontrar un
trabajo como programador."""

print(descripcion_curso)

# funcion len para comprobar el largo de un string

print(len(nombre_curso))

# para acceder al index de un string

print(nombre_curso[0])

# Por convencion el index de un string comiezna en 0

# Para recortar un string se puede hacer

print(nombre_curso[0:8])

# al pasar solo el valor de la izquierda solo rellenara con lo que python considere que "debe ser"

print(nombre_curso[9:])

# al pasar el valor de la derecha solo rellenara con lo que python considere que "debe ser"

print(nombre_curso[:8])

# cuando no se le pasan valores da el valor completo del string

print(nombre_curso[:])
