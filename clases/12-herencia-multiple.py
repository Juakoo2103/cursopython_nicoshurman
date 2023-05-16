class Animal:
    def comer(self):
        print('comiendo')

class Perro:
    def pasear(self):
        print('paseando')


class Chanchito(Perro, Animal):
    def programar(self):
        print('programando')

# ahora puedo acceder a los dos clases 
# idealmente no deben haber metodos duplicados dentro de la herencia