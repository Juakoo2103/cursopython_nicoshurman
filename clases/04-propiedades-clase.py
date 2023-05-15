class Perro:
    patas = 4
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice : guau!")

Perro.patas = 3
mi_perro = Perro("chanchito", 1)
mi_perro.patas = 5  # cambiamos solo el valor de la instancia si modificamos el valor que asignamos en la clase
mi_perro2 = Perro("Felipe", 1)
print(mi_perro.patas)
print(mi_perro2.patas)
print(Perro.patas)