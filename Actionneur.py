from digi.xbee.devices import XBeeDevice
import time
import RPi.GPIO as GPIO
import threading
import sys
import signal
import os
import fcntl
import time
inputs =[0,0,0]

PORT = "/dev/ttyUSB0"

BAUD_RATE = 9600
device = XBeeDevice(PORT, BAUD_RATE)
device.open()
device.set_parameter("NI", bytearray("ACTIONNEUR", 'utf8'))    
print("Node ID:%s" % device.get_parameter("NI").decode())


fcntl.fcntl(os.open(PORT, os.O_RDWR ), fcntl.F_SETFL, fcntl.FASYNC);
signal.pthread_sigmask(signal.SIG_UNBLOCK,[signal.SIGIO])
signal.signal(signal.SIGIO, ACTIONEUR_HANDLER)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)


def ACTIONEUR_HANDLER(signum, stack):

    time.sleep(0.1)
    xbee_message = device.read_data()
    if xbee_message is not None:
        message = xbee_message.data.decode()
        inputs=message.split(";")
        print(inputs)

        if inputs[0]=="1":
            GPIO.output(37, GPIO.HIGH)
        else:
            GPIO.output(37, GPIO.LOW)
        
        if inputs[1]=="1":
            GPIO.output(38, GPIO.HIGH)
        else:
            GPIO.output(38, GPIO.LOW)

        if inputs[2]=="1":
            GPIO.output(40, GPIO.HIGH)
        else:
            GPIO.output(40, GPIO.LOW)

GPIO.setwarnings(False)
def main():


    global inputs,locker
    while True:
        
        time.sleep(100)

        #print( inputs)
        #print("State: ",msg)





if __name__ == '__main__':
    main()
