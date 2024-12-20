import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QMessageBox, QLineEdit, QLabel, QGridLayout
from PyQt5.QtGui import QIcon

class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "PyQt Login Screen"        
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico')) # Currently no icon for this to work...
        
        self.createGridLayout()
        self.setLayout(self.layout)
        self.show()
        
    def createGridLayout(self):
        self.layout = QGridLayout()
        
        self.layout.setColumnStretch(1,2)
        
        self.textboxbl = QLabel("Text: ", self)
        self.textbox = QLineEdit(self)
        self.passwordbl = QLabel("Password: ", self)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.button = QPushButton('Register', self)
        self.button.setToolTip("You've hovered over me!")
        self.layout.addWidget(self.textboxbl,0,1)
        self.layout.addWidget(self.textbox, 0,2)
        self.layout.addWidget(self.passwordbl, 1, 1)
        self.layout.addWidget(self.password, 1, 2)
        self.layout.addWidget(self.button, 2, 2)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())