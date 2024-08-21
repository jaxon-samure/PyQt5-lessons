import os 
os.system("clear")

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

FIO = [" ", "Jaxon", "Xudoyberdiyev", "Ramazonovich"]
FIO_index = 0
count = 0


app = QApplication([])
window = QWidget()

window.setWindowTitle("Info")
window.setGeometry(400, 300, 400, 600)
window.setStyleSheet("""
        background-color: white;
                     """)

FIO_label = QLabel(FIO[FIO_index], window)
FIO_label.setStyleSheet("""
        font-size: 25px;
        color: black;
        fon-weight: 700;
                        """)

FIO_label.adjustSize()
FIO_label.move((window.width() - FIO_label.width()) // 50, 180)

butt = QPushButton("Ism")
butt2 = QPushButton("Familiya")
butt3 = QPushButton("Sharifi")

layout = QHBoxLayout()
layout.addWidget(butt)
layout.addWidget(butt2)
layout.addWidget(butt3)

window.setLayout(layout)

butt.setStyleSheet("""
        font-size: 25px;
        color: black;
        background-color: white;
                   """)
butt2.setStyleSheet("""
        font-size: 25px;
        color: black;
        background-color: white;
                   """)
butt3.setStyleSheet("""
        font-size: 25px;
        color: black;
        background-color: white;
                   """)


def urdimi():
    global FIO_index, FIO,count
    count+=1
    
    sender = window.sender()
    
    if sender == butt:
        FIO_label.setText(FIO[1])
        FIO_label.setAlignment(Qt.AlignCenter)
        FIO_label.adjustSize()
    
    elif sender == butt2:
        FIO_label.setText(FIO[1]+" "+FIO[2])
        FIO_label.setAlignment(Qt.AlignCenter)
        FIO_label.adjustSize()
    
    elif sender == butt3:
        FIO_label.setText(FIO[1] +" "+FIO[2]+" "+FIO[3])
        FIO_label.setAlignment(Qt.AlignCenter)
        FIO_label.adjustSize()
        
        
        
butt.clicked.connect(urdimi)
butt2.clicked.connect(urdimi)
butt3.clicked.connect(urdimi)
    
    
window.show()
app.exec()
    
    



 
 
 
 
 
 
 
 