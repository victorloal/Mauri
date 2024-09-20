from random import randint
import sys
from PyQt5 import QtWidgets,QtGui
from ui_home import Ui_MainWindow 
from nodo import Nodo  # Asegúrate de que el nombre del archivo es correcto

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.add_nodo_principal()

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
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())
    
