from PyQt5.QtWidgets import QGroupBox, QGridLayout, QHBoxLayout, QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QComboBox, QMessageBox, QTableView, QFormLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import mysql.connector

def getInstituciones():
    # Crea vetana
    dialog = QDialog()
    dialog.setWindowTitle("Lista de Instituciones")

    # Crea el layout
    layout = QVBoxLayout()

    # Crea la tabla
    table_view = QTableView()
    table_view.setFixedSize(1000, 400)

    # Crea el cuadro información de institución
    course_group_box = QGroupBox("Infomación de Institución")
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

    #Conecta el botón Buscar con la función search_institution
    next_button.clicked.connect(lambda: search_institucion(id_input, dialog, layout, instituciones))

    return dialog


#Función que busca las instituciones
def search_institucion(id_input, dialog, layout, instituciones):

    # Encuentra el índice de la institución seleccionada.
    selected_institution_index = id_input.currentIndex()

     # Si se selecciona una institución válida y obetiene su ID.
    if selected_institution_index > 0:
        id = instituciones[selected_institution_index - 1][0]

     # Crea el cuadro información de institución
    form_group_box = QGroupBox("Infomación de Institución")
    form_layout = QFormLayout()
    form_group_box.setLayout(form_layout)

    # Crea los inputs
    fecha_line_edit = QLineEdit()
    nombre_line_edit = QLineEdit()
    direccion_line_edit = QLineEdit()
    correo_line_edit = QLineEdit()
    telefonos_line_edit = QLineEdit()
    contacto_line_edit = QLineEdit()
    grupo_line_edit = QLineEdit()
    tipo_line_edit = QLineEdit()

    # Query que busca la información de la institución por el ID 
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

    #Guarda la información
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

    # Agrega la información a los inputs 
    form_layout.addRow("Fecha:", fecha_line_edit)
    form_layout.addRow("Intitución:", nombre_line_edit)
    form_layout.addRow("Dirección:", direccion_line_edit)
    form_layout.addRow("Correo:", correo_line_edit)
    form_layout.addRow("Teléfonos:", telefonos_line_edit)
    form_layout.addRow("Contácto:", contacto_line_edit)
    form_layout.addRow("Grupo:", grupo_line_edit)
    form_layout.addRow("Tipo:", tipo_line_edit)

    # Agrega el form group box al layout
    layout.addWidget(form_group_box)

    # Create the buttons group box
    buttons_group_box = QGroupBox()
    buttons_layout = QHBoxLayout()
    buttons_group_box.setLayout(buttons_layout)

    update_button = QPushButton("Actualizar")
    update_button.setFixedSize(250, 30)
    buttons_layout.addWidget(update_button)

    # Agrega el botón al grupo de botones
    buttons_group_box.setLayout(buttons_layout)

    # Agrega el grupo de botones al layout
    layout.addWidget(buttons_group_box)

    # Conecta el botón "Actualizar" al método update_institucion
    update_button.clicked.connect(lambda: update_institucion(id_input, dialog, layout, fecha_line_edit, nombre_line_edit, direccion_line_edit, correo_line_edit, telefonos_line_edit, contacto_line_edit, grupo_line_edit, tipo_line_edit, instituciones))

    # Set the layout for the dialog
    dialog.setLayout(layout)
    return dialog

#Función para actuaslizar los datos de las instituciones
def update_institucion(id_input,dialog, layout, fecha_line_edit, nombre_line_edit, direccion_line_edit, correo_line_edit, telefonos_line_edit, contacto_line_edit, grupo_line_edit, tipo_line_edit, instituciones):
    
    # Encuentra el índice de la institución seleccionada.
    selected_institution_index = id_input.currentIndex()

    # Si se selecciona una institución válida y obetiene su ID.
    if selected_institution_index > 0:
        id = instituciones[selected_institution_index - 1][0]

    # Datos de los inputs
    fecha = fecha_line_edit.text() or None
    nombre = nombre_line_edit.text()
    direccion = direccion_line_edit.text()
    correo = correo_line_edit.text()
    telefonos = telefonos_line_edit.text()
    contacto = contacto_line_edit.text()
    grupo = grupo_line_edit.text()
    tipo = tipo_line_edit.text()

    # Query que actualiza los datos de la institución
    query = f"UPDATE fundaprocura.instituciones SET fecha = '{fecha}', nombre = '{nombre}', direccion = '{direccion}', correo = '{correo}', telefonos = '{telefonos}', nombre_contacto = '{contacto}', grupo = '{grupo}', tipo_institucion = '{tipo}' WHERE id = {id}"
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="fundaprocura"
    )
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


    QMessageBox.information(dialog, "Actualización exitosa", "Los datos de la institución han sido actualizados correctamente.")


    return dialog

