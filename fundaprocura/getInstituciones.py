from PyQt5.QtWidgets import QGroupBox, QGridLayout, QHBoxLayout, QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QComboBox, QPlainTextEdit, QTableView, QFormLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import mysql.connector

def getInstituciones():
    # Create the dialog
    dialog = QDialog()
    dialog.setWindowTitle("Lista de Instituciones")

    # Create the layout
    layout = QVBoxLayout()

    # Create the table view
    table_view = QTableView()
    table_view.setFixedSize(1000, 400)

    # Create the course information group box
    course_group_box = QGroupBox("Infomación de Institución")
    course_layout = QGridLayout()
    course_group_box.setLayout(course_layout)

    # Create the ID input
    id_label = QLabel("Buscar:")
    id_input = QComboBox()
    id_input.setFixedSize(250, 20)

        # Connection and cursor
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )

    # Get the instituciones
    query = "SELECT id, nombre FROM fundaprocura.instituciones"
    cursor = cnx.cursor()
    cursor.execute(query)
    instituciones = cursor.fetchall()
    id_input.addItem("Seleccione una institución")
    for institucion in instituciones:
        id_input.addItem(str(institucion[1]))
    cursor.close()
    cnx.close()

    course_layout.addWidget(id_label, 0,0)
    course_layout.addWidget(id_input, 0,1)

    # Create the buttons group box
    buttons_group_box = QGroupBox()
    buttons_layout = QHBoxLayout()
    buttons_group_box.setLayout(buttons_layout)

    next_button = QPushButton("Buscar")
    next_button.setFixedSize(250, 30)

    buttons_layout.addWidget(next_button)

    layout.addWidget(course_group_box)
    layout.addWidget(buttons_group_box)

    dialog.setLayout(layout)

    next_button.clicked.connect(lambda: search_institucion(id_input, dialog, layout, instituciones))

    return dialog

def search_institucion(id_input, dialog, layout, instituciones):
    # Find the index of the selected institution
    selected_institution_index = id_input.currentIndex()

    # If a valid institution is selected, get its id
    if selected_institution_index > 0:
        id = instituciones[selected_institution_index - 1][0]

    # Create the form group box
    form_group_box = QGroupBox("Infomación de Institución")
    form_layout = QFormLayout()
    form_group_box.setLayout(form_layout)

    # Create the line edits for the form
    fecha_line_edit = QLineEdit()
    nombre_line_edit = QLineEdit()
    direccion_line_edit = QLineEdit()
    correo_line_edit = QLineEdit()
    telefonos_line_edit = QLineEdit()
    contacto_line_edit = QLineEdit()
    grupo_line_edit = QLineEdit()
    tipo_line_edit = QLineEdit()

    # Load the data into the line edits
    query = f"SELECT fecha, nombre, direccion, correo, telefonos, nombre_contacto, grupo, tipo_institucion FROM fundaprocura.instituciones WHERE id = {id}"
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )
    cursor = cnx.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()
    if len(rows) > 0:
        for row in rows:
            fecha_line_edit.setText(str(row[0]))
            nombre_line_edit.setText(str(row[1]))
            direccion_line_edit.setText(str(row[2]))
            correo_line_edit.setText(str(row[3]))
            telefonos_line_edit.setText(str(row[4]))
            contacto_line_edit.setText(str(row[5]))
            grupo_line_edit.setText(str(row[6]))
            tipo_line_edit.setText(str(row[7]))

    # Add the line edits to the form layout
    form_layout.addRow("Fecha:", fecha_line_edit)
    form_layout.addRow("Intitución:", nombre_line_edit)
    form_layout.addRow("Dirección:", direccion_line_edit)
    form_layout.addRow("Correo:", correo_line_edit)
    form_layout.addRow("Teléfonos:", telefonos_line_edit)
    form_layout.addRow("Contácto:", contacto_line_edit)
    form_layout.addRow("Grupo:", grupo_line_edit)
    form_layout.addRow("Tipo:", tipo_line_edit)

    # Add the form group box to the layout
    layout.addWidget(form_group_box)

    # Set the layout for the dialog
    dialog.setLayout(layout)
    return dialog