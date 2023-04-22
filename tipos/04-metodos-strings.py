animal = "     chanCHito feliz       "

# Metodos de manejos de strings

# Todo en mayusculas
print(animal.upper())

# Todo en minusculas
print(animal.lower())

# Toma la primera letra de la cadena y la deja en mayusculas
# Para realizar de forma correcta el capitalize hay que primero realizar un strip al string para eliminar espacios en blanco
print(animal.capitalize())

# Descomenta para probar el ejemplo
# print(animal.strip().capitalize())

# Toma la primera letra de cada palabra dentro del string y la deja en mayusculas
print(animal.title())

# Toma el string y remueve espacios en blanco a la izquierda y a la derecha
# Existe el lstrip y rstrip para eliminar espacios en blanco para izquierda y derecha
print(animal.strip())

# Devuelve el index de la cadena de caracteres
# Debe existir en el string si no devolvera -1
print(animal.find("CH"))

# Si encuentra los caracteres del primer argumento reemplaza con el segundo argumento que le damos en el metodo
print(animal.replace("nCH", "j"))

# Busca si el string contiene los caracteres especifidados en el primer argumento
print("nCH" in animal)

# Busca si el string NO contiene los caracteres especifidados en el primer argumento
print("nCH" not in animal)
