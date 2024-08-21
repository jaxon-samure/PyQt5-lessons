import os 
os.system("clear")
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QVBoxLayout,QGridLayout, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


calc = QApplication([])
window = QWidget()

window.setWindowTitle("Calculator")
window.setGeometry(100, 100, 400, 700)
window.setStyleSheet("""
        background-color: #2E2E2E;   
        """)




one = QPushButton("1")
one.setStyleSheet("""
        color: white;      
        """)
two = QPushButton("2")
two.setStyleSheet("""
        color: white;      
        """)
three = QPushButton("3")
three.setStyleSheet("""
        color: white;      
        """)
x = QPushButton("X")
x.setStyleSheet("""
    color: red;
                
    """)

four = QPushButton("4")
four.setStyleSheet("""
        color: white;      
        """)
five = QPushButton("5")
five.setStyleSheet("""
        color: white;      
        """)
six = QPushButton("6")
six.setStyleSheet("""
        color: white;      
        """)
plus = QPushButton("+")
plus.setStyleSheet("""
        color: white;
        background-color: red;      
        """)
seven = QPushButton("7")
seven.setStyleSheet("""
        color: white;      
        """)

eight = QPushButton("8")
eight.setStyleSheet("""
        color: white;      
        """)

nine = QPushButton("9")
nine.setStyleSheet("""
        color: white;      
        """)
minus = QPushButton("-")
minus.setStyleSheet("""
        color: white;
        background-color: red;      
        """)
nol = QPushButton("0")
nol.setStyleSheet("""
        color: white;
        """)

kopaytma = QPushButton("*")
kopaytma.setStyleSheet("""
        color: white;
        background-color: red;      
        """)

bolinma = QPushButton("/")
bolinma.setStyleSheet("""
        color: white;
        background-color: red;      
        """)

teng = QPushButton("=")
teng.setStyleSheet("""
        color: white;
        background-color: green;           
        """)

nuqta = QPushButton(".")
nuqta.setStyleSheet("""
        color: white;
        """)
c = QPushButton("C")
c.setStyleSheet("""
    color: red;
                
    """)
noll = QPushButton("00")
noll.setStyleSheet("""
    color: white;               
    """)
kvadrat = QPushButton("x^2")
kvadrat.setStyleSheet("""
    color: white;            
    """)

buttons = [one, two, three, x, four, five, six, plus, seven, eight, nine, minus, nol, kopaytma, bolinma, teng, nuqta,c,noll, kvadrat]
for button in buttons:
    
    button.setFixedSize(80, 50)
        

gridLayout = QGridLayout()
gridLayout.setHorizontalSpacing(0)
gridLayout.setVerticalSpacing(0)
gridLayout.setContentsMargins(0, 0, 0, 10)

gridLayout.addWidget(one, 0, 0)
gridLayout.addWidget(two, 0, 1)
gridLayout.addWidget(three, 0, 2)
gridLayout.addWidget(x, 0,3)
gridLayout.addWidget(four, 1, 0)
gridLayout.addWidget(five, 1, 1)
gridLayout.addWidget(six, 1, 2)
gridLayout.addWidget(plus, 1, 3)
gridLayout.addWidget(seven, 2, 0)
gridLayout.addWidget(eight, 2, 1)
gridLayout.addWidget(nine, 2, 2)
gridLayout.addWidget(minus, 2, 3)
gridLayout.addWidget(nol,3, 0)
gridLayout.addWidget(kopaytma,3, 1)
gridLayout.addWidget(bolinma, 3, 2)
gridLayout.addWidget(c, 3, 3)
gridLayout.addWidget(nuqta, 4, 0)
gridLayout.addWidget(teng, 4, 3)
gridLayout.addWidget(noll, 4, 2)
gridLayout.addWidget(kvadrat, 4, 1)

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
operaters = ["+", "-", "/", "*"]


def urdi():
    sender = window.sender()
    
    if sender == one:
        tex = linedit.text() + "1"
        linedit.setText(tex)
    elif sender == two:
        tex = linedit.text() + "2"
        linedit.setText(tex)
    elif sender == three:
        tex = linedit.text() + "3"
        linedit.setText(tex)
    elif sender == four:
        tex = linedit.text() + "4"
        linedit.setText(tex)
    elif sender == five:
        tex = linedit.text() + "5"
        linedit.setText(tex)
    elif sender == six:
        tex = linedit.text() + "6"
        linedit.setText(tex)
    elif sender == seven:
        tex = linedit.text() + "7"
        linedit.setText(tex)  
    elif sender == eight:
        tex = linedit.text() + "8"
        linedit.setText(tex)
    elif sender == nine:
        tex = linedit.text() + "9"
        linedit.setText(tex)
    elif sender == nol:
        if linedit.text()[-1] == "/":
            return
        tex = linedit.text() + "0"
        linedit.setText(tex)
    elif sender == noll:
        tex = linedit.text() + "00"
        linedit.setText(tex)
    elif sender == kvadrat:
        result = linedit.text() + "*" + linedit.text() 
        linedit.setText(str(eval(result)))
        
            
            
            
    elif sender == plus:
        if linedit.text()[-1] not in operaters:
            tex = linedit.text() + "+"
            linedit.setText(tex)
    elif sender == kopaytma:
        if linedit.text()[-1] not in operaters:
            tex = linedit.text() + "*"
            linedit.setText(tex)
    elif sender == bolinma:
        if linedit.text()[-1] not in operaters:
            tex = linedit.text() + "/"
            linedit.setText(tex)
    elif sender == minus:
        if linedit.text()[-1] not in operaters:
            tex = linedit.text() + "-"
            linedit.setText(tex)
        
        
        
    elif sender == x:
        tex = linedit.text()
        t_tex = tex[:-1]
        linedit.setText(t_tex)
    elif sender == teng:
        tex = linedit.text()
        linedit.setText(str(eval(tex)))
    elif sender == c:
        linedit.setText(" ")
    elif sender == nuqta:
        if len(linedit.text()) > 0:
            tex = linedit.text()+"."
            linedit.setText(tex)



linedit = QLineEdit(window)
linedit.setGeometry(16, 10, 300, 55)
linedit.setStyleSheet("""
        border: 1px solid black;
        font-size: 30px;
        color:white;              
        """)

one.clicked.connect(urdi)
two.clicked.connect(urdi)
three.clicked.connect(urdi)
four.clicked.connect(urdi)
five.clicked.connect(urdi)
six.clicked.connect(urdi)
seven.clicked.connect(urdi)
eight.clicked.connect(urdi)
nine.clicked.connect(urdi)
nol.clicked.connect(urdi)
plus.clicked.connect(urdi)
minus.clicked.connect(urdi)
kopaytma.clicked.connect(urdi)
bolinma.clicked.connect(urdi)
teng.clicked.connect(urdi)
c.clicked.connect(urdi)
noll.clicked.connect(urdi)
kvadrat.clicked.connect(urdi)
nuqta.clicked.connect(urdi)


x.clicked.connect(urdi)







window.setLayout(gridLayout)





window.show()
calc.exec_()
