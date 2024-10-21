import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QMessageBox, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import pandas as pd
import csv

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Account Registration System"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(200,200,300,300)
        self.setWindowIcon(QIcon('Snakes.ico'))

        self.pTitle = QLabel("CPE21S4 CPE009B ", self)
        self.pTitle.move(90, 0)

        self.fName = QLabel("First Name : ", self)
        self.fName.move(35,30)
        self.fName.textbox = QLineEdit(self)
        self.fName.textbox.move(135, 35)
        self.fName.textbox.resize(100, 20)
        self.fName.textbox.setText('')

        self.lName = QLabel("Last Name : ", self)
        self.lName.move(35, 60)
        self.lName.textbox = QLineEdit(self)
        self.lName.textbox.move(135, 65)
        self.lName.textbox.resize(100, 20)
        self.lName.textbox.setText('')

        self.uName = QLabel("User Name : ", self)
        self.uName.move(35, 90)
        self.uName.textbox = QLineEdit(self)
        self.uName.textbox.move(135, 95)
        self.uName.textbox.resize(100, 20)
        self.uName.textbox.setText('')

        self.password = QLabel("Password : ", self)
        self.password.move(35, 120)
        self.password.textbox = QLineEdit(self)
        self.password.textbox.move(135, 125)
        self.password.textbox.resize(100, 20)
        self.password.textbox.setText('')

        self.email = QLabel("Email Address : ", self)
        self.email.move(35,150)
        self.email.textbox = QLineEdit(self)
        self.email.textbox.move(135, 155)
        self.email.textbox.resize(100, 20)
        self.email.textbox.setText('')

        self.coNum = QLabel("Contact Number : ", self)
        self.coNum.move(35,180)
        self.coNum.textbox = QLineEdit(self)
        self.coNum.textbox.move(135, 185)
        self.coNum.textbox.resize(100, 20)
        self.coNum.textbox.setText('')

        self.sButton = QPushButton('SUBMIT', self)
        self.sButton.setToolTip("Please input all the details...")
        self.sButton.resize(100, 20)
        self.sButton.move(30, 220)  # button.move(x,y)
        self.sButton.clicked.connect(self.submit)

        self.cButton = QPushButton('CLEAR', self)
        self.cButton.setToolTip("This will clear all the fields...")
        self.cButton.resize(100, 20)
        self.cButton.move(130, 220)  # button.move(x,y)
        self.cButton.clicked.connect(self.clear)

        self.show()

    @pyqtSlot()
    def submit(self):
        data = []
        firstname = self.fName.textbox.text()
        lastname = self.lName.textbox.text()
        username = self.uName.textbox.text()
        password = self.password.textbox.text()
        email = self.email.textbox.text()
        contactnum = self.coNum.textbox.text()
        if (
            firstname   == '' or
            lastname    == '' or
            username    == '' or
            password    == '' or
            email       == '' or
            contactnum  == ''
            ):
            QMessageBox.information(self, "Registration Failed!", "Please fill out all of the necessary fields...", QMessageBox.Ok,QMessageBox.Ok)
            return
        else:
            QMessageBox.question(self, 'Registration Complete!', "Firstname: " + firstname + "\n"
                                                                + "Lastname: " + lastname + "\n"
                                                                + "Username: " + username + "\n"
                                                                + "Password: " + password + "\n"
                                                                + "Email: " + email + "\n"
                                                                + "Contact number: " + contactnum
                                 , QMessageBox.Ok, QMessageBox.Ok)
            data.append(firstname)
            data.append(lastname)
            data.append(username)
            data.append(password)
            data.append(email)
            data.append(contactnum)
            write(self, 'registration_database.csv', data)

    def clear(self):
        self.fName.textbox.setText('')
        self.lName.textbox.setText('')
        self.uName.textbox.setText('')
        self.password.textbox.setText('')
        self.email.textbox.setText('')
        self.coNum.textbox.setText('')
    
def write(self, filepath, data):
    with open(filepath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data)