import wave
from PyQt5.QtWidgets import QFileDialog, QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.uic import loadUi
from models import Song
from mutagen.mp3 import MP3


class MainView(QDialog):
    def __init__(self):
        super(MainView, self).__init__()
        loadUi('views/intefaz.ui', self)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.browse.clicked.connect(self.browsefiles)
        song = Song()
        song.datos()
        # self.loaddata()

    def browsefiles(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', '')
        self.flname.setText(self.filename[0])

        file = wave.open(self.filename[0], 'rb')
        frames = file.getnframes()
        rate = file.getframerate()
        duration = frames / float(rate)
        name = self.filename[0].split('/').pop()
        song = Song(name, int(duration), filename[0])










