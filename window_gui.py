from PyQt6 import uic, QtWidgets

Form, Window = uic.loadUiType("untitled1.ui")

class Ui (QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.printButtonPressed)

    def printButtonPressed(self):
        print('pressed')

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec())
