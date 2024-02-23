import sys
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QHBoxLayout, QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QComboBox
import mysql.connector

def instituciones():
    # Crea la ventana de dialogo
    dialog = QDialog()
    dialog.setWindowTitle("Registro de Instituciones")
    dialog.setGeometry(100, 100, 600, 400)

    # Crea layout
    layout = QVBoxLayout()

    # Create el group box
    course_group_box = QGroupBox("Infomación de la Institución")
    course_layout = QGridLayout()
    course_group_box.setLayout(course_layout)

    # Crea el group box de los botones
    buttons_group_box = QGroupBox()
    buttons_layout = QHBoxLayout()
    buttons_group_box.setLayout(buttons_layout)

    #Crea los label y los inputs en variables
    fecha_label = QLabel("Fecha:")
    fecha_input = QLineEdit()
    fecha_input.setPlaceholderText("Formato: AAAA-MM-DD")
    nombre_label = QLabel("Nombre de la Institución:")
    nombre_input = QLineEdit()
    direccion_label = QLabel("Dirección:")
    direccion_input = QLineEdit()
    correo_label = QLabel("Correo:")
    correo_input = QLineEdit()
    telefonos_label = QLabel("Teléfonos:")
    telefonos_input = QLineEdit()
    nombre_contacto_label = QLabel("Nombre de contacto:")
    nombre_contacto_input = QLineEdit()
    grupo_label = QLabel("Grupo:")
    grupo_input = QLineEdit()
    tipo_institucion_label = QLabel("Tipo de Institución")
    tipo_institucion_input = QLineEdit()


    #Distribución de los componentes en el group box
    course_layout.addWidget(fecha_label, 0, 0)
    course_layout.addWidget(fecha_input, 0, 1)
    course_layout.addWidget(nombre_label, 1, 0)
    course_layout.addWidget(nombre_input, 1, 1)
    course_layout.addWidget(direccion_label, 2, 0)
    course_layout.addWidget(direccion_input, 2, 1)
    course_layout.addWidget(correo_label, 3, 0)
    course_layout.addWidget(correo_input, 3, 1)
    course_layout.addWidget(telefonos_label, 4, 0)
    course_layout.addWidget(telefonos_input, 4, 1)
    course_layout.addWidget(nombre_contacto_label, 5, 0)
    course_layout.addWidget(nombre_contacto_input, 5, 1)
    course_layout.addWidget(grupo_label, 6, 0)
    course_layout.addWidget(grupo_input, 6, 1)
    course_layout.addWidget(tipo_institucion_label, 6, 2)
    course_layout.addWidget(tipo_institucion_input, 6, 3)
    
    # Crea el botón "Registrar"
    next_button = QPushButton("Registrar")
    next_button.setFixedSize(250, 30)

    #PPosicipin del botón
    buttons_layout.addWidget(next_button)

    layout.addWidget(course_group_box)
    layout.addWidget(buttons_group_box)

    # Set the layout for the dialog
    dialog.setLayout(layout)

    # Conecta el botón con la función para guardar los datos
    next_button.clicked.connect(lambda: insert_data(dialog, fecha_input, nombre_input, direccion_input, correo_input, telefonos_input, nombre_contacto_input, grupo_input, tipo_institucion_input))

    return dialog

def insert_data(dialog, fecha_input, nombre_input, direccion_input, correo_input, telefonos_input, nombre_contacto_input, grupo_input, tipo_institucion_input):
    # Conexión a la BD y cursor
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )

    # Obtener el valor de los inputs
    fecha = fecha_input.text() or None
    nombre = nombre_input.text()
    direccion = direccion_input.text()
    correo = correo_input.text()
    telefonos = telefonos_input.text()
    nombre_contacto = nombre_contacto_input.text()
    grupo = grupo_input.text()
    tipo_institucion = tipo_institucion_input.text()

    # Guardar Instituciones
    query = "INSERT INTO fundaprocura.instituciones (fecha,nombre,direccion,correo,telefonos,nombre_contacto,grupo,tipo_institucion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor = cnx.cursor()
    cursor.execute(query, (fecha, nombre, direccion, correo, telefonos, nombre_contacto, grupo, tipo_institucion))
    cnx.commit()
    cursor.close()
    cnx.close()

    # Cierra la ventana
    dialog.close()