def __ver_nodo(sub_arbol, con_hijos=True):
    print(f"[{sub_arbol.clave}]")
    if con_hijos:
        print(('O' if sub_arbol.izq else 'X') + ' : ' + ('O' if sub_arbol.der else 'X'))

# #pre-orden
# def preorden(arbol_bin):
#     __preorden(arbol_bin.raiz)
# def __preorden(sub_arbol):
#     if sub_arbol:
#         print(sub_arbol)
#         __preorden(sub_arbol.izq)
#         __preorden(sub_arbol.der)

 # PRE-ORDEN
def preorden(arbol_bin):
    __preorden(arbol_bin.raiz)

def __preorden(sub_arbol):
    if sub_arbol:
        __ver_nodo(sub_arbol, False)
        __preorden(sub_arbol.izq)
        __preorden(sub_arbol.der)

def cad_preorden(arbol_bin, sep="^"):
    """Retorna una cadena en PRE-ORDEN, separando cada valor clave con 'sep'.
    """
    cadena =__cad_preorden(arbol_bin.raiz,sep)
    cadena = cadena[:-1]
    return cadena

def __cad_preorden(sub_arbol,sep):
    cadena=""
    if sub_arbol:
        cadena += str(sub_arbol.clave) + sep
        cadena +=__cad_preorden(sub_arbol.izq,sep)
        cadena +=__cad_preorden(sub_arbol.der,sep)
    return cadena

 # IN-ORDEN
def inorden(arbol_bin):
    __inorden(arbol_bin.raiz)

def __inorden(sub_arbol):
    if sub_arbol:
        __inorden(sub_arbol.izq)
        __ver_nodo(sub_arbol, False)
        __inorden(sub_arbol.der)

def cad_inorden(arbol_bin, sep="-"):
    """Retorna una cadena en IN-ORDEN, separando cada valor clave con 'sep'
    """
    cadena =__cad_inorden(arbol_bin.raiz,sep)
    cadena = cadena[:-1]
    return cadena

def __cad_inorden(sub_arbol,sep):
    cadena=""
    if sub_arbol:
        cadena +=__cad_inorden(sub_arbol.izq,sep)
        cadena += str(sub_arbol.clave) + sep
        cadena +=__cad_inorden(sub_arbol.der,sep)
    return cadena

 # POST-ORDEN
def postorden(arbol_bin):
    __postorden(arbol_bin.raiz)

def __postorden(sub_arbol):
    if sub_arbol:
        __postorden(sub_arbol.izq)
        __postorden(sub_arbol.der)
        __ver_nodo(sub_arbol, False)

# def cad_postorden(arbol_bin, sep="\\"):
#     """Retorna una cadena en POST-ORDEN, separando cada valor clave con 'sep'.
#     """
#     cadena =__cad_postorden(arbol_bin.raiz,sep)
#     cadena = cadena[:-1]
#     return cadena

# def __cad_postorden(sub_arbol,sep):
#     cadena=""
#     if sub_arbol:
#         cadena +=__cad_postorden(sub_arbol.izq,sep)
#         cadena +=__cad_postorden(sub_arbol.der,sep)
#         cadena += str(sub_arbol.clave) + sep

#     return cadena
def cad_postorden(arbol_bin, sep="\\"):
    """Retorna una cadena en POST-ORDEN, separando cada valor clave con 'sep'.
    """
    cadena=""
    lista=[]
    conta=1
    # # cadena = cadena[:-1]
    # return lista1
    __cad_postorden(arbol_bin.raiz,lista)
    
    for item in lista:
        if conta<len(lista):
            cadena+=f"{str(item)}{sep}"
        else:
            cadena+=f"{str(item)}"
        conta+=1

    return cadena

def __cad_postorden(sub_arbol,lista):
    if sub_arbol:
        lista.append(sub_arbol.clave)
        # print(lista)
        __cad_postorden(sub_arbol.izq,lista)
        __cad_postorden(sub_arbol.der,lista)
    

    return lista