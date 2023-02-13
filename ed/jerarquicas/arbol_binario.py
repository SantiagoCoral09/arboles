from ed.jerarquicas.nodo_ab import NodoArbolBinario
from random import random
from ed.jerarquicas.excepciones import *


class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def adicionar(self, nueva_clave):
        self.raiz  =  self.__adicionar(self.raiz, nueva_clave)
        
    def __adicionar(self,sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbolBinario(nueva_clave)
        else:
            try:
                if self.raiz != None and type(nueva_clave) != type(self.raiz.clave):
                    raise TypeError(nueva_clave)
                elif random() <= 0.5: #Voy por la izq
                    nodo_izq= self.__adicionar(sub_arbol.izq, nueva_clave)
                    sub_arbol.izq = nodo_izq
                else: #me voy por derecha
                    sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)
            except TypeError as e:
                print(e)  
        return sub_arbol
    
    def buscar(self,clave_buscar):
        return self.__buscar(self.raiz, clave_buscar)
    
    def __buscar(self, sub_arbol, clave_buscar):
        if sub_arbol is not None:
            if sub_arbol.clave == clave_buscar:
                return sub_arbol.clave
            else:
                busc_izq = self.__buscar(sub_arbol.izq, clave_buscar)
                if busc_izq is not None:
                    return busc_izq
                busc_der = self.__buscar(sub_arbol.der, clave_buscar)
                if busc_der is not None:
                    return busc_der
        return None        
    
    def __len__ (self):
        return self.__tamaño(self.raiz)
    
    def __tamaño(self, sub_arbol):
        if sub_arbol is not None:
            return (1 + self.__tamaño(sub_arbol.izq) +  self.__tamaño(sub_arbol.der))
        return 0
    
    def hojas(self):
        cadena= self.__cadenaHojas(self.raiz)
        cadena=cadena[:-1]
        return cadena
    def __cadenaHojas(self, sub_arbol):
        cadena=""
        if sub_arbol!=None:
            if sub_arbol is self.raiz: #Es un nodo raiz
                
                cadena += (self.__cadenaHojas(sub_arbol.izq) + self.__cadenaHojas(sub_arbol.der))
            elif sub_arbol.izq == None and sub_arbol.der == None: #Es un nodo hoja
                cadena += (str(sub_arbol.clave) + "," + self.__cadenaHojas(sub_arbol.izq) + self.__cadenaHojas(sub_arbol.der))

            else: #Es un nodo interno
                cadena+= (self.__cadenaHojas(sub_arbol.izq) + self.__cadenaHojas(sub_arbol.der))
        return cadena    

    
    def internos(self):
        cadena= self.__cadenaInternos(self.raiz)
        cadena=cadena[:-1]
        return cadena
    def __cadenaInternos(self, sub_arbol):
        cadena=""
        if sub_arbol!=None:
            if sub_arbol is self.raiz: #Es un nodo raiz
                cadena += (self.__cadenaInternos(sub_arbol.izq) + self.__cadenaInternos(sub_arbol.der))
            elif sub_arbol.izq == None and sub_arbol.der == None: #Es un nodo hoja
                cadena += (self.__cadenaInternos(sub_arbol.izq) + self.__cadenaInternos(sub_arbol.der))

            else: #Es un nodo interno
                cadena += (str(sub_arbol.clave) + "," + self.__cadenaInternos(sub_arbol.izq) + self.__cadenaInternos(sub_arbol.der))
        return cadena   

    def altura(self):
        return self.__alturaArbol(self.raiz)
    def __alturaArbol(self,sub_arbol):
        if sub_arbol == None:
            return 0
            # if sub_arbol.izq==None and sub_arbol.der==None: #es una hoja
            #     return -1
        else:
            return 1+ max(self.__alturaArbol(sub_arbol.izq),self.__alturaArbol(sub_arbol.der))

if __name__=="__main__":
    arb=ArbolBinario()
    lista=[50,40,60,55,30,35,25,32,41,75,86,77,65,68,"50"]
    for i in lista:
        print(arb.adicionar(i))

    print("Buscar:", arb.buscar(8))
    # print("Minimo:",arb.elementoMinimoV1(arb))
    # print("Maximo:",arb.elementoMaximoV2(arb))

    # print("inOrden\n")
    # print(arb.imprimir(2))
    # print("preOrden\n")
    # arb.recorrerPreOrder(arb.raiz)
    # print("postOrden\n")
    # arb.recorrerPostOrder(arb.raiz)

    print("\nHojas")
    print(arb.hojas())
    print("\nInternos")
    print(arb.internos())
    # print("\nCuantas hojas")
    # print(arb.cuantashojas())
    print("\nAltura")
    print(arb.altura())
    print("Tamaño de ABB es:", len(arb))
