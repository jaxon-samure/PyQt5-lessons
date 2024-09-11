from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel

app = QApplication([])

window = QWidget()
window.resize(300, 400)
layout = QGridLayout()

# Gorizontal va vertikal bo'sh joylarni qo'lda sozlash
layout.setHorizontalSpacing(10)  # Gorizontal bo'sh joy
layout.setVerticalSpacing(10) 
# Vertikal bo'sh joy
layout.setRowStretch(0, 1)
layout.setRowStretch(1, 1)

label = QLabel("salom", window)
# Tugmalarni grid joylashuviga qo'yamiz
layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)

window.setLayout(layout)
window.show()

app.exec_()
