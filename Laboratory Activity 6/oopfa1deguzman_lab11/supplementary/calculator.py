import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Calculator(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notepad")
        self.setWindowIcon(QIcon('pythonico.ico'))
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
        
        fontButton = QAction('Font', self)
        fontButton.setShortcut('ctrl+D')
        fontButton.triggered.connect(self.showFontDialog)
        editMenu.addAction(fontButton)
        
        saveButton = QAction('Save', self)
        saveButton.setShortcut('ctrl+S')
        saveButton.triggered.connect(self.saveFileDialog)
        fileMenu.addAction(saveButton)
        
        openButton = QAction('Open', self)
        openButton.setShortcut('ctrl+O')
        openButton.triggered.connect(self.openFileNameDialog)
        fileMenu.addAction(openButton)
        
        exitButton = QAction('Exit', self)
        exitButton.setShortcut('ctrl+Q')
        exitButton.setStatusTip('Exit Application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        
    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.notepad.text.setFont(font)
            
    def saveFileDialog(self):
        options = QFileDialog.Options()
        # options = QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Notepad File", "",
                                                  "Text Files (*.txt);;Python Files (*.py);;All files (*)", options = options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.notepad.text.toPlainText())
                
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        # options = QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Notepad File", "",
                                                  "Text Files (*.txt);;Python Files (*.py);;All files (*)", options = options)
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.notepad.text.setText(data)
                
    def cleartext(self):
        self.notepad.text.clear()
        
    def loadwidget(self):
        self.notepad = calculatorButtons()
        self.setCentralWidget(self.notepad)

class calculatorButtons(QWidget):

    def __init__(self):
        super(calculatorButtons, self).__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        
        names = [
                '7', '8', '9', '/',''
                '4', '5', '6', '*',''
                '1', '2', '3', '-',''
                '0', '.', '=', '+',''
                '', '', '', '', '']
        
        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0,1,1,5)
        
        
        positions = [(i,j) for i in range(1,7) for j in range(1,6)]
        for position, name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(self.on_click)
            grid.addWidget(button, *position)
            
        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Grid Layout')
        self.show()
        
    @pyqtSlot()
    def on_click(self):
        if grid.button('1'):
            self.textLine.insert('1')
        if grid.button('2'):
            self.textLine.insert('2')

        
        
        
        
        
        
        
        