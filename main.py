from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from views import MainView

import sys

app = QApplication(sys.argv)
main_view = MainView()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_view)
widget.setFixedWidth(541)
widget.setFixedHeight(572)
widget.show()
sys.exit(app.exec_())
