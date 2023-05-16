class Animal:
    def comer(self):
        print('comiendo')

class Perro(Animal):
    def pasear(self):
        print('paseando')


class Chanchito(Animal):
    def programar(self):
        print('programando')

# HERENCIA MULTINIVEL ES RECOMEDABLE OCUPAR HASTA 2 NIVELES

chanchito = Chanchito()
chanchito.comer()
