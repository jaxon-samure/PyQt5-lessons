from PyQt5.QtWidgets import QApplication, QWidget
from components import Label, Input, ComboBox, SeatButton, Button, getLastSelectedSeat
from database import database
from os import system

system("clear")


class Window(QWidget):
    PLACES = list(map(str, list(range(1, 17))))
    users = database.select()

    def __init__(self):
        super().__init__()

        self.resize(1200, 700)
        self.move(400, 200)

        self.fioLabel = Label("F.I.SH", self)
        self.fioLabel.move(70, 100)

        self.fioInput = Input(self)
        self.fioInput.move(50, 160)

        self.placesLabel = Label("Joylar", self)
        self.placesLabel.move(70, 260)

        self.placesComboBox = ComboBox(self)
        self.placesComboBox.move(50, 320)

        self.placesComboBox.addItem("Tanlang...")
        self.placesComboBox.addItems(self.PLACES)
        
        self.priceLabel = Label("Narxi: 0 uzs", self)
        self.priceLabel.move(70, 460)

        
        self.SEAT_BUTTONS = [
            SeatButton(1, self, 600, 100),
            SeatButton(2, self, 680, 100),
            SeatButton(3, self, 900, 100),
            SeatButton(4, self, 980, 100),

            SeatButton(5, self, 620, 200),
            SeatButton(6, self, 700, 200),
            SeatButton(7, self, 880, 200),
            SeatButton(8, self, 960, 200),
            
            SeatButton(9, self, 640, 300),
            SeatButton(10, self, 720, 300),
            SeatButton(11, self, 860, 300),
            SeatButton(12, self, 940, 300),

            SeatButton(13, self, 660, 400),
            SeatButton(14, self, 740, 400),
            SeatButton(15, self, 840, 400),
            SeatButton(16, self, 920, 400),
        ]

        self.buyBtn = Button("Sotib olish", self)
        self.buyBtn.move(1000, 600)

        for odam in self.users:
            FIO = odam[1]
            ticket_no = odam[-1]
            self.SEAT_BUTTONS[ticket_no - 1].band_qilingan(FIO)

        self.buyBtn.clicked.connect(self.buyFunction)


    def buyFunction(self):
        no = getLastSelectedSeat()
        FIO = self.fioInput.text()

        database.insert(FIO, 100_000, True, no)
        self.SEAT_BUTTONS[no - 1].band_qilingan(FIO)


app = QApplication([])
oyna = Window()
oyna.show()
app.exec()