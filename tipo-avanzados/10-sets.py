# set significa grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}  # Python se encarga de remover duplicados
# primer.add(5)
# primer.remove(1)

# print(primer)

segundo = [3, 4, 5]
# transformamos la lista a set en base a una lista tambien puede ser en base a tupla
segundo = set(segundo)

# print(primer | segundo) # operador de union
# print(primer & segundo) # operador de interseccion
# print(primer - segundo) # operador de diferencia
print(primer ^ segundo)   # operador de diferencia simetrica

if 5 in segundo:
    print("hola mundo")
