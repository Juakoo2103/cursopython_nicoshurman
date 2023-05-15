class Perro:
    # Propiedad de clase
    patas = 4
    ########################

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad
    
    

    def habla(self):
        print(f"{self.__nombre} dice: guau!")

    @classmethod  # se define un metodo para crear instancias por defecto de la clase
    def factory(cls):
        return cls("chanchito feliz", 4)


perro1 = Perro.factory()
perro1.habla()