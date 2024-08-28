
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QLineEdit, QTextEdit
from os import system
system("clear")

class TodoWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("ToDo")
        self.setFixedSize(500, 700)
        
        self.label = QLineEdit(self)
        self.label.setPlaceholderText("New  task...")
        self.label.setGeometry(50, 50, 400, 50)        
        
        self.btn = QPushButton("➕", self)
        self.btn.setStyleSheet("""
            QPushButton {
                font-size: 22px;
                background-color: black;
                color: white;
                border-radius: 10px;
            }

            QPushButton::hover {
                background-color: #404040;
            }

            QPushButton::pressed {
                color: #212121;
                background-color: white;
                border: 1px solid black;
            }
        """)
        self.btn.setGeometry((self.width() - self.btn.width()) // 2,600 ,80, 40)
        
        
        
       
        self.show()
        
        
        
        
class  TodoWindow2(QWidget):
    pass        




    
app = QApplication([])
oyna = TodoWindow()

app.exec_()