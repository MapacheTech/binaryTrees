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