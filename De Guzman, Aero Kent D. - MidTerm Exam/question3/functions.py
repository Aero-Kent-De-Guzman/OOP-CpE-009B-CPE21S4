# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:35:16 2024

@author: De Guzman, Aero Kent D.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        # window = QMainWindow()
        self.title = "First OOP GUI"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(250,250,350,350)
        
        self.Name = QLabel("First Name : ", self)
        self.Name.move(35,30)
        self.Name.textbox = QLineEdit(self)
        self.Name.textbox.move(200, 35)
        self.Name.textbox.resize(100, 20)
        self.Name.textbox.setText('')
        
        self.button = QPushButton('Click to display your Fullname', self)
        self.button.move(30,55)
        self.button.resize(150,20)
        self.button.textbox = QLineEdit(self)
        self.button.textbox.move(200, 55)
        self.button.textbox.resize(100, 20)
        self.button.clicked.connect(self.btn_click)
        
        self.show()
        
    @pyqtSlot()
    def btn_click(self):
        temp = self.Name.textbox.text()
        self.button.textbox.setText(temp)