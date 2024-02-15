from lib import *

nodo1 = nodo(2)

nodo2 = nodo(10)

nodo3 = nodo(5)

nodo1.izq = nodo3
nodo1.der = nodo2

print(nodo1)
