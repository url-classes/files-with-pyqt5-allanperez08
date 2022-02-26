from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout
from views import main_view


class Song:
    def __init__(self, name='', duration=0, filename=''):
        self.tableWidget = None
        self.name = name
        self.duration = duration
        self.filename = filename

    def datos(self):
        canciones = [{}]
        row = 0
        self.tableWidget.setRowCount(len(canciones))
        for cancion in canciones:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(cancion[self.name]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(cancion[self.duration])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(cancion[self.filename]))






