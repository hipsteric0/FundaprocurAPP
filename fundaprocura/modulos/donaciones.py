import sys
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QHBoxLayout, QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QComboBox, QPlainTextEdit
import mysql.connector

def donacion():
    # Crea la ventana
    dialog = QDialog()
    dialog.setWindowTitle("Registro de donaciones")
    dialog.setGeometry(100, 100, 600, 400)

    # Crea el layout
    layout = QVBoxLayout()

    # Creaa el cuadro de Información de donación
    course_group_box = QGroupBox("Infomación de Donación")
    course_layout = QGridLayout()
    course_group_box.setLayout(course_layout)

    # Craea el cuadro del botón
    buttons_group_box = QGroupBox()
    buttons_layout = QHBoxLayout()
    buttons_group_box.setLayout(buttons_layout)

    # Crea los labels e inputs
    fecha_label = QLabel("Fecha de donación:")
    fecha_input = QLineEdit()
    fecha_input.setFixedSize(250, 30)
    fecha_input.setPlaceholderText("Formato: AAAA-MM-DD")
    equipo_label = QLabel("Equipo:")
    equipo_input = QLineEdit()
    equipo_input.setFixedSize(250, 30)
    observaciones_label = QLabel("Observaciones:")
    observaciones_input = QPlainTextEdit()
    observaciones_input.setFixedSize(250, 100)
    institucion_label = QLabel("Institución:")
    institucion_input = QComboBox()

    # Conexión y cursor a la BD
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )

    # Obtener la lista de instituciones para el combobox
    query = "SELECT id, nombre FROM fundaprocura.instituciones"
    cursor = cnx.cursor()
    cursor.execute(query)
    instituciones = cursor.fetchall()
    institucion_input.addItem("Seleccione una institución")
    for institucion in instituciones:
        institucion_input.addItem(str(institucion[1]))
    cursor.close()
    cnx.close()

    #Posición de los Inputs
    course_layout.addWidget(fecha_label, 0, 0)
    course_layout.addWidget(fecha_input, 0, 1)
    course_layout.addWidget(equipo_label, 0, 2)
    course_layout.addWidget(equipo_input, 0, 3)
    course_layout.addWidget(observaciones_label, 2, 0)
    course_layout.addWidget(observaciones_input, 2, 1)
    course_layout.addWidget(institucion_label, 3, 0)
    course_layout.addWidget(institucion_input, 3, 1)
    
    # Agrega el botón Registrar
    next_button = QPushButton("Registrar")
    next_button.setAutoDefault(False)
    next_button.setFixedSize(250, 30)

    buttons_layout.addWidget(next_button)

    # Orden de los componentes
    layout.addWidget(course_group_box)
    layout.addWidget(buttons_group_box)

    # Agrega el layout en la ventana
    dialog.setLayout(layout)

    # Conecta el botón Registrar con la función insert_data
    next_button.clicked.connect(lambda: insert_data(dialog, fecha_input, equipo_input, observaciones_input, institucion_input, instituciones))

    return dialog

#Esta función guarda la información del formulario en la BD
def insert_data(dialog, fecha_input, equipo_input, observaciones_input, institucion_input, instituciones):
    # Conexión a la BD y cursor
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )

    # Obtener el valor de los inputs
    donation_date = fecha_input.text()
    equipment = equipo_input.text()
    observations = observaciones_input.toPlainText()
    institution = 0

   # Encuentra el índice de la institución seleccionada.
    selected_institution_index = institucion_input.currentIndex()

    # Si se selecciona una institución válida y obetiene su ID.
    if selected_institution_index > 0:
        institution = instituciones[selected_institution_index - 1][0]


    #Guardar donaciones
    query = "INSERT INTO fundaprocura.donaciones (fecha_donancion,equipo,observaciones,fk_institucion) VALUES (%s,%s,%s,%s)"
    cursor = cnx.cursor()
    cursor.execute(query, (donation_date,equipment,observations,institution))
    cnx.commit()
    cursor.close()
    cnx.close()

    # Cierra la ventana
    dialog.close()