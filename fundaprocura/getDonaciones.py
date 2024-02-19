from PyQt5.QtWidgets import QGroupBox, QGridLayout, QHBoxLayout, QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QComboBox, QHeaderView, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import mysql.connector

def getDonaciones():
    # Create the dialog
    dialog = QDialog()
    dialog.setWindowTitle("Lista de donaciones")

    # Create the layout
    layout = QVBoxLayout()

    # Create the table view
    table_view = QTableView()
    table_view.setFixedSize(1500, 400)
    table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table_view.resizeRowsToContents()
    table_view.resizeColumnsToContents()    

    # Create the course information group box
    course_group_box = QGroupBox("Infomación de Donación")
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

    next_button.clicked.connect(lambda: search_donations(id_input, table_view, dialog, layout, instituciones))

    return dialog

def search_donations(id_input, table_view, dialog, layout, instituciones):
    # Create the model and load the data

    id = 0

   # Find the index of the selected institution
    selected_institution_index = id_input.currentIndex()

    # If a valid institution is selected, get its id
    if selected_institution_index > 0:
        id = instituciones[selected_institution_index - 1][0]

    model = QStandardItemModel()
    query = f"SELECT fecha_donancion, equipo, observaciones FROM fundaprocura.donaciones WHERE fk_institucion = {id}"
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
            items = [
                QStandardItem(str(item)) for item in row
            ]
            model.appendRow(items)
    else:
        model.appendRow([QStandardItem("No se encontraron donaciones con ese ID")])

    # Set the column titles
    model.setHorizontalHeaderLabels([ "Fecha", "Equipo", "Observaciones"])

    # Set the model for the table view
    table_view.setModel(model)

    # Add the table view to the layout
    layout.addWidget(table_view)

    # Set the layout for the dialog
    dialog.setLayout(layout)
    return dialog