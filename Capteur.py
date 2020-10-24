from digi.xbee.devices import XBeeDevice
from digi.xbee.util import utils
import RPi.GPIO as GPIO
import time
import sys
import threading
input=[0,0,0]
PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600
A=False
B=False
C=False
GPIO.setmode(GPIO.BOARD)
REMOTE_NODE_ID = "AUTOMATE"
GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(36,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(36,GPIO.OUT)
#GPIO.setup(40,GPIO.OUT)
GPIO.setwarnings(False)
#GPIO.output(36,GPIO.LOW)
#GPIO.output(40,GPIO.LOW)
locker1 = threading.Lock()
locker2 = threading.Lock()
case=0
def Stop(channel):
    global device  
    global remote_device
    print ("EMERGENCY STOP")
    GPIO.cleanup()
    device.send_data(remote_device, "STOP")
    sys.exit(0)

def multiples():
    locker2.acquire()
    time.sleep(0.2)
    locker2.release()


def active1(channel):
    global case
    global input
    if locker2.locked()==False :
        threading.Thread(target=multiples).start()
        time.sleep(0.1)

        if GPIO.input(37)==True :
            A=True
        else :
            A=False

        if GPIO.input(36)==True :
            B=True
        else :
            B=False

        if GPIO.input(38)==True :
            C=True
        else :
            C=False


        if (A and B and C): #changer tous les valeurs
            case=1
        elif (A and B): #changer 2
            case=2
        elif (A and C): #changer 2
            case=3
        elif (B and C): #changer 2
            case=4
        else:           #changer 1
            case=5


        if (channel == 37 and case==5) or case==1 or case==2 or case==3 :
            if input[0]==0:
                input[0]=1  
                time.sleep(0.01)
            else :
                input[0]=0   
                time.sleep(0.01)
        if (channel == 36 and case==5) or case==1 or case==2 or case==4 :
            if input[1]==0:
                input[1]=1    
                time.sleep(0.01)
            else :
                input[1]=0    
                time.sleep(0.01)  
        if (channel == 38 and case==5) or case==1 or case==3 or case==4 :
            if input[2]==0:
                input[2]=1    
                time.sleep(0.01)
            else :
                input[2]=0
            time.sleep(0.01)

        print(input)
        device.send_data_async(remote_device, str(input[0])+";"+str(input[1])+";"+str(input[2]))  



def main():

 
    GPIO.add_event_detect(36, GPIO.RISING, callback=active1)

    GPIO.add_event_detect(37, GPIO.RISING, callback=active1)

    GPIO.add_event_detect(38, GPIO.RISING, callback=active1)
    
    global device 
    device= XBeeDevice(PORT, BAUD_RATE)
    device.open()
    device.set_parameter("NI", bytearray("CAPTEUR", 'utf8'))
    print("Node ID:%s" % device.get_parameter("NI").decode())
    status="ok"
    global remote_device
    try:
        
        xbee_network = device.get_network()
        remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
        
        if remote_device is None:
            print("Could not find the remote device")
            #exit(1)
               
        while True:
     
            time.sleep(10) 

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()
