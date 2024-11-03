import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import re # this module is so that the calculator can check if the expressions are valid...
          # the eval() function can also work but is limited to basic arithmetics...
import math # this module is to enable calculation with sine & cosine, see line 126 & 127
import os

class Calculator(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon('calcPhoto.ico'))
        self.loadmenu()
        
        self.loadwidget()
        self.show()
        
    def loadmenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        
        editButton = QAction('Clear', self)
        editButton.setShortcut('ctrl+M')
        editButton.triggered.connect(self.cleartext)
        editMenu.addAction(editButton)

        hisClearButton = QAction('Reset History', self)
        hisClearButton.setShortcut('ctrl+shift+H')
        hisClearButton.triggered.connect(self.ClearCalcHistory)
        editMenu.addAction(hisClearButton)
        
        exitButton = QAction('Exit', self)
        exitButton.setShortcut('ctrl+Q')
        exitButton.setStatusTip('Exit Application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        historyButton = QAction('History', self)
        historyButton.setShortcut('ctrl+H')
        historyButton.setStatusTip('Calculator History')
        historyButton.triggered.connect(self.CalcHistory)
        fileMenu.addAction(historyButton)
    
    def CalcHistory(self):
        CalcHistory = 'CalculatorHistory.txt'
        if os.path.exists(CalcHistory):
            os.startfile(CalcHistory)
        else:
            QMessageBox.warning(self, "Error", "No history file found.")
    
    def ClearCalcHistory(self):
        with open('CalculatorHistory.txt', 'w') as txt:
            txt.write('')
            
    def cleartext(self):
        self.Calculator.textLine.setText('')
        
    def loadwidget(self):
        self.Calculator = calculatorButtons()
        self.setCentralWidget(self.Calculator)

class calculatorButtons(QWidget):

    def __init__(self):
        super(calculatorButtons, self).__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        
        names = [
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+',
                'C', 'sin(', '(', ')',
                '**','cos(','','']
        
        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0, 1, 1, 5)
        
        positions = [(i, j) for i in range(1, 7) for j in range(1, 5)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(lambda checked, btn=name: self.on_click(btn))
            grid.addWidget(button, *position)
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Calculator')
        self.show()
        
    @pyqtSlot()
    def on_click(self, btn_text):
        if btn_text == '=':
            btn_num = self.textLine.text()
            with open('CalculatorHistory.txt', 'a') as txt:
                txt.write(btn_num + '\n')

            if re.match(r'^[\d\+\-\*\/\.\(\) sincos]+$', btn_num):
                btn_num = btn_num.replace('sin(', 'math.sin(')
                btn_num = btn_num.replace('cos(', 'math.cos(')
                if self.is_valid_expression(btn_num):
                    result = eval(btn_num)
                    result = round(result, 5)
                    self.textLine.setText(str(result))
                    with open('CalculatorHistory.txt', 'a') as txt:
                        txt.write('=' + str(result) + '\n')
                else:
                    self.textLine.setText("Syntax Error")
            else:
                self.textLine.setText("Syntax Error")

        elif btn_text == 'C':
            self.textLine.setText('')
        else:
            self.textLine.insert(btn_text)

    def is_valid_expression(self, expression):
        unmatched_parenthesis = 0
        for char in expression:
            if char == '(':
                unmatched_parenthesis += 1
            elif char == ')':
                unmatched_parenthesis -= 1
                if unmatched_parenthesis < 0:
                    return False
        return unmatched_parenthesis == 0