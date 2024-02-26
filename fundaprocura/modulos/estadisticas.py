import sys
import datetime
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidgetItem, QTableWidget

class Estadisticas(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create input fields and button
        layout = QVBoxLayout()
        self.setLayout(layout)

        hbox = QHBoxLayout()
        layout.addLayout(hbox)
        hbox.addWidget(QLabel("Edad mínima:"))
        self.min_age_input = QLineEdit()
        hbox.addWidget(self.min_age_input)

        hbox = QHBoxLayout()
        layout.addLayout(hbox)
        hbox.addWidget(QLabel("Edad máxima"))
        self.max_age_input = QLineEdit()
        hbox.addWidget(self.max_age_input)

        hbox = QHBoxLayout()
        layout.addLayout(hbox)
        self.search_button = QPushButton("Buscar")
        hbox.addWidget(self.search_button)
        self.search_button.clicked.connect(self.on_search_clicked)

        # Create a table to display the search results
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(4)
        self.results_table.setHorizontalHeaderLabels(["Nombre", "Apellido", "Cédula", "Edad"])
        layout.addWidget(self.results_table)

        # Create labels to display the number of cases and the percentage of cases
        self.num_cases_label = QLabel("Número de persoanas: ")
        layout.addWidget(self.num_cases_label)
        self.percentage_label = QLabel("Porcentaje de casos: ")
        layout.addWidget(self.percentage_label)

        # Set window title
        self.setWindowTitle("Filtrar por edades")

        self.resize(430, 400)


    def on_search_clicked(self):
    # Get input values
        min_age = int(self.min_age_input.text())
        max_age = int(self.max_age_input.text())

        # Call search function
        cases, total_cases = search_cases_by_age_range(min_age, max_age)

        # Display the results in the table
        self.results_table.setRowCount(len(cases))
        for i, case in enumerate(cases):
            fecha_nacimiento = case[16]
            edad = (datetime.date.today() - fecha_nacimiento).days // 365
            self.results_table.setItem(i, 0, QTableWidgetItem(case[7]))
            self.results_table.setItem(i, 1, QTableWidgetItem(case[6]))
            self.results_table.setItem(i, 2, QTableWidgetItem(str(case[5])))
            self.results_table.setItem(i, 3, QTableWidgetItem(str(edad)))

        # Display the number of cases found
        self.num_cases_label.setText(f"Número de personas: {len(cases)}")

        # Display the percentage of cases
        if total_cases > 0:
            percentage = (len(cases) / total_cases) * 100
            self.percentage_label.setText(f"Porcentaje de casos: {percentage}%")
        else:
            self.percentage_label.setText("")
    


def search_cases_by_age_range(min_age, max_age):
            # Connect to the database
            cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="fundaprocura"
            )
            cursor = cnx.cursor()

            # Query the database for the total number of cases
            query = "SELECT COUNT(*) FROM fundaprocura.casos"
            cursor.execute(query)
            total_cases = cursor.fetchone()[0]

            # Query the database for cases within the age range
            query = "SELECT * FROM fundaprocura.casos WHERE DATEDIFF(CURDATE(), fecha_nacimiento) / 365 BETWEEN %s AND %s"
            cursor.execute(query, (min_age, max_age))

            # Get the cases within the age range
            cases = []
            for row in cursor.fetchall():
                cases.append(row)

            # Close the database connection
            cursor.close()
            cnx.close()

            return cases, total_cases

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
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Estado", "Cantidad de casos", "Porcentaje"])

        self.layout.addWidget(self.table)
        self.window.setLayout(self.layout)

    def load_data(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="fundaprocura"
        )

        cursor = connection.cursor()
        query = "SELECT e.nombre, COUNT(c.id), (COUNT(c.id) / (SELECT COUNT(*) FROM fundaprocura.casos)) * 100 as porcentaje FROM fundaprocura.estado e LEFT JOIN fundaprocura.casos c ON e.id = c.fk_esado GROUP BY e.nombre"
        cursor.execute(query)

        for row in cursor.fetchall():
            row_number = self.table.rowCount()
            self.table.insertRow(row_number)
            self.table.setItem(row_number, 0, QTableWidgetItem(row[0]))
            self.table.setItem(row_number, 1, QTableWidgetItem(str(row[1])))
            self.table.setItem(row_number, 2, QTableWidgetItem(str(row[2]) + "%"))

        connection.close()

    def show(self):
        self.window.show()

    def set_window_properties(self):
        self.window.resize(600, 400)
        self.window.setWindowTitle("Cantidada de Casos por Estado")



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
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Clasificación", "Cantidad de casos","Porcentaje"])

        self.layout.addWidget(self.table)
        self.window.setLayout(self.layout)

    def load_data(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="fundaprocura"
        )

        cursor = connection.cursor()
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

        for row in cursor.fetchall():
            row_number = self.table.rowCount()
            self.table.insertRow(row_number)
            self.table.setItem(row_number, 0, QTableWidgetItem(row[0]))
            self.table.setItem(row_number, 1, QTableWidgetItem(str(row[1])))
            self.table.setItem(row_number, 2, QTableWidgetItem(str(row[2]) + "%"))

        connection.close()

    def show(self):
        self.window.show()

    def set_window_properties(self):
        self.window.resize(600, 400)
        self.window.setWindowTitle("Cantidada de Casos por Clasificación")

