class Perro:
    # Propiedad de clase
    patas = 4
    ########################

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod  # se define un metodo COMUN para todas las instancias de la clase
    def habla(cls):
        print("guau!")

    @classmethod  # se define un metodo para crear instancias por defecto de la clase
    def factory(cls):
        return cls("chanchito feliz", 4)


Perro.habla()
perro1 = Perro("chanchito", 2)
perro2 = Perro("Felipe", 3)
perro3 = Perro.factory()
print(perro3.patas, perro3.edad, perro3.nombre)
