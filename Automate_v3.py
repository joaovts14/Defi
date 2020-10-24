from digi.xbee.devices import XBeeDevice
from digi.xbee.util import utils
import time
import sys
import signal
import os
import fcntl
import threading
import datetime
from functools import partial


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



locker = threading.Lock()

outputs=[0]
inputs=[0]

device = XBeeDevice(PORT, BAUD_RATE)
device.open()
device.set_parameter("NI", bytearray("TEST", 'utf8'))
xbee_network = 0
remote_device = 0
print("Node ID:%s" % device.get_parameter("NI").decode())


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
        loadUi("run.ui",self)        
        self.plainTextEdit.setReadOnly(True)
        self.setWindowTitle('Automate')
        self.pushButton.clicked.connect(self.connect_out)
        self.pushButton_2.clicked.connect(self.connect_in)
        self.pushButton_3.clicked.connect(self.stop)



    def connect_out(self):
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Connecting to the actuator...")
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Connected")
        threading.Thread(target=runActioneur).start()
        self.label.setText("Status: On")        


    def connect_in(self):
        global device
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Connecting to the sensor...")
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Connected")
        threading.Thread(target=runCapteur).start() 
        self.label_2.setText("Status: On")
    
    def stop(self):
        #print("ok3")
        global status
        now = datetime.datetime.now()
        self.plainTextEdit.appendPlainText(now.strftime(" %H:%M:%S")+ "  Stop")
        status=-1

def runActioneur ():

    global outputs
    global locker

    xbee_network = device.get_network()
    remote_device = xbee_network.discover_device("ACTIONEUR")
    
    while True:
        
        
        #locker.acquire()
        time.sleep(0.0001)
        device.send_data_async(remote_device, str(outputs[0]))
        #locker.release()

def runCapteur (xbee_message):
    #global recu
    global inputs
    global outputs
    global status
    global locker
    time.sleep(0.0001)
    test=code()
    #time.sleep(0.001)
   
    if xbee_message is not None:
        #millis = int(round(time.time() * 1000))
        message=xbee_message.data.decode()            
       # if message=="STOP":
        #   print("EMERGENCY STOP")
         #  device.send_data_async(remote_device, str(-1))
          # status=-1
        #locker.acquire()
        inputs[0] = message
        outputs = test.logic(inputs)
        print(inputs[0] ,"%5.0f" %( xbee_message.timestamp*1000))
        #locker.release()
    
    #if device is not None and device.is_open():
     #   device.close() 

class Capteur:
    compteur_id = 0
    def __init__(self):
        self.id = Capteur.compteur_id
        Capteur.compteur_id=Capteur.compteur_id +1
        device.add_data_received_callback(runCapteur)


class Actioneur:
    compteur_id = 0
    def __init__(self):
        self.id = Actioneur.compteur_id
        Actioneur.compteur_id=self.compteur_id +1
        threading.Thread(target=runActioneur).start()



def main():

    #app = QApplication(sys.argv)
    #widget=interface()
    #widget.show()
    #app.exec_()
    
    Capteur1=Capteur()
    Capteur2=Capteur()
    print(Capteur1.id)
    print(Capteur2.id)

    Actioneur1=Actioneur()

    while True:
        time.sleep(10)





if __name__ == '__main__':
    main()
