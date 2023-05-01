mascotas = ["wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0])
mascotas[0] = "Bicho"  # modifica el valor de la posicion 0
# print(mascotas)  # en vez de mostrar wolfgang muestra bicho
# # Muestra Pulga y Copito porque selecciono el valor del indice 2 en adelante
# print(mascotas[2:])
# print(mascotas[-1])  # da la vuelta a la lista
# print(mascotas[::2])  # se salta cada 2 veces

numeros = list(range(21))
print(numeros[1::2]) #numeros impares -1  
print(numeros[::2]) #numeros pares -1
print(numeros[:2]) #toma el valor por defecto en el inicio y llega hasta el valor -1
print(numeros[0:]) #toma el valor por defecto al final y llega hasta el ultimo valor -1


