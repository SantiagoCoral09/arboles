
from ed.jerarquicas.arbol_binario import ArbolBinario
from ed.jerarquicas.arbol_binario_busquesda import ArbolBinarioBusqueda
from ed.jerarquicas.excepciones import DuplicatedKeyError,TypeError
from ed.jerarquicas.recorridos import *


if __name__ == "__main__":
    
    # abb = ArbolBinarioBusqueda()
    
    # #for n in [4,7, 2, 7, 6, 5, 2]:
    # #    try:
    # #        abb.adicionar(n)
    # #    except DuplicatedKeyError as e:
    # #        print (e)
    # #print("Tamaño de ABB es:", len(abb))
    
    
    # try: 
    #     abb.adicionar(4)
    #     abb.adicionar(2)
    #     abb.adicionar(3)
    #     abb.adicionar(8)
    #     abb.adicionar(6)
    #     abb.adicionar(7)
    #     abb.adicionar(7)
    #     abb.adicionar("7")
        
    # except DuplicatedKeyError as e:
    #     print (e)
    # # except TypeError as e:
    # #     print (e)
        
    # print("Tamaño de ABB es:", len(abb))
    # print(abb.buscar(3))
    # print(abb.buscar(7))
    # print(abb.buscar(1))

    # class Persona:
    #     def __init__(self,nombre,edad, celular=""):
    #         self.nombre=nombre 
    #         self.edad=edad
    #         self.celular=celular
    #     def __str__(self):
    #         return f"[{self.nombre}/{self.edad}:{self.celular}]"
    #     def __gt__(self, otra_persona):
    #         if self.nombre>otra_persona.nombre:
    #             return True
    #         elif self.nombre==otra_persona.nombre and self.edad > otra_persona.edad:
    #             return True
    #         return False
    #     def __eq__(self, otra_persona):
    #         if self.nombre==otra_persona.nombre and self.edad == otra_persona.edad:
    #             return True
        
    # abbp=ArbolBinarioBusqueda()
    # abbp.adicionar(Persona("Ana",20,32115))
    # abbp.buscar(Persona("Ana",20))
    # print(abbp.buscar(Persona("Ana",20)))
    # abbp.adicionar(Persona("Juan",18))
    # abbp.adicionar(Persona("Carlos",30))
    # abbp.adicionar(Persona("Juan",20))
    # print ("Tamaño ABBP:", len(abbp))
    
    # p1=Persona("Ana",20)
    # p2=Persona("Carlos",5)
    # print(p1>p2) # False
    # print(p1<p2) # TRUE
    
    # preorden (abbp)
    arb=ArbolBinarioBusqueda()
    lista=[50,40,60,55,30,35,25,32,41,75,86,77,65,68]
    for i in lista:
        print(arb.adicionar(i))

    print("Buscar:", arb.buscar(86))
    print("Minimo:", arb.buscar_minimo())
    print("Maximo:", arb.buscar_maximo())
    print("preorden")
    preorden(arb)
    print("inorden")
    inorden(arb)
    print("postorden")
    postorden(arb)
    print("Cadena PreOrden")
    print(cad_preorden(arb))
    print("Cadena InOrden")
    print(cad_inorden(arb))
    print("Cadena PostOrden")
    print(cad_postorden(arb))
    print(f"borrar 40, mayor: {arb.borrar(40,True)}")
    print("Cadena PreOrden")
    print(cad_preorden(arb))
    print(f"borrar 60, menor: {arb.borrar(50,False)}")
    print("Cadena PreOrden")
    print(cad_preorden(arb))