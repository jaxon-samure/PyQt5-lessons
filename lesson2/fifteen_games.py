import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt
import os 

os.system("clear")

app = QApplication([])

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("15")
        self.setStyleSheet("background-color: #F0DBDB;")
        self.resize(500, 330)
        
        self.btn_coordinates = [[10, 10, 120, 80], 
                                [130, 10, 120, 80], 
                                [250, 10, 120, 80], 
                                [370, 10, 120, 80], 
                                [10, 90, 120, 80],
                                [130, 90, 120, 80],
                                [250, 90, 120, 80],
                                [370, 90, 120, 80],
                                [10, 170, 120, 80], 
                                [130, 170, 120, 80], 
                                [250, 170, 120, 80], 
                                [370, 170, 120, 80],
                                [10, 250, 120, 80], 
                                [130, 250, 120, 80], 
                                [250, 250, 120, 80 ]]
        
        self.btn_dict = {}
        self.a = list(random.sample(range(1, 16), k=15))
        
        self.move_lst = []
        x = 0
        for bt in self.btn_coordinates:
            name = "btn" + str(self.a[x])
            self.move_lst.append(self.a[x])  
            self.btn_dict[name] = QPushButton(str(self.a[x]), self)
            self.btn_dict[name].setGeometry(bt[0], bt[1], bt[2], bt[3])
            self.btn_dict[name].setStyleSheet("""
                            background-color:#222037;
                            color: white;                  
                            """)
            self.btn_dict[name].clicked.connect(self.move_tile)
            x += 1
        self.move_lst.append('16')
        
        self.bosh_btn = [370, 250, 120, 80]
    def find_key(self, btn):
        for key, value in self.btn_dict.items():
            if value == self.clicked_button:
                return key
    
    #win_lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
    def move_tile(self):
        clicked_button = self.sender()
        clicked_but_geo = clicked_button.geometry()
        
        if (abs(clicked_but_geo.x() - self.bosh_btn[0]) == 120 and clicked_but_geo.y() == self.bosh_btn[1]):
            clicked_button.setGeometry(self.bosh_btn[0], self.bosh_btn[1], 120, 80)
            self.bosh_btn = [clicked_but_geo.x(), clicked_but_geo.y(), 120, 80]
        if (abs(clicked_but_geo.y() - self.bosh_btn[1]) == 80 and clicked_but_geo.x() == self.bosh_btn[0]):
            clicked_button.setGeometry(self.bosh_btn[0], self.bosh_btn[1], 120, 80)
            self.bosh_btn = [clicked_but_geo.x(), clicked_but_geo.y(), 120, 80]
            
            
           
    
    
    


window = Window()
window.show()
app.exec_()
