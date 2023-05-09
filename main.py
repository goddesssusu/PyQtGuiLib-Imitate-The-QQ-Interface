import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from mainWindow import Ui_MainWindow


class QQInterface(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QQInterface()
    w.show()
    sys.exit(app.exec())