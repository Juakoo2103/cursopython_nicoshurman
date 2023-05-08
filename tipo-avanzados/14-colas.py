pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
uiltimoElemento = pila.pop()
print(uiltimoElemento)
print(pila)
print(pila[-1])
pila.pop()
pila.pop()
if not pila:
    print("pila vacia")
