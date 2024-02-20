import sys
from PyQt5.QtWidgets import QApplication, QMenuBar, QMenu, QAction, QMainWindow, QGridLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from donaciones import donacion
from instituciones import instituciones
from casos import casos
from historial_donaciones import historial_donaciones
from getDonaciones import getDonaciones
from getInstituciones import getInstituciones


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Crear botones
        self.donacion_button = QPushButton("Registrar Donación")
        self.getdonacion_button = QPushButton("Ver Donaciones")
        self.institucion_button = QPushButton("Registrar Institución")
        self.casos_button = QPushButton("Registrar Caso")
        self.historial_donaciones_button = QPushButton("Asignar donación a Caso")
        self.getinstituciones_button = QPushButton("Ver Instituciones")

        # Conectar botones a funciones
        self.donacion_button.clicked.connect(self.show_donacion_window)
        self.getdonacion_button.clicked.connect(self.show_getdonacion_window)
        self.institucion_button.clicked.connect(self.show_instutuciones_window)
        self.casos_button.clicked.connect(self.show_casos_window)
        self.historial_donaciones_button.clicked.connect(self.show_historial_donaciones_window)
        self.getinstituciones_button.clicked.connect(self.show_getinstituciones_window)

        # Crear layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.donacion_button)
        self.layout.addWidget(self.getdonacion_button)
        self.layout.addWidget(self.institucion_button)
        self.layout.addWidget(self.casos_button)
        self.layout.addWidget(self.historial_donaciones_button)
        self.layout.addWidget(self.getinstituciones_button)

        # Set the layout for the main window
        self.setLayout(self.layout)

    def show_donacion_window(self):
        # Crear y mostrar la ventana de donaciones
        self.donacion_window = donacion()
        self.donacion_window.show()

    def show_instutuciones_window(self):
        # Crear y mostrar la ventana de donaciones
        self.instituciones_window = instituciones()
        self.instituciones_window.show()

    def show_casos_window(self):
        # Crear y mostrar la ventana de donaciones
        self.casos_window = casos()
        self.casos_window.show()

    def show_getdonacion_window(self):
        # Crear y mostrar la ventana de donaciones
        self.getdonacion_window = getDonaciones()
        self.getdonacion_window.show()

    def show_historial_donaciones_window(self):
        # Crear y mostrar la ventana de donaciones
        self.historial_donaciones_window = historial_donaciones()
        self.historial_donaciones_window.show()    

    def show_getinstituciones_window(self):
        # Crear y mostrar la ventana de donaciones
        self.getinstituciones_window = getInstituciones()
        self.getinstituciones_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
