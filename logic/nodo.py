from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QColorDialog
from ui_py.ui_nodo import Ui_Form
  # Asegúrate de que este es el archivo generado por pyuic5


class Nodo(QtWidgets.QWidget, Ui_Form):
    def __init__(self, main_window, parent=None):
        super(Nodo, self).__init__(parent)
        self.main_window = main_window  # Referencia a la instancia de MainWindow
        self.setupUi(self)
        self.init_ui()
        self.padre: Nodo = None
        self.hijos = []
        self.id = None
        self.child_count = 0
        self.color_base = QtGui.QColor(170, 255, 255)
        self.max_darkness_level = 102
        self.name = None

    def init_ui(self):
        self.add.clicked.connect(self.agregar_hijo)
        self.delete_2.clicked.connect(self.eliminar_nodo)
        self.color.clicked.connect(self.seleccionar_color)
        self.lineEdit.textChanged.connect(self.main_window.llenar_treeWidget)
        

    def agregar_hijo(self):
        nuevo_hijo = Nodo(self.main_window, self)  # Pasar la instancia de MainWindow al nuevo hijo
        nuevo_hijo.padre = self
        self.delete_2.setVisible(False)
        self.fvgnvbghm.setVisible(False)
        self.child_count += 1

        darker_factor = min(120 + (self.child_count * 20), self.max_darkness_level)
        color_hijo = self.color_base.darker(darker_factor)
        nuevo_hijo.set_color(color_hijo)
        nuevo_hijo.color_base = color_hijo

        nuevo_hijo.lineEdit.setText(f"Hijo {self.child_count}")
        self.hijos.append(nuevo_hijo)

        self.repintar_hijos()

        # Ahora llamar a llenar_treeWidget desde la instancia de MainWindow
        self.main_window.llenar_treeWidget()

    def seleccionar_color(self):
        # Abre un diálogo de selección de color
        color = QColorDialog.getColor()

        if color.isValid():
            # Cambia el color del nodo actual y guarda el color base
            self.set_color(color)
            self.color.setStyleSheet(f"background-color: {color.name()};border: 1px solid black; border-radius: 5px; padding: 1px;")
            self.color_base = color  # Almacena el color base para los hijos

    def set_color(self, color):
        # Cambia el color del nodo al especificado
        self.color_base = color
        self.setStyleSheet(f"background-color: {color.name()};")
        self.color.setStyleSheet(f"background-color: {color.name()};border: 1px solid black; border-radius: 5px; padding: 1px;")

    def eliminar_hijo(self, nodo):
        # Elimina el nodo hijo de la lista de hijos
        if nodo in self.hijos:  # Remueve el widget del layout
            nodo.deleteLater()  # Marca el widget para ser eliminado de la memoria
            self.hijos.remove(nodo)  # Remueve el nodo de la lista de hijos
            self.child_count -= 1  # Actualiza el contador de hijos
            self.repintar_hijos()  # Repinta los nodos hijos en el layout
            self.delete_2.setVisible(self.child_count == 0)
            if self.child_count == 0:
                self.fvgnvbghm = QtWidgets.QWidget(self.widget_nodos)
                self.fvgnvbghm.setStyleSheet("border: 0px solid black; ")
                self.fvgnvbghm.setObjectName("fvgnvbghm")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.fvgnvbghm)
                self.gridLayout_2.setObjectName("gridLayout_2")
                spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
                spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
                self.Spin = QtWidgets.QDoubleSpinBox(self.fvgnvbghm)
                font = QtGui.QFont()
                font.setFamily("MS Reference Sans Serif")
                font.setPointSize(12)
                self.Spin.setFont(font)
                self.Spin.setStyleSheet("border: 1px solid black; border-radius: 5px; padding: 2px;\n"
        "background-color: rgb(255, 255, 255);")
                self.Spin.setObjectName("Spin")
                self.gridLayout_2.addWidget(self.Spin, 0, 1, 1, 1)
                self.nodos.addWidget(self.fvgnvbghm, 0, 0, 1, 1)
                
                # Ahora llamar a llenar_treeWidget desde la instancia de MainWindow
            self.main_window.llenar_treeWidget()

    def repintar_hijos(self):
        # Elimina los widgets del layout sin borrar el layout en sí
        for i in self.hijos:# Marca el widget para ser eliminado de la memoria
            self.nodos.removeWidget(i)
            
        # Repinta los nodos hijos en el layout
        for i, hijo in enumerate(self.hijos):
            row = i // 3
            col = i % 3
            self.nodos.addWidget(hijo, row, col)
            
        self.set_color(self.color_base)  # Restaura el color base

    def eliminar_nodo(self):
        padre = self.padre
        if padre is not None:
            padre.eliminar_hijo(self)  # Llama al método eliminar_hijo del padre para eliminar este nodo

        self.deleteLater()
        
     # Métodos para hacer la clase iterable
    def __iter__(self):
        """Inicializa el índice del iterador."""
        self._iterator_index = 0
        return self

    def __next__(self):
        """Devuelve el siguiente hijo si existe."""
        if self._iterator_index < len(self.hijos):
            result = self.hijos[self._iterator_index]
            self._iterator_index += 1
            return result
        else:
            raise StopIteration
        
    def get_value(self):
        return self.Spin.value() if hasattr(self, 'Spin') else 0
    
    def llenar_treeWidget(self, tree_widget_item=None):
        from logic.home import MainWindow
        if tree_widget_item is None:
            # Si es el nodo raíz, creamos el primer QTreeWidgetItem
            tree_widget_item = QtWidgets.QTreeWidgetItem([f"Nodo (Nivel {self.level})"])
            tree_widget_item.setBackground(0, QtGui.QBrush(self.color_base))
            MainWindow.treeWidget.addTopLevelItem(tree_widget_item)
        else:
            # Si no es la raíz, lo añadimos como hijo del nodo padre
            item = QtWidgets.QTreeWidgetItem([f"Nodo (Nivel {self.level})"])
            item.setBackground(0, QtGui.QBrush(self.color_base))
            tree_widget_item.addChild(item)
            tree_widget_item = item

        # Recursivamente añadimos los hijos de este nodo
        for hijo in self.hijos:
            hijo.llenar_treeWidget(tree_widget_item)

