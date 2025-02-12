import os
from random import randint
from PyQt5 import QtWidgets,QtGui
from IDS import Grafica, Pdf
from ui_py.ui_home import Ui_IDS 
from .nodo import Nodo  # Asegúrate de que el nombre del archivo es correcto
from IDS.Tree import Tree

class MainWindow(QtWidgets.QMainWindow, Ui_IDS):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.add_nodo_principal()
        self.pushButton.clicked.connect(self.calcular_resultado)

    def calcular_resultado(self):
        tree = Tree(self.nodo.lineEdit.text())
        self.nodo.id = 0
        # Call the standalone calcular_resultado method
        self.calcular_resultado_recursive(tree,self.nodo)
        # Abrir ventana para seleccionar la carpeta de guardado
        ruta_carpeta = QtWidgets.QFileDialog.getExistingDirectory(self, 'Seleccionar Carpeta', '')
        
        if ruta_carpeta:
            # Especificar el nombre del archivo PDF que deseas guardar
            nombre_pdf = "documento.pdf"  # Puedes cambiar esto según tu lógica
            ruta_completa = os.path.join(ruta_carpeta, nombre_pdf)
            
            # Llamar a tu método para obtener el resultado del árbol
            tree.get_result(ruta_carpeta)
            print(f"PDF guardado en {ruta_completa}")

    def calcular_resultado_recursive(self, tree,nodo):
        level = 0
        nombre = []
        valores = []
        for hijo in nodo:  # Assuming nodo is iterable, if it's a single node, adjust accordingly
            # comprobar si el hijo tiene un spinBox
            
            result = tree.add_node(hijo.lineEdit.text(), nodo.id, hijo.get_value())
            hijo.id = result.id 
            level = tree.get_level_key(result)
            nombre.append(hijo.lineEdit.text())
            valores.append(hijo.get_value())
            self.calcular_resultado_recursive(tree,hijo) 
        
        titulo = f"Generando gráfica de radar del nivel {level}"

        # Asegúrate de que los valores y nombres no estén vacíos
        if nombre and valores:
            grafica = Grafica.Grafica(nombre, valores, nodo.get_value())
            img = grafica.get_png()
            pdf = Pdf.PDF(titulo=titulo)
            pdf.crear_pagina(titulo, img)
            pdf.guardar_pdf()
        else:
            pass

    def add_nodo_principal(self):
        nodo_principal = Nodo(self)  # Pasar la instancia de MainWindow
        self.nodo = nodo_principal
        #odterner un color ramdon
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.nodo.color_base =  QtGui.QColor(color[0], color[1], color[2])
        nodo_principal.lineEdit.setText("Nodo Principal")
        self.scrollArea.setWidget(nodo_principal)
        self.llenar_treeWidget()
        
    def llenar_treeWidget(self):
        """Llena el treeWidget con la estructura de nodos."""
        self.treeWidget.clear()  # Limpia el árbol existente
        # Crea un nuevo elemento en el QTreeWidget para el nodo principal
        self._agregar_nodo_a_treeWidget(self.nodo, None)
        # Expande todos los nodos del QTreeWidget
        self.treeWidget.expandAll()

    def _agregar_nodo_a_treeWidget(self, nodo, tree_item_padre):
        """Agrega un nodo y sus hijos al treeWidget."""
        if nodo is None:
            return

        # Crea un QTreeWidgetItem para el nodo actual
        item_actual = QtWidgets.QTreeWidgetItem([nodo.lineEdit.text()])

        # Si es un nodo raíz, lo agregamos como toplevel en el treeWidget
        if tree_item_padre is None:
            self.treeWidget.addTopLevelItem(item_actual)
        else:
            # Si es un nodo hijo, lo agregamos al nodo padre
            tree_item_padre.addChild(item_actual)

        # Recorrer y agregar todos los hijos de este nodo
        for hijo in nodo.hijos:
            self._agregar_nodo_a_treeWidget(hijo, item_actual)
        

