from digi.xbee.devices import XBeeDevice
from digi.xbee.util import utils
import os

import time
import sys
import _thread 

import datetime

from PyQt5.QtWidgets import QPlainTextEdit,QApplication,QDialog,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi 
from code import *



#import matplotlib.pyplot as plt  
# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/ttyUSB0"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600
recu=str(2)
status=0
device = XBeeDevice(PORT, BAUD_RATE)
device.open()
device.set_parameter("NI", bytearray("TEST", 'utf8'))
xbee_network = 0
remote_device = 0
#print("Node ID:%s" % device.get_parameter("NI").decode())

device.flush_queues()
#def capteur (device,remote_device):


            # time.sleep(0.01)

            # if float(xbee_message.data.decode())<10:
            #         device.send_data(remote_device, "STOP")
            # else:
            #     device.send_data(remote_device, "RUN")
            #     print()
    
class interface(QDialog):

    def __init__(self):
        super(interface, self).__init__()
        loadUi("untitled.ui",self)        
        self.plainTextEdit.setReadOnly(True)
        self.setWindowTitle('Automate')
        self.pushButton.clicked.connect(self.connect_out)
        self.pushButton_2.clicked.connect(self.connect_in)
        self.pushButton_3.clicked.connect(self.run)


    def connect_out(self):
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Connecting to the sensor...")
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Connected")
        xbee_network = device.get_network()
        remote_device = xbee_network.discover_device("ACTIONEUR")
        _thread.start_new_thread( actioneur, (device,remote_device) )   
        self.label.setText("Staus: On")        


    def connect_in(self):
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Connecting to the actuator...")
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Connected")
        self.label_2.setText("Staus: On")


    def run(self):
        status=1
        while status==1:
            xbee_message = device.read_data()
            if xbee_message is not None:
                status=0
        while True:
            time.sleep(0.00001)
            xbee_message = device.read_data()
            
            if xbee_message is not None:
                millis = int(round(time.time() * 1000))
                global recu
                print(recu)
                if xbee_message.data.decode()=="STOP":
                    print("EMERGENCY STOP")
                    recu=str(-1)
                    device.send_data_async(remote_device, recu)
                    sys.exit(0)
                
                recu = xbee_message.data.decode()
                
           
        if device is not None and device.is_open():
            device.close()


            
def actioneur (device,remote_device):
    global recu
    while True:
    #     device.send_data(remote_device, "RUN")
        # print("teste")
        # time.sleep(1)
        # if float(xbee_message.data.decode())<10:
        #         device.send_data(remote_device, "STOP")
        # else:
        #     device.send_data(remote_device, "RUN")
        #     print()
        
        time.sleep(0.00001)
        #print(recu)
        #if float(xbee_message.data.decode())<10:
        #millis = int(round(time.time() * 1000))

        device.send_data_async(remote_device, recu)
        #else:
         #   device.send_data_async(remote_device, "RUN")
          #  print()         
      







def main():
    obj=code()
    print(obj.test())
    app = QApplication(sys.argv)
    widget=interface()
    widget.show()
    app.exec_()
    run()


 

    
#    _thread.start_new_thread( capteur, (device,remote_device) )



if __name__ == '__main__':
    main()
