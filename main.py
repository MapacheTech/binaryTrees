from lib import *

inOrderArr = []

preOrderArr = []

postOrderArr = []



nodo1 = nodo(1)

nodo2 = nodo(2)

nodo3 = nodo(3)

nodo4 = nodo(4)

nodo5 = nodo(5)

nodo6 = nodo(6)

nodo7 = nodo(7)

linkHijo(nodo1, nodo2, nodo3)
linkHijo(nodo2, nodo4, nodo5)
linkHijo(nodo3, nodo6, nodo7)


print("In order:")
LVR(nodo1, inOrderArr)

print(inOrderArr)

print("Pre Order:")
VLR(nodo1 , preOrderArr)

print(preOrderArr)

print("Post Order:")
LRV(nodo1, postOrderArr)

print(postOrderArr)

print("-------------------------------------------------------------------")

arrNodos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
nodoRaiz = None

for i in range(0,len(arrNodos),1):
    if i == 0:
        nodoRaiz = nodo(arrNodos[i])
    else:
        nodosOrdenados(nodoRaiz, nodo(arrNodos[i]))
    
    pass



"""nodoRaiz = nodo(16)
nodo9 = nodo(5)
nodo10 = nodo(7)
nodo11 = nodo(12)
nodo12 = nodo(9)
nodo13 = nodo(20)
nodo14 = nodo(18)
nodo15 = nodo(3)
nodo16 = nodo(10)
nodo17 = nodo(14)"""



print("Inicio nodos ordenados")

"""nodosOrdenados(nodoRaiz, nodo9)
nodosOrdenados(nodoRaiz, nodo10)
nodosOrdenados(nodoRaiz, nodo11)
nodosOrdenados(nodoRaiz, nodo12)
nodosOrdenados(nodoRaiz, nodo13)
nodosOrdenados(nodoRaiz, nodo14)
nodosOrdenados(nodoRaiz, nodo15)
nodosOrdenados(nodoRaiz, nodo16)
nodosOrdenados(nodoRaiz, nodo17)"""
printArbol(nodoRaiz)
"""print(nodo9.getArbol())
print(nodo10.getArbol())
print(nodo11.getArbol())
print(nodo12.getArbol())
print(nodo13.getArbol())
print(nodo14.getArbol())
print(nodo15.getArbol())
print(nodo16.getArbol())
print(nodo17.getArbol())"""


print("------------------------------------------------------------------")

preOrderNR = []
inOrderNR = []
postOrderNR = []

VLR(nodoRaiz, preOrderNR)
print("Pre order: ")
print(preOrderNR)

LVR(nodoRaiz, inOrderNR)
print("In order: ")
print(inOrderNR)

LRV(nodoRaiz, postOrderNR)
print("Post Order: ")
print(postOrderNR)


print("-----------------------------------------------------------------------")

nodoRaiz =nodo(arraynum[0])
cola = []
cola.append(nodoRaiz)
def agregaNodos(currentNodo,):
    
    currentNodo = cola.pop()
    
    if currentNodo.izq is None:
        currentNodo.izq = nodo(arraynum[i])
        return 0
    if currentNodo.der is None:
        currentNodo.der = nodo(arraynum[i])
        return 0
    cola.append(currentNodo.izq)
    cola.append(currentNodo.der)
    
    agregaNodos(currentNodo,)