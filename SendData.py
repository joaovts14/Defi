


from digi.xbee.devices import XBeeDevice
import RPi.GPIO as GPIO
import time


PORT = "/dev/ttyUSB0"

BAUD_RATE = 9600
GPIO.setmode(GPIO.BOARD)

tempLED = 0.07
REMOTE_NODE_ID = " "
GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(7,GPIO.LOW)
GPIO.output(11,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(15,GPIO.LOW)
GPIO.output(35,GPIO.LOW)
GPIO.output(33,GPIO.LOW)
GPIO.output(31,GPIO.LOW)
GPIO.output(29,GPIO.LOW)
GPIO.output(38,GPIO.LOW)
GPIO.output(36,GPIO.LOW)
GPIO.output(40,GPIO.LOW)

def main():
    
    device = XBeeDevice(PORT, BAUD_RATE)
    status="ok"
    try:
        device.open()
        xbee_network = device.get_network()
        remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
        
        if remote_device is None:
            print("Could not find the remote device")
            exit(1)
        i=1
        
        while i==1:    
            if GPIO.input(37)==GPIO.HIGH :
                i=0

        GPIO.output(7,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(11,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(11,GPIO.LOW)
        GPIO.output(13,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(15,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(35,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(35,GPIO.LOW)
        GPIO.output(33,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(33,GPIO.LOW)
        GPIO.output(31,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(31,GPIO.LOW)
        GPIO.output(29,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(29,GPIO.LOW)
        GPIO.output(38,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(38,GPIO.LOW)
        GPIO.output(38,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(38,GPIO.LOW)
        GPIO.output(29,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(29,GPIO.LOW)
        GPIO.output(31,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(31,GPIO.LOW)
        GPIO.output(33,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(33,GPIO.LOW)
        GPIO.output(35,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(35,GPIO.LOW)
        GPIO.output(15,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(13,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(11,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(11,GPIO.LOW)
        GPIO.output(7,GPIO.HIGH)
        time.sleep(tempLED)
        GPIO.output(7,GPIO.LOW)
                
        while i==0:
            
            
            Trig = 16         
            Echo = 18         

            GPIO.setup(Trig,GPIO.OUT)
            GPIO.setup(Echo,GPIO.IN)

            GPIO.output(Trig, False)

            time.sleep(0.10)       

            GPIO.output(Trig, True)
            time.sleep(0.00000001)
            GPIO.output(Trig, False)

            while GPIO.input(Echo)==0:  
              debutImpulsion = time.time()

            while GPIO.input(Echo)==1:  
              finImpulsion = time.time()

            distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s
            if distance < 4:
                
                GPIO.output(7,GPIO.HIGH)
                GPIO.output(11,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(15,GPIO.HIGH)
                GPIO.output(35,GPIO.HIGH)
                GPIO.output(33,GPIO.HIGH)
                GPIO.output(31,GPIO.HIGH)
                GPIO.output(29,GPIO.HIGH)
                GPIO.output(38,GPIO.HIGH)

            elif distance < 6:
                GPIO.output(7,GPIO.HIGH)
                GPIO.output(11,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(15,GPIO.HIGH)
                GPIO.output(35,GPIO.HIGH)
                GPIO.output(33,GPIO.HIGH)
                GPIO.output(31,GPIO.HIGH)
                GPIO.output(29,GPIO.HIGH)
                GPIO.output(38,GPIO.LOW)
            elif distance < 8:
                GPIO.output(7,GPIO.HIGH)
                GPIO.output(11,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(15,GPIO.HIGH)
                GPIO.output(35,GPIO.HIGH)
                GPIO.output(33,GPIO.HIGH)
                GPIO.output(31,GPIO.HIGH)
                GPIO.output(29,GPIO.LOW)
                GPIO.output(38,GPIO.LOW)
            elif distance < 10:
                GPIO.output(7,GPIO.HIGH)
                GPIO.output(11,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(15,GPIO.HIGH)
                GPIO.output(35,GPIO.HIGH)
                GPIO.output(33,GPIO.HIGH)
                GPIO.output(31,GPIO.LOW)
                GPIO.output(29,GPIO.LOW)
                GPIO.output(38,GPIO.LOW)
            elif distance < 12:
                GPIO.output(7,GPIO.HIGH)
                GPIO.output(11,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(15,GPIO.HIGH)
                GPIO.output(35,GPIO.HIGH)
                GPIO.output(33,GPIO.LOW)
                GPIO.output(31,GPIO.LOW)
                GPIO.output(29,GPIO.LOW)
                GPIO.output(38,GPIO.LOW)
            elif distance < 14:
                GPIO.output(7,GPIO.HIGH)
                GPIO.output(11,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(15,GPIO.HIGH)
                GPIO.output(35,GPIO.HIGH)
                GPIO.output(33,GPIO.LOW)
                GPIO.output(31,GPIO.LOW)
                GPIO.output(29,GPIO.LOW)
                GPIO.output(38,GPIO.LOW)
            elif distance < 16:
                GPIO.output(7,GPIO.HIGH)
                GPIO.output(11,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(15,GPIO.HIGH)
                GPIO.output(35,GPIO.LOW)
                GPIO.output(33,GPIO.LOW)
                GPIO.output(31,GPIO.LOW)
                GPIO.output(29,GPIO.LOW)
                GPIO.output(38,GPIO.LOW)
            elif distance < 18:
                GPIO.output(7,GPIO.HIGH)
                GPIO.output(11,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(15,GPIO.LOW)
                GPIO.output(35,GPIO.LOW)
                GPIO.output(33,GPIO.LOW)
                GPIO.output(31,GPIO.LOW)
                GPIO.output(29,GPIO.LOW)
                GPIO.output(38,GPIO.LOW)
            elif distance < 20:
                GPIO.output(7,GPIO.HIGH)
                GPIO.output(11,GPIO.HIGH)
                GPIO.output(13,GPIO.LOW)
                GPIO.output(15,GPIO.LOW)
                GPIO.output(35,GPIO.LOW)
                GPIO.output(33,GPIO.LOW)
                GPIO.output(31,GPIO.LOW)
                GPIO.output(29,GPIO.LOW)
                GPIO.output(38,GPIO.LOW)
            elif distance < 22:
                GPIO.output(7,GPIO.HIGH)
                GPIO.output(11,GPIO.LOW)
                GPIO.output(13,GPIO.LOW)
                GPIO.output(15,GPIO.LOW)
                GPIO.output(35,GPIO.LOW)
                GPIO.output(33,GPIO.LOW)
                GPIO.output(31,GPIO.LOW)
                GPIO.output(29,GPIO.LOW)
                GPIO.output(38,GPIO.LOW)
            else:
                GPIO.output(7,GPIO.LOW)
                GPIO.output(11,GPIO.LOW)
                GPIO.output(13,GPIO.LOW)
                GPIO.output(15,GPIO.LOW)
                GPIO.output(35,GPIO.LOW)
                GPIO.output(33,GPIO.LOW)
                GPIO.output(31,GPIO.LOW)
                GPIO.output(29,GPIO.LOW)
                GPIO.output(38,GPIO.LOW)                
            DATA_TO_SEND=str(distance)
            device.send_data(remote_device, DATA_TO_SEND)
            

            

            while True:
                xbee_message = device.read_data()
                if xbee_message is not None:
                    STATUS=xbee_message.data.decode()
                    print(STATUS)
                    if STATUS=="RUN":
                        GPIO.output(36,GPIO.HIGH)
                    else:
                        GPIO.output(40,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(36,GPIO.LOW)
                    GPIO.output(40,GPIO.LOW)
                    break
                    
            if GPIO.input(37)==GPIO.HIGH :
                break
            
            

        GPIO.cleanup()


    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()
