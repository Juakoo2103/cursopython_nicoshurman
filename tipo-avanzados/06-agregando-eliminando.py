mascotas = [
    "Pelusa",
    "Wolfgang",
    "Pulga",
    "Felipe",
    "Chanchito Feliz",
    "Pulga"
]
mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")

# eliminar
mascotas.remove("Pulga")  # Elemento a elimiinar
mascotas.pop(1)
del mascotas[0]
mascotas.clear()  # se elimna todo el listado


print(mascotas)
