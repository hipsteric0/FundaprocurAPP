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
    # Clear the list widget
    list_widget.clear()

    cursor = connection.cursor()
    query = """
            SELECT
                hd.id AS id_historico,
                hd.fecha_prestada AS fecha_prestada,
                hd.equipo_prestado AS equipo_prestado,
                hd.fecha_devolucion AS fecha_devolucion,
                d.id AS id_donacion,
                d.fecha_donancion AS fecha_donacion,
                d.equipo AS equipo_donado,
                d.observaciones AS observaciones,
                i.nombre AS institucion,
                c.nombres AS nombres,
                c.apellidos AS apellidos,
                c.cedula AS cedula,
                c.id AS id_caso
            FROM
                fundaprocura.historico_donaciones hd
            JOIN
                fundaprocura.donaciones d ON hd.fk_donacion = d.id
            JOIN
                fundaprocura.casos c ON hd.fk_caso = c.id
            JOIN
                fundaprocura.instituciones i ON d.fk_institucion = i.id
            WHERE
                CONCAT(c.nombres, ' ', c.apellidos) LIKE '%{}%'
            ORDER BY
                hd.fecha_prestada ASC;
        """.format(name)

    cursor.execute(query)
    results = cursor.fetchall()

    # Display the results
    for result in results:
        item = QListWidgetItem(f"{result[9]}, {result[10]}, FECHA: {result[1]}")
        item.setData(QtCore.Qt.UserRole, result)
        list_widget.addItem(item)

# Function to display the details of a clicked item
def display_details(item):

    result = item.data(QtCore.Qt.UserRole)
    details_window = QDialog()
    details_window.setWindowTitle("Historial de donaciones")
    details_layout = QGridLayout()

    # Create the course information group box
    course_group_box = QGroupBox("Infomación Personal")
    course_layout = QGridLayout()
    course_group_box.setLayout(course_layout)

    # Create the buttons group box
    buttons_group_box = QGroupBox()
    buttons_layout = QHBoxLayout()
    buttons_group_box.setLayout(buttons_layout)

    fecha_donacion_label = QLabel("Fecha de donación:")
    fecha_donacion_input = QLineEdit()
    fecha_donacion_input.setReadOnly(True)
    donacion_label = QLabel("Equipo: ")
    donacion_input = QLineEdit()
    institucion_label = QLabel("Institución:")
    institucion_input = QLineEdit()
    fecha_prestada_dato_label = QLabel("Fecha prestada: ")
    fecha_prestada_dato_input = QLineEdit()
    fecha_prestada_dato_input.setPlaceholderText("Formato: AAAA-MM-DD")
    fecha_devolucion_dato_label = QLabel("Fecha devolución: ")
    fecha_devolucion_dato_input = QLineEdit()
    fecha_devolucion_dato_input.setPlaceholderText("Formato: AAAA-MM-DD")


    course_layout.addWidget(fecha_donacion_label,  0, 0)
    fecha_donacion_input.setText(str(result[5]))
    course_layout.addWidget(fecha_donacion_input, 0, 1)

    course_layout.addWidget(donacion_label,  1, 0)
    donacion_input.setText(str(result[6]))
    course_layout.addWidget(donacion_input, 1, 1)

    course_layout.addWidget(institucion_label,  1, 2)
    institucion_input.setText(str(result[8]))
    course_layout.addWidget(institucion_input, 1, 3)    

    course_layout.addWidget(fecha_prestada_dato_label , 1, 4)
    fecha_prestada_dato_input.setText(str(result[1]))
    course_layout.addWidget(fecha_prestada_dato_input, 1, 5)

    course_layout.addWidget(fecha_devolucion_dato_label, 1, 6)
    fecha_devolucion_dato_input.setText(str(result[3]))
    course_layout.addWidget(fecha_devolucion_dato_input, 1, 7)

    id = str(result[12])

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
    next_button.clicked.connect(lambda: insert_data(details_window, id, equipo_input, fecha_prestada_input, fecha_devolucion_input, donaciones))
    details_window.exec_()

def insert_data(details_window, id, equipo_input, fecha_prestada_input, fecha_devolucion_input, donaciones):
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

    
    # Encuentra el índice de la institución seleccionada.
    selected_equipo_index = equipo_input.currentIndex()

    # Si se selecciona una institución válida y obetiene su ID.
    if selected_equipo_index > 0:
        equipo = donaciones[selected_equipo_index - 1][0]


    #Guardar donaciones
    query = "INSERT INTO fundaprocura.historico_donaciones (fk_caso, fk_donacion, fecha_prestada, fecha_devolucion) VALUES (%s,%s,%s,%s)"
    cursor = cnx.cursor()
    cursor.execute(query, (caso,equipo,fecha_prestada,fecha_devolucion))
    cnx.commit()
    cursor.close()
    cnx.close()

    details_window.close()


# PyQt5 application
class historial_donaciones(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setWindowTitle("Historial de donaciones")
        self.resize(400, 400)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Buscar", self)
        self.list_widget = QListWidget(self)

        # Connect the button to the search function
        self.button.clicked.connect(lambda: search(self.line_edit.text(), self.connection, self.list_widget))

        self.list_widget.itemClicked.connect(display_details)

        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.list_widget)

        self.setLayout(self.layout)

        # Connect to the MySQL database
        self.connection = create_connection()

        self.show()