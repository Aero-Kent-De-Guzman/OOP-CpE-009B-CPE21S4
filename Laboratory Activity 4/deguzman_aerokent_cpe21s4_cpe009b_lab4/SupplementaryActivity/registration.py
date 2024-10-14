import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Account Registration System"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()
        self.programTitle()
        self.firstName()
        self.lastName()
        self.userName()
        self.password()
        self.email()
        self.contactNo()
        self.submit()
        self.clear()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(200,200,300,300)
        self.setWindowIcon(QIcon('Snakes.ico'))

    def programTitle(self):
        self.pTitle = QLabel("CPE21S4 CPE009B ", self)
        self.pTitle.move(90, 0)

    def firstName(self):
        self.fName = QLabel("First Name : ", self)
        self.fName.move(35,30)
        self.textbox = QLineEdit(self)
        self.textbox.move(135, 35)
        self.textbox.resize(100, 20)
        self.textbox.setText("Lorem")

    def lastName(self):
        self.lName = QLabel("Last Name : ", self)
        self.lName.move(35, 60)
        self.textbox = QLineEdit(self)
        self.textbox.move(135, 65)
        self.textbox.resize(100, 20)
        self.textbox.setText("Ipsun")

    def userName(self):
        self.uName = QLabel("User Name : ", self)
        self.uName.move(35, 90)
        self.textbox = QLineEdit(self)
        self.textbox.move(135, 95)
        self.textbox.resize(100, 20)
        self.textbox.setText("loremIpsun")

    def password(self):
        self.password = QLabel("Password : ", self)
        self.password.move(35, 120)
        self.textbox = QLineEdit(self)
        self.textbox.move(135, 125)
        self.textbox.resize(100, 20)
        self.textbox.setText("ABC123")

    def email(self):
        self.email = QLabel("Email Address : ", self)
        self.email.move(35,150)
        self.textbox = QLineEdit(self)
        self.textbox.move(135, 155)
        self.textbox.resize(100, 20)
        self.textbox.setText("loren.Ipsum@example.com")

    def contactNo(self):
        self.coNum = QLabel("Contact Number : ", self)
        self.coNum.move(35,180)
        self.textbox = QLineEdit(self)
        self.textbox.move(135, 185)
        self.textbox.resize(100, 20)
        self.textbox.setText("0912 345 6789")

    def submit(self):
        self.sButton = QPushButton('SUBMIT', self)
        self.sButton.setToolTip("Please input all the details, currently no functions...")
        self.sButton.resize(100, 20)
        self.sButton.move(30, 220)  # button.move(x,y)

    def clear(self):
        self.cButton = QPushButton('CLEAR', self)
        self.cButton.setToolTip("Will clear all the details, currently no functions...")
        self.cButton.resize(100, 20)
        self.cButton.move(130, 220)  # button.move(x,y)

        self.show()