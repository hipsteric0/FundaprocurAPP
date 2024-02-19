import sys
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QHBoxLayout, QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QComboBox, QPlainTextEdit
import mysql.connector

def historial_donaciones():
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

    caso_label = QLabel("Nombre:")
    caso_input = QComboBox()
    equipo_label = QLabel("Equipo:")
    equipo_input = QComboBox()
    fecha_prestada_label = QLabel("Fecha prestada:")
    fecha_prestada_input = QLineEdit()
    fecha_devolucion_label = QLabel("Fecha devolución:")
    fecha_devolucion_input = QLineEdit()

    # Conexión y cursor
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )

    # Obtener las casos
    query = "SELECT id, nombres, apellidos FROM fundaprocura.casos"
    cursor = cnx.cursor()
    cursor.execute(query)
    casos = cursor.fetchall()
    caso_input.addItem("Nombre")
    for caso in casos:
        caso_input.addItem(str(caso[1])+" "+str(caso[2]))
    cursor.close()


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
    cnx.close()

    course_layout.addWidget(caso_label, 0, 0)
    course_layout.addWidget(caso_input, 0, 1)
    course_layout.addWidget(equipo_label, 0, 2)
    course_layout.addWidget(equipo_input, 0, 3)
    course_layout.addWidget(fecha_prestada_label, 2, 0)
    course_layout.addWidget(fecha_prestada_input, 2, 1)
    course_layout.addWidget(fecha_devolucion_label, 2, 2)
    course_layout.addWidget(fecha_devolucion_input, 2, 3)
    
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
    next_button.clicked.connect(lambda: insert_data(dialog, caso_input, equipo_input, fecha_prestada_input, fecha_devolucion_input, casos, donaciones))

    return dialog

def insert_data(dialog, caso_input, equipo_input, fecha_prestada_input, fecha_devolucion_input, casos, donaciones):
    # Conexión a la BD y cursor
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )

    # Obtener el valor de los inputs
    caso = 0 or None
    equipo = 0 or None
    fecha_prestada = fecha_prestada_input.text() or None
    fecha_devolucion = fecha_devolucion_input.text() or None

   # Encuentra el índice de la institución seleccionada.
    selected_caso_index = caso_input.currentIndex()

    # Si se selecciona una institución válida y obetiene su ID.
    if selected_caso_index > 0:
        caso = casos[selected_caso_index - 1][0]

    
    # Encuentra el índice de la institución seleccionada.
    selected_equipo_index = equipo_input.currentIndex()

    # Si se selecciona una institución válida y obetiene su ID.
    if selected_caso_index > 0:
        equipo = donaciones[selected_equipo_index - 1][0]


    #Guardar donaciones
    query = "INSERT INTO fundaprocura.historico_donaciones (fk_caso, fk_donacion, fecha_prestada, fecha_devolucion) VALUES (%s,%s,%s,%s)"
    cursor = cnx.cursor()
    cursor.execute(query, (caso,equipo,fecha_prestada,fecha_devolucion))
    cnx.commit()
    cursor.close()
    cnx.close()

    # Cierra la ventana
    dialog.close()