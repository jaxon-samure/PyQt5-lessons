from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QComboBox, QButtonGroup
from os import system

system("clear")

TESTS = [
    {
        'id': 1,
        'question': "Tuxum birinchi paydo bo'lganmi tovuqmi?",
        'answers': {
            'A': "Tuxum",
            'B': "Tovuq",
            'C': "Aziz",
            'D': "Mo'rs"
        },
        'right_answer': 'C'
    },
    {
        'id': 2,
        'question': "O'zbekiston oldin nima deb nomlangan?",
        'answers': {
            'A': "O'zbekiston",
            'B': "Qozog'iston",
            'C': "Qirg'iziston",
            'D': "Aziziston"
        },
        'right_answer': 'A'
    },
    {
        'id': 3,
        'question':"Men kecha nima ovqat yedim?",
        'answers':{
            'A': "Osh",
            'B': "Somsa",
            'C': "Hech nima",
            'D': "Qayerdan bilaman"
        },
        'right_answer': 'C'
    },
    {
        'id': 4,
        'question':"Jaxonni tug'ilgan kuni qachon?",
        'answers':{
            'A': "Mill avv",
            'B': "Miloddan keyin",
            'C': "Milodda",
            'D': "1 - dekabr"
        },
        'right_answer': 'D'
    }
        ]

class Window(QWidget):
    q_index = 0
    count_right = 0

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Savol-Javob")
        self.setStyleSheet("background-color : white" )
        self.setFixedSize(600, 500)

        self.questionLabel = QLabel("Savol", self)
        self.questionLabel.setStyleSheet("font-size: 22px; font-weight: bold; color: black;")
        self.questionLabel.move(20, 70)
        

        self.A_variant = QRadioButton("A", self)
        self.A_variant.setStyleSheet("font-size: 16px; color: black;")
        self.A_variant.move(50, 100)

        self.B_variant = QRadioButton("B", self)
        self.B_variant.setStyleSheet("font-size: 16px; color: black;")
        self.B_variant.move(50, 140)
        
        self.C_variant = QRadioButton("C", self)
        self.C_variant.setStyleSheet("font-size: 16px; color: black;")
        self.C_variant.move(50, 180)
        
        self.D_variant = QRadioButton("D", self)
        self.D_variant.setStyleSheet("font-size: 16px; color: black;")
        self.D_variant.move(50, 220)
        
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.A_variant)
        self.button_group.addButton(self.B_variant)
        self.button_group.addButton(self.C_variant)
        self.button_group.addButton(self.D_variant)

        self.nextBtn = QPushButton("Next", self)
        self.nextBtn.setStyleSheet("font-size: 20px; background-color: #1E1D1D; color: white")
        self.nextBtn.move(400, 450)

        self.fillWindowWithQuestion()

        self.nextBtn.clicked.connect(self.nextFunction)

        self.show()
        

    def clearRadioButtons(self):
        self.button_group.setExclusive(False)  
        self.B_variant.setChecked(False)
        self.C_variant.setChecked(False)
        self.D_variant.setChecked(False)
        self.button_group.setExclusive(True)
    
    


    def fillWindowWithQuestion(self):
        question = TESTS[self.q_index]

        self.questionLabel.setText(str(self.q_index+1) + " . " + question['question'])
        self.A_variant.setText(question['answers']['A'])
        self.B_variant.setText(question['answers']['B'])
        self.C_variant.setText(question['answers']['C'])
        self.D_variant.setText(question['answers']['D'])

        self.A_variant.adjustSize()
        self.B_variant.adjustSize()
        self.C_variant.adjustSize()
        self.D_variant.adjustSize()
        
        


    def nextFunction(self):
        self.selected_opion = self.button_group.checkedButton()
        a = self.selected_opion.text()
        right_answer = TESTS[self.q_index]['right_answer']
        if a == TESTS[self.q_index]['answers'][right_answer]:
            self.count_right+=1
        
        self.q_index += 1
        if self.q_index >= len(TESTS):
            self.questionLabel.setText(f"""Savollar tugadi ! \nTo'g'ri javoblar soni : {self.count_right}""")
            self.questionLabel.adjustSize()
            self.questionLabel.move(200, 200)
            self.A_variant.close()
            self.B_variant.close()
            self.C_variant.close()
            self.D_variant.close()
            
            
        else:
            self.clearRadioButtons()
            self.fillWindowWithQuestion()


app = QApplication([])
oyna = Window()

app.exec()