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

        # Crea un widget para contener los comboboxes
        combobox_widget = QWidget()
        combobox_layout = QHBoxLayout(combobox_widget)

        # Crear combobox de Donaciones
        self.combobox = QComboBox()
        self.combobox.addItem("---Donaciones---")
        self.combobox.addItem("Registrar Donación")
        self.combobox.addItem("Ver Donaciones")

        # Crear combobox de Instituciones
        self.combobox2 = QComboBox()
        self.combobox2.addItem("---Instituciones---")
        self.combobox2.addItem("Ver Instituciones")
        self.combobox2.addItem("Registrar Institución")

        # Crear combobox de Casos
        self.combobox3 = QComboBox()
        self.combobox3.addItem("---Casos---")
        self.combobox3.addItem("Registrar Caso")
        self.combobox3.addItem("Asignar donación a Caso")
        self.combobox3.addItem("Buscar Casos")

        # Crear combobox de Filtros
        self.combobox4 = QComboBox()
        self.combobox4.addItem("---Filtros---")
        self.combobox4.addItem("Rango de edad")
        self.combobox4.addItem("Número de casos por estado")
        self.combobox4.addItem("Número de casos por clafisicación")

        # Conectar el combobox a funciones
        self.combobox.currentIndexChanged.connect(self.combobox_selected)
        self.combobox2.currentIndexChanged.connect(self.combobox_selected2)
        self.combobox3.currentIndexChanged.connect(self.combobox_selected3)
        self.combobox4.currentIndexChanged.connect(self.combobox_selected4)

        # Agrega comboboxes al layout
        combobox_layout.addWidget(self.combobox)
        combobox_layout.addWidget(self.combobox2)
        combobox_layout.addWidget(self.combobox3)
        combobox_layout.addWidget(self.combobox4)

        # Crea el layout principal
        self.layout = QVBoxLayout()

        # Agregar los comoboboxes al layout
        self.layout.addWidget(combobox_widget)

        # Layoyt de la pantala principal
        self.setLayout(self.layout)

        self.resize(500, 150)

    # Opciones del combobox Donaciones
    def combobox_selected(self, index):
        if index == 1:
            self.show_donacion_window()
        elif index == 2:
            self.show_getdonacion_window()

    # Opciones del combobox Instituciones
    def combobox_selected2(self, index2):
        if index2 == 1:
            self.show_getinstituciones_window()
        elif index2 == 2:
            self.show_instutuciones_window()

    # Opciones del combobox Casos
    def combobox_selected3(self, index3):
        if index3 == 1:
            self.show_casos_window()
        elif index3 == 2:
            self.show_historial_donaciones_window()
        elif index3 == 3:
            self.show_getcasos_window()

    # Opciones del combobox Filtros
    def combobox_selected4(self, index4):
        if index4 == 1:
            self.show_estadisticas_window()
        elif index4 == 2:
            self.show_estadocaso_window()
        elif index4 == 3:
            self.show_casoclasificacion()

    def show_donacion_window(self):
        # Crear y muestra la ventana de donaciones
        self.donacion_window = donacion()
        self.donacion_window.show()

    def show_instutuciones_window(self):
        # Crear y muestra la ventana de instituciones
        self.instituciones_window = instituciones()
        self.instituciones_window.show()

    def show_casos_window(self):
        # Crear y muestra la ventana de casos
        self.casos_window = casos()
        self.casos_window.show()

    def show_getdonacion_window(self):
        # Crear y muestra la ventana de ver donaciones
        self.getdonacion_window = getDonaciones()
        self.getdonacion_window.show()

    def show_historial_donaciones_window(self):
        # Crear y muestra la ventana de asignar donaciones
        self.historial_donaciones_window = historial_donaciones()
        self.historial_donaciones_window.show()    

    def show_getinstituciones_window(self):
        # Crear y muestra la ventana de ver instituciones
        self.getinstituciones_window = getInstituciones()
        self.getinstituciones_window.show()

    def show_getcasos_window(self):
        # Crear y muestra la ventana de ver casos
        self.getcasos_window = getCasos()
        self.getcasos_window.show()

    def show_estadisticas_window(self):
        # Crear y muestra la ventana de filtro 1
        self.estadistica_window = Estadisticas()
        self.estadistica_window.show()

    def show_estadocaso_window(self):
        # Crear y muestra la ventana de filtro 2
        self.estadocaso_window = EstadoCasos()
        self.estadocaso_window.show()

    def show_casoclasificacion(self):
        # Crear y muestra la ventana de filtro 3
        self.casoclasificacion_window = CasosClasificacion()
        self.casoclasificacion_window.show()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
