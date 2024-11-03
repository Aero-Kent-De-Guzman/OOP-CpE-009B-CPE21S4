import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import re # this module is so that the calculator can check if the expressions are valid...
          # the eval() function can also work but is limited to basic arithmetics...
import math # this module is to enable calculation with sine & cosine, see line 126 & 127
import os
from calculator import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())