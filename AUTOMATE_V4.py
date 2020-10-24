import os

import time
import sys
import _thread 

import datetime

from PyQt5.QtWidgets import QPlainTextEdit,QApplication,QDialog,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi 


class interface(QDialog):

    def __init__(self):
        super(interface, self).__init__()
        loadUi("main.ui",self)        
    #    self.plainTextEdit.setReadOnly(True)
        self.setWindowTitle('Automate')
        self.pushButton.clicked.connect(self.run)
    def run(self):
    	os.system("python3 ReceiveDataPollingSample_v4.py")

          

def main():
    app = QApplication(sys.argv)
    widget=interface()
    widget.show()
    app.exec_()
    run()


 

    
#    _thread.start_new_thread( capteur, (device,remote_device) )



if __name__ == '__main__':
    main()
