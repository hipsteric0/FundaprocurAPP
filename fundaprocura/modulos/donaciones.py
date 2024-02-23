import sys
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QHBoxLayout, QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QComboBox, QPlainTextEdit
import mysql.connector

def donacion():
    # Create the dialog
    dialog = QDialog()
    dialog.setWindowTitle("Registro de donaciones")
    dialog.setGeometry(100, 100, 600, 400)

    # Create the layout
    layout = QVBoxLayout()

    # Create the course information group box
    course_group_box = QGroupBox("Infomación de Donación")
    course_layout = QGridLayout()
    course_group_box.setLayout(course_layout)

    # Create the buttons group box
    buttons_group_box = QGroupBox()
    buttons_layout = QHBoxLayout()
    buttons_group_box.setLayout(buttons_layout)

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

    # Conexión y cursor
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )

    # Obtener las instituciones
    query = "SELECT id, nombre FROM fundaprocura.instituciones"
    cursor = cnx.cursor()
    cursor.execute(query)
    instituciones = cursor.fetchall()
    institucion_input.addItem("Seleccione una institución")
    for institucion in instituciones:
        institucion_input.addItem(str(institucion[1]))
    cursor.close()
    cnx.close()

    course_layout.addWidget(fecha_label, 0, 0)
    course_layout.addWidget(fecha_input, 0, 1)
    course_layout.addWidget(equipo_label, 0, 2)
    course_layout.addWidget(equipo_input, 0, 3)
    course_layout.addWidget(observaciones_label, 2, 0)
    course_layout.addWidget(observaciones_input, 2, 1)
    course_layout.addWidget(institucion_label, 3, 0)
    course_layout.addWidget(institucion_input, 3, 1)
    
    # Add buttons to the buttons group box
    next_button = QPushButton("Registrar")
    next_button.setAutoDefault(False)
    next_button.setFixedSize(250, 30)

    buttons_layout.addWidget(next_button)

    layout.addWidget(course_group_box)
    layout.addWidget(buttons_group_box)

    # Set the layout for the dialog
    dialog.setLayout(layout)

    # Connect the buttons to their respective functions
    next_button.clicked.connect(lambda: insert_data(dialog, fecha_input, equipo_input, observaciones_input, institucion_input, instituciones))

    return dialog

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