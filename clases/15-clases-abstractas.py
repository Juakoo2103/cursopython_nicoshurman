# Permite no crear instancias abstractas com un model = Model()
from abc import ABC, abstractclassmethod


class Model(ABC):
    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    @property
    @abstractclassmethod
    def tabla(self):
        pass

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()

usuario.guardar()
Usuario.buscar_por_id(123)
