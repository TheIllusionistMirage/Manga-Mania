#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication
from gui import GUI



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    g = GUI()
    sys.exit(app.exec_())
