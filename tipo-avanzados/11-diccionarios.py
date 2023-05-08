# coleccion de datos agrupados por llave y valor
# la llave solo pueden ser strings

punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])  # accedes al valor mediante la KEY
print(punto["y"])  # accedes al valor mediante la KEY

punto["z"] = 45  # agregando una key
print(punto)

if "lala" in punto:
    print("encontre", punto["lala"])

print(punto.get("x"))
# Nos devuelve none en caso de que la llave no existe
print(punto.get("lala", 97))

del punto["x"]
del (punto["y"])

print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios =[
    {"id":1,"nombre":"chanchito"},
    {"id":2,"nombre":"feliz"},
    {"id":3,"nombre":"nicolas"},
    {"id":4,"nombre":"felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])