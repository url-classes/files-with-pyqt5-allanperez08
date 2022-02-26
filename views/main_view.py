import wave
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5.uic import loadUi
from models import Song
from structures import CircularList


class MainView(QDialog):
    def __init__(self):
        super(MainView, self).__init__()
        loadUi('views/intefaz.ui', self)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.browse.clicked.connect(self.browsefiles)
        self.songs = []
        self.list_songs = CircularList()
        self.show_anterior()

    def browsefiles(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open file', '')
        self.flname.setText(self.filename[0])

        file = wave.open(self.filename[0], 'rb')
        frames = file.getnframes()
        rate = file.getframerate()
        duration = frames / float(rate)
        name = self.filename[0].split('/').pop()
        self.songs.append(Song(name, int(duration), self.filename[0]))
        self.list_songs.append(self.songs)
        self.show_songs()

    def show_songs(self):
        row = 0
        self.tableWidget.setRowCount(len(self.songs))
        for song in self.songs:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(song.get_name()))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(song.get_duration())))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(song.get_filename()))
            row += 1

    def show_anterior(self):
        self.anterior_label.setText(self.list_songs.tail)










