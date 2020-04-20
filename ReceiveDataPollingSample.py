from digi.xbee.devices import XBeeDevice
from digi.xbee.util import utils
import os

import time
import sys
import _thread 
import threading

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
print("Node ID:%s" % device.get_parameter("NI").decode())

device.flush_queues()

outputs=[0]
inputs=[0]



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
        loadUi("run.ui",self)        
        self.plainTextEdit.setReadOnly(True)
        self.setWindowTitle('Automate')
        self.pushButton.clicked.connect(self.connect_out)
        self.pushButton_2.clicked.connect(self.connect_in)
        self.pushButton_3.clicked.connect(self.stop)



    def connect_out(self):
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Connecting to the sensor...")
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Connected")
        threading.Thread(target=runActioneur,args=[device]).start()
        self.label.setText("Staus: On")        


    def connect_in(self):
        global device
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Connecting to the actuator...")
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Connected")
        threading.Thread(target=runCapteur,args=[device]).start() 
        self.label_2.setText("Staus: On")
    
    def stop(self):
        #print("olas")
        global status
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Stop")
        status=-1

def runActioneur (device):
    global recu
    global outputs
    xbee_network = device.get_network()
    remote_device = xbee_network.discover_device("ACTIONEUR")
    
    while True:
        time.sleep(0.001)
        device.send_data_async(remote_device, str(outputs[0]))


def runCapteur (device):
    global recu
    global inputs
    global outputs
    global status
    test=code()
    

    status=1
    while status!=-1:
        time.sleep(0.001)
        xbee_message = device.read_data()
        
        if xbee_message is not None:
            #millis = int(round(time.time() * 1000))
            
            if xbee_message.data.decode()=="STOP":
               print("EMERGENCY STOP")
               device.send_data_async(remote_device, str(-1))
               status=-1
            
            inputs[0] = xbee_message.data.decode()
            outputs = test.logic(inputs)
            #print(inputs[0])
        
    if device is not None and device.is_open():
        device.close() 


               # "Thread-x finished!"
def main():

    app = QApplication(sys.argv)
    widget=interface()
    widget.show()
    app.exec_()
    #_thread.start_new_thread( actioneur1, (device,remote_device) )
    #actioneur1(device,remote_device)
    #teste=MyThread(name="ola")
    #teste.run()

    

    #while True:
     #   if input1 == 0:
      #      output1=1


    #capteur1 = Capteur(name="teste1")
    #capteur1.run()
    #print("tes")
    #actioneur1 = Actioneur(name="teste2")
    #actioneur1.run()
    

 

    
#    _thread.start_new_thread( capteur, (device,remote_device) )



if __name__ == '__main__':
    main()
