import os 
os.system("clear")

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout,QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


app = QApplication([])

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("15")
        self.setStyleSheet("background-color: #F0DBDB;")
        self.resize(500, 330)
        
       
        self.btn_coordinates = [[10, 10, 120, 80, "1"], 
                               [130, 10, 120, 80, "2"], 
                               [250, 10, 120, 80, "3"], 
                               [370, 10, 120, 80, "4"], 
                               [10, 90, 120, 80, "5"],
                               [130, 90, 120, 80, "6"],
                               [250, 90, 120, 80, "7"],
                               [370, 90, 120, 80, "8"],
                               [10, 170, 120, 80, "9"], 
                               [130, 170, 120, 80, "10"], 
                               [250, 170, 120, 80, "11"], 
                               [370, 170, 120, 80, "12"],
                               [10, 250, 120, 80, "13"], 
                               [130, 250, 120, 80, "14"], 
                               [250, 250, 120, 80, "15"],
                               ]
                                
                            
                               
                               
        
        self.btn_dict = {}
        for bt in self.btn_coordinates:
            name = "btn" + bt[4]  
            self.btn_dict[name] = QPushButton(bt[4], self)
            self.btn_dict[name].setGeometry(bt[0], bt[1], bt[2], bt[3])
            self.btn_dict[name].setStyleSheet("""
                            background-color:#222037;
                            color: white;                  
                            """)
            
            
        def find_keys_by_value(d, target_value):
            return [key for key, value in d.items() if value == target_value]
        def rm_key(key):
            for i in self.btn_coordinates:
                if i[4] == key[4]:
                    self.btn_coordinates.remove(i)
                    
        def bosdi(self):
            self.btn_coordinates.remove(0)
            
            
            print(self.btn_coordinates)
        
            
            
            
        self.btn_dict['btn1'].clicked.connect(bosdi)

            
        
            
        
        self.show()



oyna = Window()  
app.exec_()  