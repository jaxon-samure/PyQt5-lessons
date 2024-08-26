from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import os
os.system("clear")

class Oyna(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Nimadir")
        self.resize(400, 600)

        self.btn = QPushButton("Button", self)
        self.btn.clicked.connect(self.bos)
        
        self.oyna2 = Oyna2()
        
        self.show()

    def bos(self):
        self.oyna2.show()
        self.close()

class Oyna2(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("nima")
        self.resize(500, 700)

app = QApplication([])
e = Oyna()
e.show()
app.exec_()
