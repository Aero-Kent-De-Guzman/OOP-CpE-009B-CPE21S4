# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:33:20 2024

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
        self.button = QPushButton('Click to Change Color', self)
        self.button.move(30,55)
        self.button.resize(150,20)
        self.button.clicked.connect(self.btn_click)
        self.show()
        
    @pyqtSlot()
    def btn_click(self):
        self.button.setStyleSheet('background-color : yellow')