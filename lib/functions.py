from .classes import *

def linkHijo(nodoPadre, nodoHijoIz=None,nodoHijoDer=None):
    if nodoHijoIz is not None:
        nodoPadre.izq = nodoHijoIz
    if nodoHijoDer is not None:
        nodoPadre.der = nodoHijoDer
    pass

def LVR(Nodo, inOrderArr):
    if Nodo is not None:
        nodoPadre = Nodo
        LVR(nodoPadre.izq, inOrderArr)
        inOrderArr.append(nodoPadre.valor)
        LVR(nodoPadre.der, inOrderArr)
    else:
        pass
    
    return inOrderArr

def VLR(Nodo, preOrderArr):
    if Nodo is not None:
        nodoPadre = Nodo
        preOrderArr.append(nodoPadre.valor)
        LVR(nodoPadre.izq, preOrderArr)        
        LVR(nodoPadre.der, preOrderArr)
    else:
        pass
    
    return preOrderArr

def LRV(Nodo, postOrderArr):
    if Nodo is not None:
        nodoPadre = Nodo
        LVR(nodoPadre.izq, postOrderArr)        
        LVR(nodoPadre.der, postOrderArr)
        postOrderArr.append(nodoPadre.valor)        
    else:
        pass
    
    return postOrderArr

def nodosOrdenados(nodoPadre, newNodo):
    if newNodo.valor < nodoPadre.valor:
        if nodoPadre.izq is None:
            nodoPadre.izq = newNodo
        else:
            nodosOrdenados(nodoPadre.izq, newNodo)
    if newNodo.valor > nodoPadre.valor:
        if nodoPadre.der is None:
            nodoPadre.der = newNodo
        else:
            nodosOrdenados(nodoPadre.der, newNodo)
    pass

def printArbol(Nodo):
    if Nodo is not None:
        nodoPadre = Nodo
        print(nodoPadre.getArbol())
        printArbol(nodoPadre.izq,)        
        printArbol(nodoPadre.der)
    return 0

def agregaNodos(currentNodo, nuevoNumero):
    cola = []
    cola.append(currentNodo)
    
    while cola:
          
        currentNodo = cola.pop(0)
        
        if currentNodo.izq is None:
            currentNodo.izq = nodo(nuevoNumero)
            return 0
        if currentNodo.der is None:
            currentNodo.der = nodo(nuevoNumero)
            return 0
        cola.append(currentNodo.izq)
        cola.append(currentNodo.der)
        
    return 0