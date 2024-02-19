import sys
from PyQt5.QtWidgets import QApplication, QMenuBar, QMenu, QAction, QMainWindow, QGridLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from donaciones import donacion
from instituciones import instituciones
from casos import casos
from historial_donaciones import historial_donaciones
from getDonaciones import getDonaciones
from getInstituciones import getInstituciones


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create the main window layout
        self.main_widget = QWidget()
        self.layout = QVBoxLayout()

        # Create the menu bar
        self.menu_bar = QMenuBar()
        self.layout.addWidget(self.menu_bar)

        # Create the "Donaciones" menu
        self.donaciones_menu = QMenu("Donaciones", self)
        self.menu_bar.addMenu(self.donaciones_menu)
        self.instituciones_menu = QMenu("Instituciones", self)
        self.menu_bar.addMenu(self.instituciones_menu)
        self.casos_menu = QMenu("Casos", self)
        self.menu_bar.addMenu(self.casos_menu)

        # Crear acción para mostrar la ventana de donaciones
        self.donacion_action = QAction("Registrar Donación", self)
        self.donaciones_menu.addAction(self.donacion_action)
        self.getdonacion_action = QAction("Ver Donaciones", self)
        self.donaciones_menu.addAction(self.getdonacion_action)
        self.institucion_action = QAction("Registrar Institución", self)
        self.instituciones_menu.addAction(self.institucion_action)
        self.casos_action = QAction("Registrar Caso", self)
        self.casos_menu.addAction(self.casos_action)
        self.historial_donaciones_action = QAction("Asignar donación a Caso", self)
        self.casos_menu.addAction(self.historial_donaciones_action)
        self.getinstituciones_action = QAction("Ver Instituciones", self)
        self.instituciones_menu.addAction(self.getinstituciones_action)

        # Conectar la acción a un slot que muestre la ventana de donaciones
        self.donacion_action.triggered.connect(self.show_donacion_window)
        self.getdonacion_action.triggered.connect(self.show_getdonacion_window)
        self.institucion_action.triggered.connect(self.show_instutuciones_window)
        self.casos_action.triggered.connect(self.show_casos_window)
        self.historial_donaciones_action.triggered.connect(self.show_historial_donaciones_window)
        self.getinstituciones_action.triggered.connect(self.show_getinstituciones_window)

        # Set the layout for the main window
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

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

# print("Agregrar institución")
# fecha_institucion = input("Fecha: ")
# nombre = input("Nombre de institución: ")
# direccion = input("Direción: ")
# correo = input("Correo: ")
# telefonos = input("Telefonos: ")
# nombre_contacto = input("Nombre de contacto: ")
# grupo = input("Grupo: ")
# tipo_institucion = input("Tipo de institución: ")

# add_institucion = "INSERT INTO fundaprocura.instituciones (fecha,nombre,direccion,correo,telefonos,nombre_contacto,fk_grupo,fk_tipo_institucion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

# cursor.execute(add_institucion, (fecha_institucion ,nombre,direccion,correo,telefonos,nombre_contacto,grupo,tipo_institucion))

# print("Agregrar donación")
# fecha_donacion = input("Fecha de donación: ")
# equipo = input("Equipo: ")
# observaciones = input("Observaciones: ")
# institucion = input("Institución: ")

# add_institucion = "INSERT INTO fundaprocura.donaciones (fecha_donancion,equipo,observaciones,fk_institucion) VALUES (%s,%s,%s,%s)"

# cursor.execute(add_institucion, (fecha_donacion,equipo,observaciones,institucion))


# print("Agregrar caso")
# grupo = input("Grupo: ")
# fecha_caso = input("Fecha caso: ")
# ref = input("REF: ")
# cedula = input("Cedula: ")
# apellidos = input("Apellidos: ")
# nombres = input("Nombres: ")
# sexo = input("Sexo: ")
# direccion = input("Dirección: ")
# telefono = input("Telefono: ")
# locacion_don = input("Locación don.: ")
# fecha_accidente = input("Fecha del accidente: ")
# causa = input("Causa: ")
# lesion = input("Lesión: ")
# fecha_nacimiento = input("Fecha de nacimiento: ")
# lugar_nacimiento = input("Lugar de nacimiento: ")
# equipo_actual = input("Equipo actual: ")
# donacion = input("Donación: ")
# medidas = input("Medidas: ")
# medidas_instrucciones = input("Medidias instrucciones: ")
# ultima_medicion = input("Ultima medición: ")
# serie = input("Serial: ")
# control_WF = input("Control WF: ")
# nombre_familiar = input("Nombre familiar: ")
# cedula_familiar = input("Cedula familiar: ")
# direccion_familiar = input("Dirección familiar: ")
# telefono_familiar = input("Telefono familiar: ")
# recaudos = input("Recaudos: ")
# observaciones_comentarios = input("Observaciones - comentarios: ")
# fk_tipo_caso = input("Tipo de caso: ")
# fk_clasificacion = input("Clasificación: ")
# fk_estado = input("Estado: ")
# fk_municipio_ciudad = input("Municipio - Ciudad: ")
# fk_parentesco = input("Parentesco familiar: ")


# add_institucion = "INSERT INTO fundaprocura.casos (grupo,fecha,ref,cedula,apellidos,nombres,sexo,direccion,telefono,locacion_don,fecha_accidente,causa,lesion,fecha_nacimiento,lugar_nacimiento,equipo_actual,donacion,medidas,medidas_instrucciones,ultima_medicion,serie,control_WF,nombre_familiar,cedula_familiar,direccion_familiar,telefono_familiar,recaudos,observaciones_comentarios,fk_tipo_caso,fk_clasificacion,fk_esado,fk_municipio_ciudad,fk_parentesco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

# cursor.execute(add_institucion, (grupo,fecha_caso,ref,cedula,apellidos,nombres,sexo,direccion,telefono,locacion_don,fecha_accidente,causa,lesion,fecha_nacimiento,lugar_nacimiento,equipo_actual,donacion,medidas,medidas_instrucciones,ultima_medicion,serie,control_WF,nombre_familiar,cedula_familiar,direccion_familiar,telefono_familiar,recaudos,observaciones_comentarios,fk_tipo_caso,fk_clasificacion,fk_estado,fk_municipio_ciudad,fk_parentesco))

# print("Agregrar historial del caso")
# equipo = input("Equipo: ")
# fecha_donancion = input("Fecha de donación: ")
# donaciones = input("Donaciones: ")
# fecha_prestada = input("Fecha prestada: ")
# equipo_prestado = input("Equipo prestado: ")
# fecha_devolucion = input("Fecha devolución: ")
# fk_caso = input("Caso: ")
# fk_donacion = input("Donación: ")

# add_institucion = "INSERT INTO fundaprocura.historico_donaciones (equipo,fecha_donancion,donaciones,fecha_prestada,equipo_prestado,fecha_devolucion,fk_caso,fk_donacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

# cursor.execute(add_institucion, (equipo,fecha_donancion,donaciones,fecha_prestada,equipo_prestado,fecha_devolucion,fk_caso,fk_donacion))

# Ejecutar la consulta SELECT

# print("Lista de grupos de institución")
# cursor.execute("SELECT * FROM grupo")

# # Obtener todos los resultados de la consulta
# result = cursor.fetchall()

# # Imprimir los resultados
# for row in result:
#     print(row)


# print("Lista de Estados")
# # Ejecutar la consulta SELECT
# cursor.execute("SELECT * FROM estado")

# # Obtener todos los resultados de la consulta
# result2 = cursor.fetchall()

# # Imprimir los resultados
# for row in result2:
#     print(row)


# cnx.commit()

# cursor.close()
# cnx.close()