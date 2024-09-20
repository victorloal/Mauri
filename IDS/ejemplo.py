from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QDesktopWidget
import sys
  
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.numero_nodos = 1
        # setting title
        self.setWindowTitle("IDS")
  
        # setting geometry
        self.setGeometry(100, 100, 600, 400)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
    # method for widgets
    def UiComponents(self):
        # Añadir un layout
        #saber el maximo de la pantalla
        
        desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry()

        max_width = screen_rect.width()
        max_height = screen_rect.height()

        
        self.boton_redondo = QPushButton("Raiz", self)

        # Establecer geometría correctamente
        self.boton_redondo.setGeometry(int(max_width/2)-50, 50, 100, 100)

        # Aplicar hoja de estilo para hacer que el QPushButton sea redondo
        self.boton_redondo.setStyleSheet("QPushButton { background-color: rgb(153, 193, 241); border-radius: 50px; }")
        
        # Conectar el botón a la función nodo_grafico
        self.boton_redondo.clicked.connect(self.nodo_grafico)
        
        self.showMaximized()
        
        
    def nodo_grafico(self):
        self.numero_nodos += 1
        # Obtener el objeto QPushButton que emitió la señal
        boton = self.sender()

        # Crear un nuevo botón redondo
        nuevo_boton = QPushButton(f"Nivel {self.numero_nodos}", self)

        # Establecer geometría correctamente
        x, y = boton.pos().x(), boton.pos().y()
        # odtener la posición del boton
        # odtener el tamaño del boton
        
        width, height = boton.width(), boton.height()
        
        
        nuevo_boton.setGeometry(x, y + 50 +height, 100, 100)

        # Aplicar hoja de estilo para hacer que el QPushButton sea redondo
        nuevo_boton.setStyleSheet("QPushButton { background-color: rgb(130,207,22); border-radius: 50px; }")
        
        # Mostrar el nuevo botón en la ventana
        nuevo_boton.show()
        nuevo_boton.clicked.connect(self.nodo_grafico)
        
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())
