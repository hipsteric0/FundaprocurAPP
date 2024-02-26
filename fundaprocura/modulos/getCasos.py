import sys
import mysql.connector
from PyQt5.QtWidgets import QPlainTextEdit, QWidget, QLineEdit, QPushButton, QVBoxLayout, QListWidget, QListWidgetItem, QDialog, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QGridLayout, QComboBox
from PyQt5.QtCore import  Qt
from PyQt5 import QtCore

# Connect to the MySQL database
def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )
    return connection

# Search function
def search(name, connection, list_widget):
    cursor = connection.cursor()
    query = f"SELECT * FROM fundaprocura.casos WHERE CONCAT(nombres, ' ', apellidos) LIKE '%{name}%'"
    cursor.execute(query)
    results = cursor.fetchall()

    # Clear the list widget
    list_widget.clear()

    # Display the results
    for result in results:
        item = QListWidgetItem(f"Caso: {result[0]}, {result[7]}, {result[6]}, CI: {result[5]}")
        item.setData(QtCore.Qt.UserRole, result)
        list_widget.addItem(item)

# Function to display the details of a clicked item
def display_details(item):

    result = item.data(QtCore.Qt.UserRole)
    details_window = QDialog()
    details_window.setWindowTitle("Información del Caso")
    details_layout = QGridLayout()

    # Create the course information group box
    course_group_box = QGroupBox("Infomación Personal")
    course_layout = QGridLayout()
    course_group_box.setLayout(course_layout)

    # Create the buttons group box
    buttons_group_box = QGroupBox()
    buttons_layout = QHBoxLayout()
    buttons_group_box.setLayout(buttons_layout)

    grupo_label = QLabel("Grupo: ")
    grupo_input = QLineEdit()
    fecha_caso_label = QLabel("Fecha caso: ")
    fecha_caso_input = QLineEdit()
    fecha_caso_input.setPlaceholderText("Formato: AAAA-MM-DD")
    ref_label = QLabel("REF: ")
    ref_input = QLineEdit()
    cedula_label = QLabel("Cedula: ")
    cedula_input = QLineEdit()
    apellidos_label = QLabel("Apellidos: ")
    apellidos_input = QLineEdit()
    nombres_label = QLabel("Nombres: ")
    nombres_input = QLineEdit()
    sexo_label = QLabel("Sexo: ")
    sexo_input = QLineEdit()
    direccion_label = QLabel("Dirección: ")
    direccion_input = QLineEdit()
    direccion_input = QPlainTextEdit()
    direccion_input.setFixedSize(250, 80)
    telefono_label = QLabel("Telefonos: ")
    telefono_input = QLineEdit()
    telefono_input = QPlainTextEdit()
    telefono_input.setFixedSize(250, 80)
    correo_label = QLabel("Correo:")
    correo_input = QLineEdit()
    locacion_don_label = QLabel("Locación don.: ")
    locacion_don_input = QLineEdit()
    locacion_don_input = QPlainTextEdit()
    locacion_don_input.setFixedSize(250, 80)
    fecha_accidente_label = QLabel("Fecha del accidente: ")
    fecha_accidente_input = QLineEdit()
    fecha_accidente_input.setPlaceholderText("Formato: AAAA-MM-DD")
    causa_label = QLabel("Causa: ")
    causa_input = QLineEdit()
    lesion_label = QLabel("Lesión: ")
    lesion_input = QLineEdit()
    fecha_nacimiento_label = QLabel("Fecha de nacimiento: ")
    fecha_nacimiento_input = QLineEdit()
    fecha_nacimiento_input.setPlaceholderText("Formato: AAAA-MM-DD")
    lugar_nacimiento_label = QLabel("Lugar de nacimiento: ")
    lugar_nacimiento_input = QLineEdit()
    lugar_nacimiento_input = QPlainTextEdit()
    lugar_nacimiento_input.setFixedSize(250, 80)
    equipo_actual_label = QLabel("Equipo actual: ")
    equipo_actual_input = QLineEdit()
    donacion_label = QLabel("Donación: ")
    donacion_input = QLineEdit()
    medidas_label = QLabel("Medidas: ")
    medidas_input = QLineEdit()
    medidas_input = QPlainTextEdit()
    medidas_input.setFixedSize(250, 80)
    medidas_instrucciones_label = QLabel("Medidias instrucciones: ")
    medidas_instrucciones_input = QLineEdit()
    medidas_instrucciones_input = QPlainTextEdit()
    medidas_instrucciones_input.setFixedSize(250, 80)
    ultima_medicion_label = QLabel("Ultima medición: ")
    ultima_medicion_input = QLineEdit()
    ultima_medicion_input.setPlaceholderText("Formato: AAAA-MM-DD")
    serie_label = QLabel("Serial: ")
    serie_input = QLineEdit()
    control_WF_label = QLabel("Control WF: ")
    control_WF_input = QLineEdit()
    nombre_familiar_label = QLabel("Nombre familiar: ")
    nombre_familiar_input = QLineEdit()
    cedula_familiar_label = QLabel("Cedula familiar: ")
    cedula_familiar_input = QLineEdit()
    direccion_familiar_label = QLabel("Dirección familiar: ")
    direccion_familiar_input = QLineEdit()
    direccion_familiar_input = QPlainTextEdit()
    direccion_familiar_input.setFixedSize(250, 80)
    telefono_familiar_label = QLabel("Telefono familiar: ")
    telefono_familiar_input = QLineEdit()
    recaudos_label = QLabel("Recaudos: ")
    recaudos_input = QLineEdit()
    recaudos_input = QPlainTextEdit()
    recaudos_input.setFixedSize(250, 80)
    observaciones_comentarios_label = QLabel("Observaciones - comentarios: ")
    observaciones_comentarios_input = QLineEdit()
    observaciones_comentarios_input = QPlainTextEdit()
    observaciones_comentarios_input.setFixedSize(250, 80)
    fk_tipo_caso_label = QLabel("Tipo de caso: ")
    fk_tipo_caso_input = QLineEdit()
    fk_clasificacion_label = QLabel("Clasificación: ")
    fk_clasificacion_input = QLineEdit()
    fk_estado_label = QLabel("Estado: ")
    fk_estado_input = QLineEdit()
    fk_municipio_ciudad_label = QLabel("Municipio - Ciudad: ")
    fk_municipio_ciudad_input = QLineEdit()
    fk_parentesco_label = QLabel("Parentesco familiar: ")
    fk_parentesco_input = QLineEdit()


    course_layout.addWidget(grupo_label , 0, 0)
    grupo_input.setText(str(result[1]))
    course_layout.addWidget(grupo_input, 0, 1)

    course_layout.addWidget(fecha_caso_label,  0, 2)
    fecha_caso_input.setText(str(result[3]))
    fecha_caso_input.setReadOnly(True)
    course_layout.addWidget(fecha_caso_input, 0, 3)

    course_layout.addWidget(ref_label , 0, 4)
    ref_input.setText(str(result[4]))
    course_layout.addWidget(ref_input, 0, 5)

    course_layout.addWidget(fk_clasificacion_label , 0, 6)
    fk_clasificacion_input.setText(str(result[32]))
    fk_clasificacion_input.setReadOnly(True)
    course_layout.addWidget(fk_clasificacion_input, 0, 7)

    course_layout.addWidget(fk_tipo_caso_label , 1, 0)
    fk_tipo_caso_input.setText(str(result[2]))
    course_layout.addWidget(fk_tipo_caso_input, 1, 1)

    course_layout.addWidget(cedula_label, 1, 2)
    cedula_input.setText(str(result[5]))
    course_layout.addWidget(cedula_input, 1, 3)

    course_layout.addWidget(apellidos_label , 2, 0)
    apellidos_input.setText(str(result[6]))
    course_layout.addWidget(apellidos_input, 2, 1)

    course_layout.addWidget(nombres_label , 3, 0)
    nombres_input.setText(str(result[7]))
    course_layout.addWidget(nombres_input, 3, 1)

    course_layout.addWidget(sexo_label , 3, 2)
    sexo_input.setText(str(result[8]))
    course_layout.addWidget(sexo_input, 3, 3)

    course_layout.addWidget(fk_estado_label , 4, 2)
    fk_estado_input.setText(str(result[33]))
    fk_estado_input.setReadOnly(True)
    course_layout.addWidget(fk_estado_input, 4, 3)

    course_layout.addWidget(correo_label , 4, 4)
    correo_input.setText(str(result[11]))
    course_layout.addWidget(correo_input, 4, 5)

    course_layout.addWidget(fecha_nacimiento_label , 4, 6)
    fecha_nacimiento_input.setText(str(result[16]))
    fecha_nacimiento_input.setReadOnly(True)
    course_layout.addWidget(fecha_nacimiento_input, 4, 7)

    course_layout.addWidget(direccion_label , 5, 0)
    direccion_input.setPlainText(str(result[9]))
    course_layout.addWidget(direccion_input, 5, 1)

    course_layout.addWidget(fk_municipio_ciudad_label , 5, 2)
    fk_municipio_ciudad_input.setText(str(result[18]))
    course_layout.addWidget(fk_municipio_ciudad_input, 5, 3)

    course_layout.addWidget(telefono_label , 5, 4)
    telefono_input.setPlainText(str(result[10]))
    course_layout.addWidget(telefono_input, 5, 5)

    course_layout.addWidget(lugar_nacimiento_label , 5, 6)
    lugar_nacimiento_input.setPlainText(str(result[17]))
    course_layout.addWidget(lugar_nacimiento_input, 5, 7)

    course_layout.addWidget(locacion_don_label,  6, 2)
    locacion_don_input.setPlainText(str(result[12]))
    course_layout.addWidget(locacion_don_input, 6, 3)

    course_layout.addWidget(fecha_accidente_label , 7, 0)
    fecha_accidente_input.setText(str(result[13]))
    fecha_accidente_input.setReadOnly(True)
    course_layout.addWidget(fecha_accidente_input, 7, 1)

    course_layout.addWidget(causa_label, 8, 0)
    causa_input.setText(str(result[14]))
    course_layout.addWidget(causa_input, 8, 1)

    course_layout.addWidget(lesion_label , 8, 2)
    lesion_input.setText(str(result[15]))
    course_layout.addWidget(lesion_input, 8, 3)

    course_layout.addWidget(equipo_actual_label , 9, 0)
    equipo_actual_input.setText(str(result[19]))
    course_layout.addWidget(equipo_actual_input, 9, 1)

    course_layout.addWidget(donacion_label , 10, 0)
    donacion_input.setText(str(result[20]))
    course_layout.addWidget(donacion_input, 10, 1)

    course_layout.addWidget(medidas_label,  11, 0)
    medidas_input.setPlainText(str(result[21]))
    course_layout.addWidget(medidas_input, 11, 1)

    course_layout.addWidget(medidas_instrucciones_label , 11, 2)
    medidas_instrucciones_input.setPlainText(str(result[22]))
    course_layout.addWidget(medidas_instrucciones_input, 11, 3)

    course_layout.addWidget(ultima_medicion_label, 11, 4)
    ultima_medicion_input.setText(str(result[23]))
    ultima_medicion_input.setReadOnly(True)
    course_layout.addWidget(ultima_medicion_input, 11, 5)

    course_layout.addWidget(serie_label , 12, 0)
    serie_input.setText(str(result[24]))
    course_layout.addWidget(serie_input, 12, 1)

    course_layout.addWidget(control_WF_label , 12, 2)
    control_WF_input.setText(str(result[25]))
    course_layout.addWidget(control_WF_input, 12, 3)

    course_layout.addWidget(nombre_familiar_label , 13, 0)
    nombre_familiar_input.setText(str(result[26]))
    course_layout.addWidget(nombre_familiar_input, 13, 1)

    course_layout.addWidget(cedula_familiar_label , 14, 0)
    cedula_familiar_input.setText(str(result[27]))
    course_layout.addWidget(cedula_familiar_input, 14, 1)

    course_layout.addWidget(direccion_familiar_label , 14, 2)
    direccion_familiar_input.setPlainText(str(result[28]))
    course_layout.addWidget(direccion_familiar_input, 14, 3)

    course_layout.addWidget(fk_parentesco_label , 14, 4)
    fk_parentesco_input.setText(str(result[34]))
    fk_parentesco_input.setReadOnly(True)
    course_layout.addWidget(fk_parentesco_input, 14, 5)

    course_layout.addWidget(telefono_familiar_label,  15, 2)
    telefono_familiar_input.setText(str(result[29]))
    course_layout.addWidget(telefono_familiar_input, 15, 3)

    course_layout.addWidget(recaudos_label , 16, 0)
    recaudos_input.setPlainText(str(result[30]))
    course_layout.addWidget(recaudos_input, 16, 1)

    course_layout.addWidget(observaciones_comentarios_label, 17, 2)
    observaciones_comentarios_input.setPlainText(str(result[31]))
    course_layout.addWidget(observaciones_comentarios_input, 17, 3)

    historico = QListWidget()
    historico.setFixedSize(600, 100)

    id = result[0]

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )

    cursor = connection.cursor()
    query = """
    SELECT
                hd.id AS id_historico,
                hd.fecha_prestada AS fecha_prestada,
                hd.equipo AS equipo_prestado,
                hd.fecha_devolucion AS fecha_devolucion,
                d.id AS id_donacion,
                d.fecha_donancion AS fecha_donacion,
                d.equipo AS equipo_donado,
                d.observaciones AS observaciones,
                i.nombre AS institucionhistorico_donaciones
            FROM
                fundaprocura.historico_donaciones hd
            JOIN
                fundaprocura.donaciones d ON hd.fk_donacion = d.id
            JOIN
                fundaprocura.casos c ON hd.fk_caso = c.id
            JOIN
                fundaprocura.instituciones i ON d.fk_institucion = i.id
            WHERE
                c.id = %s
            ORDER BY
                hd.fecha_prestada ASC;"""
    cursor.execute(query, (id,))
    results = cursor.fetchall()

    # Clear the list widget
    historico.clear()

    # Display the results
    for result in results:
        item = QListWidgetItem(f"Fecha prestada: {result[1]}, Fecha devolución: {result[3]}, Equipo: {result[6]}, Observaciones: {result[2]}")
        item.setData(QtCore.Qt.UserRole, result)
        historico.addItem(item)


        # Rest of the code remains the same
    lista_group_box = QGroupBox()
    lista_layaout = QHBoxLayout()
    lista_group_box.setLayout(lista_layaout)
    lista_layaout.addWidget(historico)

    buttons_group_box = QGroupBox()
    buttons_layout = QHBoxLayout()
    buttons_group_box.setLayout(buttons_layout)

    update_button = QPushButton("Actualizar")
    update_button.setFixedSize(250, 30)
    buttons_layout.addWidget(update_button)

    # Agrega el botón al grupo de botones
    buttons_group_box.setLayout(buttons_layout)

    # Agrega el grupo de botones al layout
    course_layout.addWidget(buttons_group_box)

    # Agrega el grupo de listas al layout
    course_layout.addWidget(lista_group_box)

    update_button.clicked.connect(lambda: insert_data(details_window,id,grupo_input, ref_input, cedula_input, apellidos_input, nombres_input,sexo_input, direccion_input, telefono_input,correo_input, locacion_don_input, causa_input, lesion_input, lugar_nacimiento_input, equipo_actual_input, donacion_input, medidas_input, medidas_instrucciones_input,  serie_input, control_WF_input, nombre_familiar_input, cedula_familiar_input, direccion_familiar_input, telefono_familiar_input, recaudos_input,fk_tipo_caso_input, fk_municipio_ciudad_input, observaciones_comentarios_input))

    # Set the layout for the dialog
    details_window.setLayout(course_layout)


    equipo_label = QLabel("Equipo:")
    equipo_input = QComboBox()
    fecha_prestada_label = QLabel("Fecha prestada:")
    fecha_prestada_input = QLineEdit()
    fecha_devolucion_label = QLabel("Fecha devolución:")
    fecha_devolucion_input = QLineEdit()
    observaciones_label = QLabel("Observaciones")
    observaciones_input = QPlainTextEdit()

    # Conexión y cursor
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )

     # Obtener donaciones
    query = "SELECT id, equipo FROM fundaprocura.donaciones"
    cursor = cnx.cursor()
    cursor.execute(query)
    donaciones = cursor.fetchall()
    equipo_input.addItem("Equipo")
    for donacion in donaciones:
        equipo_input.addItem(str(donacion[1]))
    cursor.close()
    cnx.close()

    course_layout.addWidget(equipo_label, 18, 1)
    course_layout.addWidget(equipo_input, 19, 1)
    course_layout.addWidget(fecha_prestada_label, 18, 3)
    course_layout.addWidget(fecha_prestada_input, 19, 3)
    course_layout.addWidget(fecha_devolucion_label, 18, 5)
    course_layout.addWidget(fecha_devolucion_input, 19, 5)
    course_layout.addWidget(observaciones_label, 18, 7)
    course_layout.addWidget(observaciones_input, 19 ,7)
    
    
    # Add buttons to the buttons group box
    next_button = QPushButton("Registrar")
    next_button.setAutoDefault(False)
    next_button.setFixedSize(250, 30)

    buttons_layout.addWidget(next_button)

    # Add the buttons group box to the course layout
    course_layout.addWidget(buttons_group_box, 20, 0, 1, 8)

    # Rest of the code remains the same

    # Set the layout for the dialog
    details_window.setLayout(course_layout)
    next_button.clicked.connect(lambda: insert_historico(details_window, id, equipo_input, fecha_prestada_input, fecha_devolucion_input, observaciones_input, donaciones))
    
    details_window.exec_()


def insert_data(details_window, id, grupo_input, ref_input, cedula_input, apellidos_input, nombres_input,sexo_input, direccion_input, telefono_input, correo_input, locacion_don_input,  causa_input, lesion_input, lugar_nacimiento_input, equipo_actual_input, donacion_input, medidas_input, medidas_instrucciones_input, serie_input, control_WF_input, nombre_familiar_input, cedula_familiar_input, direccion_familiar_input, telefono_familiar_input, recaudos_input,fk_tipo_caso_input, fk_municipio_ciudad_input, observaciones_comentarios_input):

    id = id
    grupo = grupo_input.text()
    ref = ref_input.text()
    cedula = int(cedula_input.text() or 0)
    apellidos = apellidos_input.text()
    nombres = nombres_input.text()
    sexo = sexo_input.text()
    direccion = direccion_input.toPlainText()
    telefono = telefono_input.toPlainText()
    correo = correo_input.text()
    locacion_don = locacion_don_input.toPlainText()
    causa = causa_input.text()
    lesion = lesion_input.text()
    lugar_nacimiento = lugar_nacimiento_input.toPlainText()
    equipo_actual = equipo_actual_input.text()
    donacion = donacion_input.text()
    medidas = medidas_input.toPlainText()
    medidas_instrucciones = medidas_instrucciones_input.toPlainText()
    serie = serie_input.text()
    control_WF = control_WF_input.text()
    nombre_familiar = nombre_familiar_input.text()
    cedula_familiar = int(cedula_familiar_input.text() or 0)
    direccion_familiar = direccion_familiar_input.toPlainText()
    telefono_familiar = telefono_familiar_input.text()
    recaudos = recaudos_input.toPlainText()
    observaciones_comentarios = observaciones_comentarios_input.toPlainText()
    fk_tipo_caso = fk_tipo_caso_input.text()
    fk_municipio_ciudad = fk_municipio_ciudad_input.text()
    


    # Insert the data
    query = "UPDATE fundaprocura.casos SET grupo=%s, tipo_caso=%s, ref=%s, cedula=%s, apellidos=%s, nombres=%s, sexo=%s, direccion=%s, telefono=%s, correo=%s, locacion_don=%s, causa=%s, lesion=%s, lugar_nacimiento=%s, municipio_ciudad=%s, equipo_actual=%s, donacion=%s, medidas=%s, medidas_instrucciones=%s, serie=%s, control_WF=%s, nombre_familiar=%s, cedula_familiar=%s, direccion_familiar=%s, telefono_familiar=%s, recaudos=%s, observaciones_comentarios=%s WHERE id=%s"
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )
    cursor = cnx.cursor()
    cursor.execute(query, (grupo,fk_tipo_caso,ref,cedula,apellidos,nombres,sexo,direccion,telefono,correo,locacion_don,causa,lesion,lugar_nacimiento,fk_municipio_ciudad,equipo_actual,donacion,medidas,medidas_instrucciones,serie,control_WF,nombre_familiar,cedula_familiar,direccion_familiar,telefono_familiar,recaudos,observaciones_comentarios, id))
    cnx.commit()
    cursor.close()
    cnx.close()

    details_window.close()


def insert_historico(details_window, id, equipo_input, fecha_prestada_input, fecha_devolucion_input, observaciones_input, donaciones):
    # Conexión a la BD y cursor
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )

    # Obtener el valor de los inputs
    caso = id
    equipo = 0 or None
    fecha_prestada = fecha_prestada_input.text() or None
    fecha_devolucion = fecha_devolucion_input.text() or None
    observaciones = observaciones_input.toPlainText()

    
    # Encuentra el índice de la institución seleccionada.
    selected_equipo_index = equipo_input.currentIndex()

    # Si se selecciona una institución válida y obetiene su ID.
    if selected_equipo_index > 0:
        equipo = donaciones[selected_equipo_index - 1][0]


    #Guardar donaciones
    query = "INSERT INTO fundaprocura.historico_donaciones (fk_caso, fk_donacion, fecha_prestada, fecha_devolucion, equipo) VALUES (%s,%s,%s,%s,%s)"
    cursor = cnx.cursor()
    cursor.execute(query, (caso,equipo,fecha_prestada,fecha_devolucion, observaciones))
    cnx.commit()
    cursor.close()
    cnx.close()

    details_window.close()



# PyQt5 application
class getCasos(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Buscar", self)
        self.setWindowTitle("Buscar Casos")
        self.resize(400, 400)
        self.list_widget = QListWidget(self)

        # Connect the button to the search function
        self.button.clicked.connect(lambda: search(self.line_edit.text(), self.connection, self.list_widget))

        # Connect the list widget to the display_details function
        self.list_widget.itemClicked.connect(display_details)

        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.list_widget)

        self.setLayout(self.layout)

        # Connect to the MySQL database
        self.connection = create_connection()

        self.show()