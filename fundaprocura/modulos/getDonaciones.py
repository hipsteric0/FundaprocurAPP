from PyQt5.QtWidgets import QGroupBox, QGridLayout, QHBoxLayout, QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QComboBox, QHeaderView, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import mysql.connector

def getDonaciones():
    # Crea vetana
    dialog = QDialog()
    dialog.setWindowTitle("Lista de donaciones")

    # Crea el layout
    layout = QVBoxLayout()

    # Crea la tabla
    table_view = QTableView()
    table_view.setFixedSize(1000, 400)
    table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table_view.resizeRowsToContents()
    table_view.resizeColumnsToContents()    

    # Crea el cuadro de Información de la Donación
    course_group_box = QGroupBox("Infomación de Donación")
    course_layout = QGridLayout()
    course_group_box.setLayout(course_layout)

    # Crea el label y combobox de busqueda
    id_label = QLabel("Buscar:")
    id_input = QComboBox()
    id_input.setFixedSize(250, 20)

     # Conexión y cursor a la BD
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )

    # Query que obtiene las instituciones
    query = "SELECT id, nombre FROM fundaprocura.instituciones"
    cursor = cnx.cursor()
    cursor.execute(query)
    instituciones = cursor.fetchall()
    id_input.addItem("Seleccione una institución")
    for institucion in instituciones:
        id_input.addItem(str(institucion[1]))
    cursor.close()
    cnx.close()

    #Posición labels e inputs
    course_layout.addWidget(id_label, 0,0)
    course_layout.addWidget(id_input, 0,1)

    # Crea el cuadro del botón
    buttons_group_box = QGroupBox()
    buttons_layout = QHBoxLayout()
    buttons_group_box.setLayout(buttons_layout)

    #Botón buscar
    next_button = QPushButton("Buscar")
    next_button.setFixedSize(250, 30)

    buttons_layout.addWidget(next_button)

    #Orden de los componentes
    layout.addWidget(course_group_box)
    layout.addWidget(buttons_group_box)

    dialog.setLayout(layout)

    #Conecta el botón Buscar con la función search_donations
    next_button.clicked.connect(lambda: search_donations(id_input, table_view, dialog, layout, instituciones))

    return dialog


#Función que busca las donaciones
def search_donations(id_input, table_view, dialog, layout, instituciones):


    id = 0

   # Encuentra el índice de la institución seleccionada.
    selected_institution_index = id_input.currentIndex()

    # Si se selecciona una institución válida y obetiene su ID.
    if selected_institution_index > 0:
        id = instituciones[selected_institution_index - 1][0]

    model = QStandardItemModel()
    # Query que busca las donaciones que han sido realizadas por la institución seleccionada
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

    # Agrega la infomación al modelo de la tabla
    if len(rows) > 0:
        for row in rows:
            items = [
                QStandardItem(str(item)) for item in row
            ]
            model.appendRow(items)
    else:
        model.appendRow([QStandardItem("No se encontraron donaciones con ese ID")])

    # Titulos de las columnas de la tabla
    model.setHorizontalHeaderLabels([ "Fecha", "Equipo", "Observaciones"])

    table_view.setModel(model)

    layout.addWidget(table_view)

    dialog.setLayout(layout)
    return dialog