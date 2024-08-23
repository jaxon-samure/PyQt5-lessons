import os 
os.system("clear")

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout,QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


app = QApplication([])

class deraza(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Oyna")
        self.resize(500, 600)
        self.labelS = QLabel("Qaysi Davlatga borasan , Tanla!", self)
        
        self.labelS.setStyleSheet("""
                font-size: 22px;
                color: #040404;    
                """)
        self.labelS.adjustSize()
        self.labelS.move((self.width() - self.labelS.width()) // 2, 120)
        
        self.sora = QCheckBox("BAA", self)
        self.sora.move(150, 150)
        
        self.sora.setStyleSheet("""
            font-size: 20px;
            color: #FF0000;
            """)
        self.sora2 = QCheckBox("Russia", self)
        self.sora2.move(150, 250)
        
        self.sora2.setStyleSheet("""
            font-size: 20px;
            color: #FF0000;
            """)
        
        self.soraBaa1 = QCheckBox("Dubai", self)
        self.soraBaa1.setStyleSheet("""
            font-size: 16px;
            color: #641010;
            """)
        self.soraBaa1.move(170, 180)
        self.soraBaa2 = QCheckBox("Al Jaxon", self)
        self.soraBaa2.setStyleSheet("""
            font-size: 16px;
            color: #641010;
            """)
        self.soraBaa2.move(170, 200)
        self.soraBaa3 = QCheckBox("Al Axror", self)
        self.soraBaa3.setStyleSheet("""
            font-size: 16px;
            color: #641010;
            """)
        self.soraBaa3.move(170, 220)
        
        self.soraRus1 =  QCheckBox("Moskva", self)
        self.soraRus1.setStyleSheet("""
            font-size: 16px;
            color: #641010;
            """)
        self.soraRus1.move(170, 280)
        self.soraRus2 =  QCheckBox("Natasha", self)
        self.soraRus2.setStyleSheet("""
            font-size: 16px;
            color: #641010;
            """)
        self.soraRus2.move(170, 300)
        self.soraRus3 =  QCheckBox("Ozon", self)
        self.soraRus3.setStyleSheet("""
            font-size: 16px;
            color: #641010;
            """)
        self.soraRus3.move(170, 320)
        
        
        self.soraBaa1.setEnabled(False)
        self.soraBaa2.setEnabled(False)
        self.soraBaa3.setEnabled(False)
        self.soraRus1.setEnabled(False)
        self.soraRus2.setEnabled(False)
        self.soraRus3.setEnabled(False)
       
       
        def bosdi(self,a):
            if a:
                self.soraBaa1.setEnabled(True)
                self.soraBaa2.setEnabled(True)
                self.soraBaa3.setEnabled(True)
            else:
                self.soraBaa1.setEnabled(False)
                self.soraBaa2.setEnabled(False)
                self.soraBaa3.setEnabled(False)
        def bosdi2(self, b):
            if b:
                self.soraRus1.setEnabled(True)
                self.soraRus2.setEnabled(True)
                self.soraRus3.setEnabled(True)
            else:
                self.soraRus1.setEnabled(False)
                self.soraRus2.setEnabled(False)
                self.soraRus3.setEnabled(False)
                
                
        self.sora.toggled.connect(lambda checked: bosdi(self, checked))
        self.sora2.toggled.connect(lambda checked: bosdi2(self, checked))
        
            
        

        
        self.show()
        
        
        
window = deraza()      
app.exec_()
        
        
        
        
        
        