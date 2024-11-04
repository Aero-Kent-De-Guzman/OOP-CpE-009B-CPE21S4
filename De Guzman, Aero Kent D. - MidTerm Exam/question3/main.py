# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:34:55 2024

@author: TIPQC
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot
from functions import App

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())