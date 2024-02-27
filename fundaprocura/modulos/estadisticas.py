import sys
import datetime
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidgetItem, QTableWidget


# Función de filtro por rango de edad
class Estadisticas(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    #Función inicial
    def init_ui(self):
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        #Label e input edad mínima
        hbox = QHBoxLayout()
        layout.addLayout(hbox)
        hbox.addWidget(QLabel("Edad mínima:"))
        self.min_age_input = QLineEdit()
        hbox.addWidget(self.min_age_input)

        #Label e input edad máxima
        hbox = QHBoxLayout()
        layout.addLayout(hbox)
        hbox.addWidget(QLabel("Edad máxima"))
        self.max_age_input = QLineEdit()
        hbox.addWidget(self.max_age_input)

        #Botón de "Búscar"
        hbox = QHBoxLayout()
        layout.addLayout(hbox)
        self.search_button = QPushButton("Buscar")
        hbox.addWidget(self.search_button)

        #Botón de conecta con la función que muestra los resultados
        self.search_button.clicked.connect(self.on_search_clicked)

        # Crea la tabla con los resultados buscados
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(4)
        self.results_table.setHorizontalHeaderLabels(["Nombre", "Apellido", "Cédula", "Edad"])
        layout.addWidget(self.results_table)

        # labels con la información de contador y porcentaje
        self.num_cases_label = QLabel("Número de persoanas: ")
        layout.addWidget(self.num_cases_label)
        self.percentage_label = QLabel("Porcentaje de casos: ")
        layout.addWidget(self.percentage_label)

        # Titulo de la ventana
        self.setWindowTitle("Filtrar por edades")

        self.resize(430, 400)

    #Función 
    def on_search_clicked(self):
    # Valor de los inputs
        min_age = int(self.min_age_input.text())
        max_age = int(self.max_age_input.text())

        # Llamada a la función que busca los casos
        cases, total_cases = search_cases_by_age_range(min_age, max_age)

        # Resultados que son mostrados en la tabla
        self.results_table.setRowCount(len(cases))
        for i, case in enumerate(cases):
            fecha_nacimiento = case[16]
            edad = (datetime.date.today() - fecha_nacimiento).days // 365
            self.results_table.setItem(i, 0, QTableWidgetItem(case[7]))
            self.results_table.setItem(i, 1, QTableWidgetItem(case[6]))
            self.results_table.setItem(i, 2, QTableWidgetItem(str(case[5])))
            self.results_table.setItem(i, 3, QTableWidgetItem(str(edad)))

        # Muestra contador de casos
        self.num_cases_label.setText(f"Número de personas: {len(cases)}")

        # Muestra el porcentaje
        if total_cases > 0:
            #Calcula el porcentaje 
            percentage = (len(cases) / total_cases) * 100
            self.percentage_label.setText(f"Porcentaje de casos: {percentage}%")
        else:
            self.percentage_label.setText("")
    

#Función que busca los casos
def search_cases_by_age_range(min_age, max_age):
            # Conexión y cursor a la BD 
            cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="fundaprocura"
            )
            cursor = cnx.cursor()

            # Query para obetener el número de casos existentes
            query = "SELECT COUNT(*) FROM fundaprocura.casos"
            cursor.execute(query)
            total_cases = cursor.fetchone()[0]

            # Query que busca los casos que estan en el rango de edad
            query = "SELECT * FROM fundaprocura.casos WHERE DATEDIFF(CURDATE(), fecha_nacimiento) / 365 BETWEEN %s AND %s"
            cursor.execute(query, (min_age, max_age))

            # Guarda los casos en un array
            cases = []
            for row in cursor.fetchall():
                cases.append(row)

            # Cierra la conexión a la BD
            cursor.close()
            cnx.close()

            return cases, total_cases


# Función de filtro por Estados
class EstadoCasos:

    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.table = QTableWidget()

        self.init_ui()
        self.load_data()
        self.set_window_properties()

    def init_ui(self):
        #Inicia tabla con los títulos de las columnas
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Estado", "Cantidad de casos", "Porcentaje"])

        #Agrega la tabla al layout
        self.layout.addWidget(self.table)
        self.window.setLayout(self.layout)

    def load_data(self):
        # Conexión y cursor a la BD 
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="fundaprocura"
        )

        cursor = connection.cursor()
        #Query que cuenta la cantiodad de casos por Estado y calcula el porcentaje
        query = "SELECT e.nombre, COUNT(c.id), (COUNT(c.id) / (SELECT COUNT(*) FROM fundaprocura.casos)) * 100 as porcentaje FROM fundaprocura.estado e LEFT JOIN fundaprocura.casos c ON e.id = c.fk_esado GROUP BY e.nombre"
        cursor.execute(query)

        #Muestra en la tabla los resultados del query
        for row in cursor.fetchall():
            row_number = self.table.rowCount()
            self.table.insertRow(row_number)
            self.table.setItem(row_number, 0, QTableWidgetItem(row[0]))
            self.table.setItem(row_number, 1, QTableWidgetItem(str(row[1])))
            self.table.setItem(row_number, 2, QTableWidgetItem(str(row[2]) + "%"))

        connection.close()
        cursor.close()

    def show(self):
        self.window.show()
 
    #Tamaño de la ventana y título
    def set_window_properties(self):
        self.window.resize(600, 400)
        self.window.setWindowTitle("Cantidada de Casos por Estado")


# Función de filtro por clasificación 
class CasosClasificacion:
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.table = QTableWidget()

        self.init_ui()
        self.load_data()
        self.set_window_properties()

    def init_ui(self):
        #Inicia tabla con los títulos de las columnas
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Clasificación", "Cantidad de casos","Porcentaje"])

        #Agrega la tabla al layout
        self.layout.addWidget(self.table)
        self.window.setLayout(self.layout)

    def load_data(self):
        # Conexión y cursor a la BD 
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="fundaprocura"
        )

        cursor = connection.cursor()
        # Query que cuenta la cantidad de casos por cada clasificación de edad
        query = """
                SELECT 
                clasificacion_edad,
                COUNT(*) as total,
                (COUNT(*) / SUM(COUNT(*)) OVER () * 100) as porcentaje
            FROM (
                SELECT 
                    CASE 
                        WHEN TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) BETWEEN 0 AND 11 THEN 'Niño'
                        WHEN TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) BETWEEN 12 AND 17 THEN 'Adolescente'
                        WHEN TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) BETWEEN 18 AND 59 THEN 'Adulto'
                        WHEN TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) BETWEEN 60 AND 110 THEN 'Adulto mayor'
                        ELSE 'N/A'
                    END as clasificacion_edad
                FROM fundaprocura.casos
            ) as categorized_ages
            GROUP BY clasificacion_edad;
                """
        cursor.execute(query)

        #Muestra en la tabla los resultados del query
        for row in cursor.fetchall():
            row_number = self.table.rowCount()
            self.table.insertRow(row_number)
            self.table.setItem(row_number, 0, QTableWidgetItem(row[0]))
            self.table.setItem(row_number, 1, QTableWidgetItem(str(row[1])))
            self.table.setItem(row_number, 2, QTableWidgetItem(str(row[2]) + "%"))

        connection.close()
        cursor.close()

    def show(self):
        self.window.show()

    #Tamaño de la ventana y título
    def set_window_properties(self):
        self.window.resize(600, 400)
        self.window.setWindowTitle("Cantidada de Casos por Clasificación")

