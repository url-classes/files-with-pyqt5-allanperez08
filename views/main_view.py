from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PyBeats - Reproductor de canciones')
        self.setFixedWidth(640)
        self.setFixedHeight(760)

        layout = QVBoxLayout(self)

        label = QLabel(self)
        label.setText('Pantalla principal')
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.show()
