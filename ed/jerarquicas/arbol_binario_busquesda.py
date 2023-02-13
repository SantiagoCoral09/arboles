from ed.jerarquicas.arbol_binario import ArbolBinario
from ed.jerarquicas.excepciones import DuplicatedKeyError,TypeError
from ed.jerarquicas.nodo_ab import NodoArbolBinario


class ArbolBinarioBusqueda (ArbolBinario):
    def adicionar(self, nueva_clave):
        self.raiz = self.__adicionar (self.raiz, nueva_clave)
        # return self.__adicionar (self.raiz, nueva_clave).clave
        
    def __adicionar (self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbolBinario(nueva_clave)
        else:
            try:
                if self.raiz != None and type(nueva_clave) != type(self.raiz.clave):
                    raise TypeError(nueva_clave)
                if sub_arbol.clave > nueva_clave: # por izquierda
                    sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
                elif sub_arbol.clave < nueva_clave: # por derecha
                    sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)
                else: # nueva_clave duplicada
                    raise DuplicatedKeyError(nueva_clave)  
            except DuplicatedKeyError as e:
                print(e)    
            except TypeError as e:
                print(e)                           
        return sub_arbol
    
    def buscar(self, clave_buscar):
        return self.__buscar(self.raiz, clave_buscar)
    
    def __buscar(self, sub_arbol, clave_buscar):
        if sub_arbol is not None:
            if sub_arbol.clave == clave_buscar:
                return sub_arbol.clave
            elif sub_arbol.clave > clave_buscar: # por izquierda
                return self.__buscar(sub_arbol.izq, clave_buscar)
            return self.__buscar(sub_arbol.der, clave_buscar) # por derecha
        return None

    def buscar_minimo(self):
        """Método que busca y retorna la CLAVE con menor valor del ABB,
        o retorna None cuando el ABB esté vacio.
        """
        if self.raiz == None:
            return None
        else:
            return self.__elementoMinimo(self.raiz)

    def __elementoMinimo(self,sub_arbol):
        #recursivo
        if sub_arbol.izq==None:
            return sub_arbol.clave#nodo.dato
        else:
            return self.__elementoMinimo(sub_arbol.izq)

    def buscar_maximo(self):
        """Método que busca y retorna la CLAVE con mayor valor del ABB,
        o retorna None cuando el ABB esté vacio.
        """ 
        if self.raiz == None:
            return None
        else:
            return self.__elementoMaximo(self.raiz)

    def __elementoMaximo(self,sub_arbol):
        #recursivo
        if sub_arbol.der==None:
            return sub_arbol.clave #nodo.dato
        else:
            return self.__elementoMaximo(sub_arbol.der)

    # def getMin(self):
    #     curr = self
    #     while curr.left is not None:
    #         curr = curr.left
    #     return curr.value

    # def getMax(self):
    #     curr = self
    #     while curr.right is not None:
    #         curr = curr.right
    #     return curr.value

    def __busca_nodo(self,dato):
        actual=None
        if self.raiz != None:
            actual=self.raiz
            while actual != None and dato!=actual.clave:
                if dato < actual.clave: #Mover a la izq
                    actual=actual.izq
                elif dato>actual.clave:
                    actual=actual.der
        return actual

    def borrar(self, clave_elimin, mayor=True):
        """Método que borra un nodo del ABB. Cuando el nodo a borrar tiene ambos hijos.

            1) si 'mayor' es True: se busca y reemplaza el nodo a borrar por el MAYOR de sus hijos menores.
            2) si 'mayor' es False: se busca y reeplaza el nodo a borrar por el MENOR de sus hijos mayores.
        """
        elemento=None
        posicion = self.__busca_nodo(clave_elimin)
        if posicion != None:
            elemento=posicion.clave
            self.raiz = self.__elimina_nodo(self.raiz, clave_elimin, mayor)

        return elemento   

    def __elimina_nodo(self,sub_arbol,dato,mayor):
        if sub_arbol == None:
            return None
        elif dato < sub_arbol.clave:
            sub_arbol.izq = self.__elimina_nodo(sub_arbol.izq, dato, mayor)
        elif dato > sub_arbol.clave:
            sub_arbol.der = self.__elimina_nodo(sub_arbol.der, dato, mayor)
        else:
            nodo_eliminar = sub_arbol
            if nodo_eliminar.der == None:
                sub_arbol = nodo_eliminar.izq
            elif nodo_eliminar.izq == None:
                sub_arbol = nodo_eliminar.der
            else:
                if mayor==True:
                    nodo_eliminar = self.__cambiarMayor(nodo_eliminar)
                else:
                    nodo_eliminar = self.__cambiarMenor(nodo_eliminar)
                nodo_eliminar = None
        return sub_arbol

    def __cambiarMayor(self,aux):##Cual es el hijo mayor de los izq
        cambio=aux
        otro=aux.izq
        while otro.der != None:
            cambio = otro
            otro = otro.der
        aux.clave = otro.clave
        if cambio == aux:
            cambio.izq = otro.izq
        else:
            cambio.der = otro.izq
        return otro    

    def __cambiarMenor(self,aux):##Cual es el hijo menor de los der
        cambio=aux
        otro=aux.der
        while otro.izq != None:
            cambio = otro
            otro = otro.izq
        aux.clave = otro.clave
        if cambio == aux:
            cambio.der = otro.der
        else:
            cambio.izq = otro.der
        return otro   