import sys
from PyQt5.QtWidgets import QApplication, QMenuBar, QMenu, QAction, QMainWindow, QGridLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QComboBox
from PyQt5.QtCore import Qt
from modulos.donaciones import donacion
from modulos.instituciones import instituciones
from modulos.casos import casos
from modulos.historial_donaciones import historial_donaciones
from modulos.getDonaciones import getDonaciones
from modulos.getInstituciones import getInstituciones
from modulos.getCasos import getCasos
from modulos.estadisticas import Estadisticas, EstadoCasos, CasosClasificacion

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a widget to hold the comboboxes
        combobox_widget = QWidget()
        combobox_layout = QHBoxLayout(combobox_widget)

        # Crear combobox
        self.combobox = QComboBox()
        self.combobox.addItem("Donaciones")
        self.combobox.addItem("Registrar Donación")
        self.combobox.addItem("Ver Donaciones")

        self.combobox2 = QComboBox()
        self.combobox2.addItem("Instituciones")
        self.combobox2.addItem("Ver Instituciones")
        self.combobox2.addItem("Registrar Institución")

        self.combobox3 = QComboBox()
        self.combobox3.addItem("Casos")
        self.combobox3.addItem("Registrar Caso")
        self.combobox3.addItem("Asignar donación a Caso")
        self.combobox3.addItem("Ver CASOS")

        self.combobox4 = QComboBox()
        self.combobox4.addItem("Filtros")
        self.combobox4.addItem("Estadisticas")
        self.combobox4.addItem("Número de casos por estado")
        self.combobox4.addItem("Número de casos por clafisicación")

        # Conectar el combobox a funciones
        self.combobox.currentIndexChanged.connect(self.combobox_selected)
        self.combobox2.currentIndexChanged.connect(self.combobox_selected2)
        self.combobox3.currentIndexChanged.connect(self.combobox_selected3)
        self.combobox4.currentIndexChanged.connect(self.combobox_selected4)

        # Add comboboxes to the layout
        combobox_layout.addWidget(self.combobox)
        combobox_layout.addWidget(self.combobox2)
        combobox_layout.addWidget(self.combobox3)
        combobox_layout.addWidget(self.combobox4)

        # Create a main layout
        self.layout = QVBoxLayout()

        # Add the combobox widget to the main layout
        self.layout.addWidget(combobox_widget)

        # Set the layout for the main window
        self.setLayout(self.layout)

        self.resize(500, 150)


    def combobox_selected(self, index):
        if index == 1:
            self.show_donacion_window()
        elif index == 2:
            self.show_getdonacion_window()


    def combobox_selected2(self, index2):
        if index2 == 1:
            self.show_getinstituciones_window()
        elif index2 == 2:
            self.show_instutuciones_window()


    def combobox_selected3(self, index3):
        if index3 == 1:
            self.show_casos_window()
        elif index3 == 2:
            self.show_historial_donaciones_window()
        elif index3 == 3:
            self.show_getcasos_window()

    def combobox_selected4(self, index4):
        if index4 == 1:
            self.show_estadisticas_window()
        elif index4 == 2:
            self.show_estadocaso_window()
        elif index4 == 3:
            self.show_casoclasificacion()

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

    def show_getcasos_window(self):
        # Crear y mostrar la ventana de donaciones
        self.getcasos_window = getCasos()
        self.getcasos_window.show()

    def show_estadisticas_window(self):
        # Crear y mostrar la ventana de donaciones
        self.estadistica_window = Estadisticas()
        self.estadistica_window.show()

    def show_estadocaso_window(self):
        # Crear y mostrar la ventana de donaciones
        self.estadocaso_window = EstadoCasos()
        self.estadocaso_window.show()

    def show_casoclasificacion(self):
        # Crear y mostrar la ventana de donaciones
        self.casoclasificacion_window = CasosClasificacion()
        self.casoclasificacion_window.show()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
