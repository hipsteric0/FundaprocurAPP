import sys
import datetime
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidgetItem, QTableWidget
from PyQt5.QtCore import QTimer, QObject, pyqtSignal

import threading

class MyTimer(QObject):
    stopped = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.thread_id = threading.get_ident()
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)

    def start(self, interval):
        self.timer.start(interval)

    def stop(self):
        self.timer.stop()
        self.stopped.emit()

    def on_timeout(self):
        print(f"MyTimer ticked in thread {threading.get_ident()}, which is different from the thread it was created in ({self.thread_id})")


class EstadoCasos:
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.table = QTableWidget()

        self.init_ui()
        self.load_data()
        self.set_window_properties()

        # Create a new MyTimer object and start it
        self.timer = MyTimer()
        self.timer.stopped.connect(self.on_timer_stopped)
        self.timer.start(1000)  # every second

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

        # Stop the timer when the window is closed
        self.window.closeEvent = self.on_window_closed

    def on_window_closed(self, event):
        self.timer.stop()
        event.accept()

    def on_timer_stopped(self):
        print("MyTimer stopped")

if __name__ == "__main__":
    estado_casos = EstadoCasos()
    sys.exit(estado_casos.app.exec_())