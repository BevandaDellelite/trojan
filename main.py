from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.function)
    def function(self):
        if self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() != "" and self.ui.lineEdit_3.text() != "":
            self.ui.pushButton.setText('правильно')
        else:
            self.ui.pushButton.setText('не правильно')
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()