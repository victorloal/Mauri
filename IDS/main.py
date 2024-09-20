from Tree import Tree
class Main:
    def __init__(self,name):
        self.arbol = Tree(name)
        
    def agregar_nodo(self, nombre, id_padre, valor=None):
        self.arbol.add_node(nombre, id_padre, valor)
    
    def obtener_resultado(self):
        self.arbol.get_result()
        
main = Main("carro")
main.agregar_nodo("MOTOR",0)
main.agregar_nodo("CHASIS",0)
main.agregar_nodo("CARROCERIA",0)
# Agregamos nodos para el segundo nivel
main.agregar_nodo("CULATA",1,2)
main.agregar_nodo("CIGUEÑAL",1,5)
main.agregar_nodo("ARBOL DE LEVAS",1,2)
main.agregar_nodo("VALVULAS",1,3)
main.agregar_nodo("COMBUSTION",1,2.8)
main.agregar_nodo("CARTER",1,2.5)
# Agregamos nodos para el segundo nivel
main.agregar_nodo("SUSPENSION",2,2)
main.agregar_nodo("DIRECCION",2,2)
main.agregar_nodo("FRENOS",2,2.4)
main.agregar_nodo("TRANSMISION",2,3.5)
main.agregar_nodo("SIST. ELECTRICO ",2,1.5)
main.agregar_nodo("ESTRUCTURA",2,3.5)
# Agregamos nodos para el segundo nivel
main.agregar_nodo("FAROS",3,3)
main.agregar_nodo("PARACHOQUES",3,1)
main.agregar_nodo("LLANTAS",3,2)
main.agregar_nodo("PUERTAS",3,4)
main.agregar_nodo("LATONERIA",3,2)
main.agregar_nodo("COJINERIA",3,1)

main.obtener_resultado()

print(main.arbol.root.get_value())