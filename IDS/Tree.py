from IDS.Grafica import Grafica
from IDS.Pdf import PDF
import IDS.Nodo as nodo
import IDS.Math as math


class Tree:
    def __init__(self, name):
        self.root = nodo.Nodo(name, 0)
        self.leaves = []
        self.leaves.append(self.root)
        self.id = 1
    
    def add_node(self, name,  IdFather, value=None):
        father = self.getIdFather(IdFather)
        if father is None:
            return "padre no encontrado"
        new_node = nodo.Nodo(name, self.id, value, father)
        father.add_child(new_node)
        self.leaves.append(new_node)
        try:
            self.leaves.remove(father)
        except:
            pass
        self.id += 1
        return new_node
    
        
    
    def getIdFather(self, id, nodos=None):
        if nodos is None:
            nodos = self.leaves

        for leaf in nodos:
            try:
                if leaf.get_idNodo() == id:  
                    return leaf
                padre = self.getIdFather(id, [leaf.get_father()])
                if padre:
                    return padre
            except:
                pass
        return None



    def get_level_key(self,node):
        return node.get_level()

    def get_nodos_ordenados_por_nivel(self):
        lista_de_nodos = self.leaves
        nodos_ordenados_por_nivel = sorted(lista_de_nodos, key=self.get_level_key, reverse=True)
        return nodos_ordenados_por_nivel
    
    def get_result(self,ruta):
        self.auxNodos = self.get_nodos_ordenados_por_nivel()

        while True:
            nodo = self.auxNodos[0]
            nodoFather = nodo.get_father()
            if nodoFather:
                nodoFather.result()
                self.auxNodos.append(nodoFather)
                for nodo in nodoFather.get_children():
                    self.auxNodos.remove(nodo)
            else:
                break

        self.generar_pdf(ruta)
        
    def generar_pdf(self,ruta):
        pdf = PDF(titulo=f"Resultados: {str(self.root.name)}",ruta=ruta)  # Crear el PDF
        self.generar_pdf_recursivo(self.root, pdf)  # Generar el PDF recursivamente
        pdf.guardar_pdf()  

    
    def generar_pdf_recursivo(self, nodo, pdf):
        nombres = []
        valores = []
        titulo = f"Resultados de {nodo.get_name()}"
        
        # Obtener los hijos del nodo actual
        hijos = nodo.get_children()  # Asegúrate de que este método exista y funcione

        for hijo in hijos:
            # Agregar nombre y valor del hijo actual
            nombres.append(hijo.get_name()) 
            valores.append(hijo.get_value())
            
            # Llamar recursivamente a los hijos del hijo actual
            self.generar_pdf_recursivo(hijo, pdf)

        # Solo crear la gráfica si hay nombres y valores
        if nombres and valores:
            grafica = Grafica(nombres, valores, nodo.get_value())
            img = grafica.get_png()
            pdf.crear_pagina(titulo, img)  # Crear una página por cada nodo padre con sus hijos
        else:
            pass
  
        
    
    def calculate_average(self):
        
        return math.average()

    def add_leaf(self, leaf):
        self.leaves.append(leaf)
        leaf.set_father(self.root)
        self.root.add_child(leaf)
        
    def average(self):
        return math.average(self.root)
    
    def get_leaves(self):
        return self.leaves
    
    def get_root(self):
        return self.root
    
    def __str__(self, nodos=None):
        result = ""
        
        if nodos is None:
            nodos = self.leaves

        for leaf in nodos:
            result += leaf.get_name() + " --> " + str(leaf.get_value()) + "  level -->" + str(leaf.get_level()) + "\n"
            if leaf.get_father() is not None:
                result += self.__str__([leaf.get_father()])
        
        return result
    
    def pdf (self):
        
        pass
        
    